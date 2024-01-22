from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.schema import TextNode
from data_reader import getData
from llama_index.tools import QueryEngineTool
import openai
from llama_index.agent import OpenAIAgent
from  HelperFunctionsSpec import *
openai.api_key = "sk-"

def createIndex():
    documents = SimpleDirectoryReader("data").load_data()
    data = getData()
    textNodes =[]
    for idx, row in enumerate(data.items()):
        concept, comments = row
        textNodes.append(TextNode(text="The following concept " + concept +  " is explained by this explanation " +  comments + ".", id_=idx))       
    return VectorStoreIndex(textNodes)
       

def queryFromIndex():
    the_query_engine = createIndex().as_query_engine()
    response = the_query_engine.query("Use only the provided context to answer the question - I am refused enrty into the portal")    
    print(response)
    response = the_query_engine.query("My userId is U-23323245")    
    print(response)


def getQueryIndex():
    return createIndex().as_query_engine()
   
#queryFromIndex()

   
