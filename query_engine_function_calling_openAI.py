
from retreiver import *
import openai
from llama_index.agent import OpenAIAgent
from  HelperFunctionsSpec import *
from llama_index.tools import QueryEngineTool, ToolMetadata
from indexer import *
from prompt import CUSTOMER_SUPPORT_AGENT
from llama_index.llms import OpenAI

openai.api_key = "sk-"
llm =OpenAI(temperature=0)

query_engine_tools = [
    QueryEngineTool(
        query_engine=getQueryIndex(),
        metadata=ToolMetadata(
            name="support_bot_qe",
            description=(
                "Provides contextual information about the  questions asked by the user in chat"
                "Always consult this first before calling other tools"
            ),
        ),
    ),
]


def chat(query):
    theAgent = OpenAIAgent.from_tools(tools = HelperFunctionSpec().to_tool_list(), verbose=True, llm =llm, system_prompt=CUSTOMER_SUPPORT_AGENT)
    #print(theAgent.chat ("Use only the provided context to answer the question: -" +  query ))
    print(theAgent.chat (getContext(query)))


chat("I am refused entry into the portal")
#chat("I cannot reset my password")
#chat("My user Id is 34191010")