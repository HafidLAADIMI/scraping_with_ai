import requests

# DeepSeek API endpoint and API key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "sk-59ef4f46a8744378bda7210fe0fc0e10"


# Example data scraped from the website
def call_deep_seek(dom_content, parse_description):
    template = (
        f"You are tasked with extracting specific information from the following text content: {dom_content}. "
        "Please follow these instructions carefully: \n\n"
        f"1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
        "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
        "3. **Empty Response:** If no information matches the description, return an empty string ('')."
        "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    )
    payload = {
        "model": "deepseek-chat",  # Specify the model (check documentation)
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": template}  # Your template goes here
        ]
    }
    # Make a POST request to the DeepSeek API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)

    # Check the response
    if response.status_code == 200:
        result = response.json()
        print("DeepSeek API Response:", result)
        return result
    else:
        print("Failed to call DeepSeek API:", response.status_code, response.text)
        return response.text
