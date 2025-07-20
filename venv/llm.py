from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base", 
    model_kwargs={"temperature": 0.3, "max_new_tokens": 256}
)
