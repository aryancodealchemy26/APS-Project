import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv("GEMINI_API_KEY")

def get_ai_advice(subject, score, category):
    # This is the EXACT URL for the stable V1 API. 
    # Notice 'v1' instead of 'v1beta'
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={my_key}"
    
    headers = {'Content-Type': 'application/json'}
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are an Expert Educational Consultant. A teacher of {subject} has an AI score of {score}/100 and is {category}. Give 3 short tips."
            }]
        }]
    }

    try:
        # We send a POST request directly to Google
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check if the response was successful
        if response.status_code == 200:
            result = response.json()
            # Navigate the JSON structure to get the text
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Server Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Network Error: {str(e)}"

# import os
# import google.generativeai as genai
# from dotenv import load_dotenv



# # 1.Load the secrets from .env
# load_dotenv()
# my_key = os.getenv("GEMINI_API_KEY")

# # # Setup the AI
# genai.configure(api_key=my_key, transport='rest')
# # model = genai.GenerativeModel(model_name='gemini-1.5-flash')
# # client = genai.Client(api_key=my_key)

# def get_ai_advice(subject, score, category):
#     # This is 'Prompt Engineering'
#     # We tell the AI exactly who it is and what to do.
#     prompt = f"""
#     You are an Expert Educational Consultant. 
#     A teacher who teaches {subject} has an AI readiness score of {score}/100 
#     and is categorized as {category}.
    
#     Give them 3 short, practical steps to improve their AI usage in their specific subject.
#     Keep it very simple and encouraging.
#     """
    
#     try:
#     # Change "gemini-2.0-flash" to "gemini-1.5-flash" 
#     # as your dashboard shows it has an active free tier limit.
#         model = genai.GenerativeModel('models/gemini-1.5-flash') 
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         # Graceful Degradation: Returning a useful error message instead of crashing
#         return f"AI Service is currently unavailable. (Reason: {e})"