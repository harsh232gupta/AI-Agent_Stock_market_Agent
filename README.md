# AI Stock Market Agent 

## Overview
This project is an AI-powered stock market agent that:
- Fetches real-time stock prices using Yahoo Finance and DuckDuckGo search.
- Provides an API to access stock prices.
- Uses AI (GPT-4) to analyze stock trends and provide Buy/Sell/Hold recommendations.

## Tech Stack
- **Python**: Backend logic
- **FastAPI**: API development
- **LangChain**: AI agent structuring
- **OpenAI API**: LLM integration
- **Yahoo Finance API / DuckDuckGo Search**: Stock price retrieval

## How to Run
### 1. Clone this Repository
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Set Up Virtual Environment
```bash
python -m venv stock_ai_env
source stock_ai_env/bin/activate  # On macOS/Linux
stock_ai_env\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a `.env` file in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the API
```bash
uvicorn main:app --reload
```

### 6. Test Endpoints
Open browser and visit:
[Swagger Docs](http://127.0.0.1:8000/docs)

## API Endpoints
- `GET /` - Check if the server is running.
- `POST /fetch_stock_price/` - Fetches stock price by ticker.
- `POST /analyze_stock/` - AI-based stock price analysis.

### Example API Request
```json
{
  "ticker": "AAPL"
}
```


---

This project provides a **fully functional AI-powered stock market analysis agent**! 🚀
