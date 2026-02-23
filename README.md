
# 🤖 Multi-Agent Report Generator

A powerful multi-agent AI system that researches, analyzes, and generates comprehensive reports using OpenAI's GPT models and Tavily search API.

## ✨ Features

- 🔍 **Researcher Agent**: Searches the web using Tavily API for relevant information
- 📊 **Analyst Agent**: Extracts key trends, risks, and insights from research findings
- ✍️ **Writer Agent**: Synthesizes information into professional markdown reports
- 📋 **Structured Output**: Generates executive summaries, detailed reports, and follow-up questions
- 💾 **Session Persistence**: Uses SQLite to maintain conversation history

## 🏗️ Project Architecture

```
User Query
    ↓
[Researcher Agent] → Searches & summarizes findings
    ↓
[Analyst Agent] → Identifies trends & insights
    ↓
[Writer Agent] → Creates final report
    ↓
Executive Summary + Detailed Report + Follow-up Questions
```

## 📋 Prerequisites

- Python 3.12+
- Conda
- OpenAI API Key
- Tavily API Key

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/iyash1/multiagent-report-gen.git
cd multiagent-report-gen
```

### 2️⃣ Create Conda Environment
```bash
conda create -n report-gen python=3.12
conda activate report-gen
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5️⃣ Run the Application
```bash
python app.py
```

## 📖 Usage

```
Enter your research query: What are the latest trends in AI?
```

The system will:
1. Research the topic using Tavily
2. Analyze findings for key insights
3. Generate a professional report with markdown formatting

## 📦 Dependencies

- `openai-agents==0.2.2` - Multi-agent framework
- `python-dotenv` - Environment variable management
- `langchain-openai==0.2.1` - LangChain OpenAI integration
- `pydantic` - Data validation
- `colorama` - Colored terminal output

## 🔧 Configuration

All agent models use `gpt-4.1-mini`. To change models, edit the `GPT_MODEL_4` constant in `constants.py`.

## 📂 Project Structure

```
multiagent-report-gen/
├── app.py                 # Main application orchestrator
├── researchAgent.py       # Researcher agent with Tavily search
├── analystAgent.py        # Analyst agent for trend analysis
├── writerAgent.py         # Writer agent for report generation
├── agents.py              # Agent framework and utilities
├── dataModels.py          # Pydantic models for data validation
├── constants.py           # Configuration constants
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
└── README.md              # This file
```

## ⚠️ Important Security Notes

⚠️ **Never commit `.env` file to version control!**
- Add `.env` to `.gitignore`
- Keep API keys confidential

## 🆘 Troubleshooting

- **API Key Error**: Verify `.env` file exists and keys are valid
- **Missing Dependencies**: Run `pip install -r requirements.txt`
- **Conda Not Found**: Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

## 📝 License

MIT License

