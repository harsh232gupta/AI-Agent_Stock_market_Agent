import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file
GEMINI_API_KEY = "AIzaSyC7C-pQ1qF-ET_TLdYoJIRmWVkgE9vWGPs"


# Initialize Gemini Client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_stock_price(ticker: str, price: float):
    prompt = f"Analyze the stock price of {ticker}, currently at ${price}. Provide a buy/sell/hold recommendation with reasoning."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in analysis: {str(e)}"

# Example Usage
# if __name__ == "__main__":
#     ticker = "AAPL"
#     price = 175.50
#     print(analyze_stock_price(ticker, price))
