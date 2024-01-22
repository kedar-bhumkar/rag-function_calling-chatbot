from llama_index.tools.tool_spec.base import BaseToolSpec

class HelperFunctionSpec(BaseToolSpec):
    spec_functions = ["checkUserExitsIinACL", "addUserInACL"]

    def addUserInACL(self):
        "A tool to add a user inside the patient portal access-control-list"
        return "User added successfully"    

    def checkUserExitsIinACL(self):
        "A tool to check if  a  user exists in  the patient portal access-control-list"
        #return "User does not exist in ACL"
        return "User already  exists in ACL"