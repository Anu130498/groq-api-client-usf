import requests

# Groq API endpoint and your API key
GROQ_API_URL = "https://api.groq.com/v1/ask"  # Adjust if your endpoint differs.
API_KEY = "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"

def ask_groq_api(question):
    """
    Sends the question to the Groq API and returns the answer.
    """
    payload = {"question": question}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Assuming the API returns the answer in a field named "answer"
        return data.get("answer", "No answer found in the response.")
    except requests.RequestException as e:
        return f"Request error: {e}"
    except ValueError:
        return "Error decoding JSON response from the API."

def main():
    print("Welcome to the Groq API Q&A tool!")
    print("Type 'quit' to exit.\n")
    
    while True:
        question = input("Enter your question: ").strip()
        if question.lower() == "quit":
            print("Exiting... Goodbye!")
            break
        if not question:
            print("Please enter a valid question.\n")
            continue

        answer = ask_groq_api(question)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
