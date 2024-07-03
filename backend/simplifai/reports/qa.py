import argparse

# from langchain_community.llms import Ollama
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import PromptTemplate
# from langchain.chains import RetrievalQA

from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .to_nepali import nepali_translator as to_np
from mindsdb_sdk import connect
from dotenv import load_dotenv
import os

class QA:
    def __init__(self):
        # load_dotenv()
        # self.server_url = os.getenv('MINDS_DB')
        self.server = connect('http://172.17.0.1:47334')
        self.project = self.server.get_project('mindsdb')
        self.model = self.project.get_model('simplifai')

    def _ask_non_rag(self, query: str, isDoctor: bool, isEnglish:bool) -> str:
        print(f'qurey in non rag: { query}') 

        template_simple = f"""Answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        you can't give a false answer,
        Answer in very simple words
        
        Question: {query}
        Helpful Answer:"""

        template_doctor= f"""Answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        you can't give a false answer,
        Answer using medical terms
        
        Question: {query}
        Helpful Answer:"""

        if isDoctor:
            template = template_doctor
        else:
            template = template_simple

        result = self.model.predict({'text': template})
        response_eng  = result.loc[0, 'completion']  # Assuming result is a DataFrame

        print(f'qa : {query}: { response_eng}')

        if isEnglish:
            response = response_eng
        else:
            response = to_np(response_eng)
        
        return response





