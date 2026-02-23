from pydantic import BaseModel
from typing_extensions import TypedDict

class TavilySearchParams(TypedDict):
    query: str
    max_results: int

class AnalysisSummary(BaseModel):
    summary: str

class FinalReport(BaseModel):
    short_summary: str  # A brief 2–3 sentence executive summary
    markdown_report: str    # A detailed report in Markdown format (at least 500 words)
    follow_up_questions: list[str]    # A list of 3–5 suggested follow-up research questions
