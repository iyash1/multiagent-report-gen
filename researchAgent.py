import os, requests
from colorama import Fore, Style, init
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
from dataModels import TavilySearchParams, AnalysisSummary
from constants import RESEARCH_AGENT_NAME, TAVILY_SEARCH_URL, GPT_MODEL_4

load_dotenv()
init(autoreset=True)

# ------------------------------------------------------------------
# Define the Tavily search tool
# ------------------------------------------------------------------

tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError(f"{Fore.RED} ➡️ TAVILY_API_KEY not found in environment variables. ❌ {Style.RESET_ALL}")
else:
    print(f""" {Fore.GREEN} ➡️ Tavily API key loaded successfully. ✅ {Style.RESET_ALL}""")

@function_tool
def tavily_search(params: TavilySearchParams) -> str:
    try:
        url = TAVILY_SEARCH_URL
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": tavily_api_key,
            "query": params["query"],
            "max_results": params.get("max_results", 3),
        }

        response = requests.post(url, json = payload, headers = headers, timeout=60)
        if response.status_code == 200:
            results = response.json().get("results", [])
            summary = "\n".join([f"- {r['title']}: {r['content']}" for r in results])
            return summary if summary else "No relevant results found."
        else:
            return f"Tavily API error: {response.status_code}"
    except Exception as e:
        return f"Error calling Tavily API: {str(e)}"

# ------------------------------------------------------------------
# Define the Researcher Agent
# ------------------------------------------------------------------

def getResearcherAgent():
    researcher_agent = Agent(name = RESEARCH_AGENT_NAME,
                             instructions = """
    ## Context
    You are a research agent with access to the Tavily search tool.

    ## Instruction
    Given a user query, use the Tavily search tool to find relevant information and summarize the key findings.

    ## Input
    - A research query from the user.

    ## Output
    - A summary of key findings in a maximum of 5 bullet points.
    """,
        model = GPT_MODEL_4,
        tools = [tavily_search],
        output_type = AnalysisSummary)

    return researcher_agent