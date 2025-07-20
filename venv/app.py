import streamlit as st
from langchain.agents import initialize_agent, AgentType
from tools import get_wiki_tool
from llm import llm

st.set_page_config(page_title="Wikipedia Chat Agent", page_icon="📚")
st.title("📚 Wikipedia Chat Agent")
st.markdown("Wikipedia + LLM ile çalışan bir soru-cevap ajanı.")

# Sohbet geçmişi
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Cümle sayısı ayarı
sentences = st.slider("📏 Kaç cümlelik Wikipedia özeti alınsın?", 1, 10, 2)

# Form: Soru + buton
with st.form(key="query_form"):
    query = st.text_input("❓ Sorunuz:", placeholder="Kuantum bilgisayar nedir?")
    submit = st.form_submit_button("Yanıtla")

# Soruyu işleme
if submit and query:
    wiki_tool = get_wiki_tool(sentences=sentences)

    agent = initialize_agent(
        tools=[wiki_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    with st.spinner("🧠 Yanıt hazırlanıyor..."):
        try:
            answer = agent.run(query)
        except Exception as e:
            answer = f"Hata oluştu: {e}"

    st.session_state.chat_history.append((query, answer))

# Geçmişi göster
if st.session_state.chat_history:
    st.markdown("## 💬 Sohbet Geçmişi")
    for user_q, agent_a in reversed(st.session_state.chat_history):
        st.markdown(f"**Sen:** {user_q}")
        st.markdown(f"**Agent:** {agent_a}")
        st.markdown("---")
