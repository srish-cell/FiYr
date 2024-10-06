
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai

genai.configure(api_key="AIzaSyDC4S2ykQO2yP62_nNe-bHiaB4gp-xA0A0")

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

)

chat_session = model.start_chat(
  history=[]
)

def analyze(output):
    
    response = chat_session.send_message(output+"\nAnalyze the given output and analysis the valuable information from this and recommandiation for the vulnerability and generate it and report it in the form of line number , vulnerbility , impact, mitigation , and recommandiation " ,safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE

    }
    )
   
    return response.text
