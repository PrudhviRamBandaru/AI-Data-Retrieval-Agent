import google.generativeai as genai
import re

API_KEY = "ENTER-YOUR-API-KEY"
genai.configure(api_key=API_KEY)


def call_gemini_api(prompt):
    """Call the Gemini API to process the query and get results"""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def clean_text(text):
    """Clean the response text by removing unwanted characters"""
    cleaned_text = re.sub(r"[*#_]+", "", text)  # Remove certain special characters
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Clean up whitespace
    return cleaned_text


def process_data_with_gemini(results, user_query):
    """Process the search results using the Gemini API and extract relevant info"""
    processed_results = []

    for item in results:
        entity = item["entity"]
        try:
            query = user_query.format(entity=entity)
            response_text = call_gemini_api(query)
            cleaned_text = clean_text(response_text)
            processed_results.append({"entity": entity, "extracted_info": cleaned_text})
        except Exception as e:
            processed_results.append({"entity": entity, "extracted_info": f"Error: {str(e)}"})

    return processed_results
