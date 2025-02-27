import json
import requests


# http://localhost:3001/api/models

def google_search(query: str):
    """
    Search Google using a query.

    Args:
        query (str): The search query.

    Returns:
        str: A concatenated list of the top search results.
    """
    api_url = "http://localhost:3001/api/search"

    headers = {"Content-Type": "application/json"}
    data = json.dumps(
        {
            "chatModel": {"provider": "groq", "model": "llama3-70b-8192"},
            "embeddingModel": {
                "provider": "local",
                "model": "xenova-bge-small-en-v1.5",
            },
            "optimizationMode": "balanced",
            "focusMode": "webSearch",
            "query": query,
            "history": [],
        }
    )

    response = requests.post(api_url, headers=headers, data=data)
    result = response.json()

    return result["message"]


print(google_search("I remember reading an article 2 months ago about this young stanford guy named Pranav with a startup that raised some millions of dollars about some kind of finance related stuff."))