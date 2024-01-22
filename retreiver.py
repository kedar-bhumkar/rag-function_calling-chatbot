from llama_index import VectorStoreIndex
from llama_index.retrievers import  VectorIndexRetriever
from indexer import *
from llama_index.schema import TextNode

def getContext(query):
    print('User query...', query )
    #retriever = createIndex().as_retriever()
    retriever = VectorIndexRetriever(index = createIndex(), similarity_top_k  = 1)
    nodes = retriever.retrieve(query)
    print("Closest matching data chunk - ",nodes[0].text)

    return nodes[0].text

#getContext("I am refused enrty into the portal")
