from langchain.tools import Tool
import wikipedia

def get_wiki_tool(sentences: int = 2):
    def search_wikipedia(query: str) -> str:
        try:
            return wikipedia.summary(query, sentences=sentences)
        except:
            return "Wikipedia'da uygun sonuç bulunamadı."

    return Tool(
        name="Wikipedia",
        func=search_wikipedia,
        description="Uses Wikipedia to answer questions about general knowledge."
    )
