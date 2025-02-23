from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool

from pydantic import BaseModel, Field


class LoanCheckInput(BaseModel):
    # Check the input for open an account
    account_number: int = Field(description="Number of the account to check if there is a loan.")
    client_name: str = Field(description="The name of the client")


class LoanCheckTool(BaseTool):
    name: str = "loan_check"
    description: str = "Use this tool when you need you need to check if a client has a open loan and the upcoming installment date. You need to ask the client to provide an account number and a name."

    args_schema: Type[BaseModel] = LoanCheckInput
    return_direct: bool = False

    def _run(self, account_number: int, client_name: str, run_manager: Optional[CallbackManagerForToolRun] = None):
        loan_check = self.loan_check(account_number, client_name)
        return loan_check

    def loan_check(self, account_number: int, client_name: str):
        # Prepare the data as a JSON dictionary

        ### TODO: it is still necessary to create some validation function to verify each item
        account_details = {
            "account_number": account_number,
            "name_of_client": client_name,
        }

        #### Make the API call
        ## api_url = "https://openaccount.fake/"
        ## response = requests.post(api_url, data=account_details)
        ####

        clients = {
            123456789: ("John Doe", 5),
            987654321: ("Jane Smith", 10),
            111222333: ("Alice Johnson", -15),
            444555666: ("Bob Brown", 0),
            777888999: ("Charlie Davis", 0),
            101010101: ("Diana Evans", 30),
        }

        client_info = clients.get(account_details.get("account_number"))
        if client_info and client_info[0] == account_details.get("name_of_client"):
            return {
                "upcoming_in_days": client_info[1],
                "status": "success"
            }
        else:
            return {
                "upcoming_in_days": 0,
                "status": "failure"
            }
