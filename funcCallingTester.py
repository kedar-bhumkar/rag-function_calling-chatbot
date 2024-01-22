import openai
from llama_index.agent import OpenAIAgent
from  HelperFunctionsSpec import *
openai.api_key = "sk-"

theAgent = OpenAIAgent.from_tools(HelperFunctionSpec().to_tool_list(), verbose=True)
print(theAgent.chat('Follow the below steps 1. Grab the userId of this user 2. Check inside the patient  portal access-control-list if this user has been added 3. If not added, add the userID to this list 4. Inform the user to check if they can access the patient portal.'))


