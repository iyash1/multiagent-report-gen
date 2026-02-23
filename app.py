import os, asyncio
from colorama import Fore, Style, init
from dotenv import load_dotenv
from agents import Runner, SQLiteSession
from researchAgent import getResearcherAgent
from analystAgent import getAnalystAgent
from writerAgent import getWriterAgent
from dataModels import FinalReport

# ------------------------------------------------------------------
# Load environment variables and initialize colorama
# ------------------------------------------------------------------
print(f" {Fore.GREEN} ➡️ Loading environment variables and initializing...{Style.RESET_ALL}")
load_dotenv()
init(autoreset=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError(f"{Fore.RED} ➡️ OPENAI_API_KEY not found in environment variables. ❌ {Style.RESET_ALL}")
else:
    print(f""" {Fore.GREEN} ➡️ OPENAI API key loaded successfully. ✅ {Style.RESET_ALL}""")

# ---------------------------------------------------------------------------
# Orchestrating function to run the agents and pass information between them
# ---------------------------------------------------------------------------
session = SQLiteSession("research_agent_practice")
async def main(user_query: str):
    try:
        # Step 1: Run the researcher agent to gather information about the user's query
        researcher_agent = getResearcherAgent()
        researcher_result = await Runner.run(researcher_agent, user_query, session = session)
        research_summary = researcher_result.final_output.summary  # Get the short research summary

        # Step 2: Run the analyst agent to analyze the research findings
        analyst_agent = getAnalystAgent()
        analyst_result = await Runner.run(analyst_agent, research_summary, session = session)
        analysis_summary = analyst_result.final_output.summary  # Get the short analysis summary

        # Step 3: Prepare the combined input for the writer agent
        input_for_writer = (
            f"Original query: {user_query}\n"
            f"Research summary: {research_summary}\n"
            f"Analysis summary: {analysis_summary}"
        )

        # Step 4: Run the writer agent to create the final report
        writer_agent = getWriterAgent()
        writer_result = await Runner.run(writer_agent, input_for_writer, session = session)
        final_output: FinalReport = writer_result.final_output  # The final report from the writer

        # Step 5: Display the results in a nice, clear format
        print(f"""-----------------\n### 📝 **Short Summary:**
{final_output.short_summary}\n
-----------------\n### 📄 **Full Report (Markdown):**
{final_output.markdown_report}\n
-----------------\n### 🔍 **Follow-Up Questions:**
- {"\n- ".join(final_output.follow_up_questions)}  # Any extra questions the user might explore
-----------------
        """)
    except Exception as e:
        print(f"❌  {Fore.RED}ERROR ➡️ {str(e)}{Style.RESET_ALL}")

# ------------------------------------------------------------------
# Run the main function
# ------------------------------------------------------------------

if __name__ == "__main__":
    try:
        print(f""" {Fore.CYAN}
                --------------------------------------------------------------------------------------------------
                 🙋🏻‍♂️ Welcome to the Research Agent! All agents are set up! ✅ 
                --------------------------------------------------------------------------------------------------{Style.RESET_ALL}
            """)
        while True:
            user_query = input(f"{Fore.YELLOW}Enter your research query (or type 'exit' to quit): {Style.RESET_ALL}")
            if user_query.lower() == "exit":
                print(f"{Fore.CYAN}Exiting the Research Agent ➡️  Clearing session memory ➡️  Goodbye! 👋{Style.RESET_ALL}")
                break
            if not user_query.strip():
                print(f"{Fore.RED}Please enter a valid query. ❌{Style.RESET_ALL}")
                continue

            asyncio.run(main(user_query))
    except Exception as e:
        print(f"❌  {Fore.RED}ERROR ➡️ {str(e)}{Style.RESET_ALL}")