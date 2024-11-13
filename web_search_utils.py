import requests
import time


def web_search(query):
    """Perform a web search for the given query using SerpAPI"""
    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": "ENTER-YOUR-SERPAPI=KEY"}
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.ConnectTimeout:
            print(f"Timeout occurred, retrying... ({attempt + 1}/{max_retries})")
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    return None
