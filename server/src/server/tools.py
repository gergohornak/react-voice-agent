from langchain_core.tools import tool

from langchain_community.tools import TavilySearchResults


@tool
def add(a: int, b: int):
    """Add two numbers. Please let the user know that you're adding the numbers BEFORE you call the tool"""
    return a + b


tavily_tool = TavilySearchResults(
    max_results=5,
    include_answer=True,
    description=(
        "This is a search tool for accessing the internet.\n\n"
        "Let the user know you're asking your friend Tavily for help before you call the tool."
    ),
)



@tool
def report_incident(section: str, severity: str, detail: str):
    """Report an incident to the database with the given section from Preprocessing, Cooking, Storage, Packaging, severity from Minor, Medium or Severe, and detail of the incident."""
    print('!!!!!!!!!!!!!!!!!!!Incident reported', section, severity, detail)


    url = 'https://api.retool.com/v1/workflows/08a2cee8-4dac-42c2-976b-7d4304bbfcb5/startTrigger'

    import requests
    myobj = {'section': section, 'severity': severity, 'detail': detail}

    x = requests.post(url, json = myobj, headers={"X-Workflow-Api-Key":"retool_wk_c0e61e552a8740d7a3d130a3a1b37e38"})

    print(x.text)


    return f"Reported successfully"


TOOLS = [add, tavily_tool, report_incident]