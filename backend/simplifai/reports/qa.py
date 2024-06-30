import argparse

from langchain_community.llms import Ollama
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .to_nepali import nepali_translator as to_np

class QA:
    def __init__(self):
        # self.args = args
        self.llm = Ollama(model="anoob/simp2:latest")
        # self.llm = Ollama(model="simp2:latest",  callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
        
    def _ask_rag(self, query: str) -> str:
        model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"
        gpt4all_kwargs = {'allow_download': 'True'}
        embeddings = GPT4AllEmbeddings(
            model_name=model_name,
            gpt4all_kwargs=gpt4all_kwargs
        )
        persist_dir = 'db'
        vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

        template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Use as simple sentences as possible.
        {context}
        Question: {question}
        Helpful Answer:"""
        QA_CHAIN_PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        # Retrieves the appropriate context from the vector DB:
        qa_chain = RetrievalQA.from_chain_type(
            self.llm,
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        )
        response = qa_chain.invoke({"query": query})
        return response["result"]
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

        response_eng = self.llm.invoke(template)
        print(f'qa : {query}: { response_eng}')

        if isEnglish:
            response = response_eng
        else:
            response = to_np(response_eng)
        
        return response


import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Ask questions to your documents.")
    parser.add_argument("--no-rag", action='store_true', help="Get your answer without RAG")
    return parser.parse_args()


# args = parse_arguments()
# qa = QA(args)

# query = input("Query?: ")
# response = qa._ask_non_rag(query)


# print(f'Simplify: {response}')

