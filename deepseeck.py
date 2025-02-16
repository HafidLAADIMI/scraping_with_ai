import requests

# DeepSeek API endpoint and API key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "sk-59ef4f46a8744378bda7210fe0fc0e10"


def call_deep_seek(dom_content, parse_description):
    template = (
        f"Extract specific information from the following text: ```{dom_content}```. Your task is to extract only the information that directly matches this description: ```{parse_description}```. Do not include any additional text, comments, or explanations in your response. If no information matches the description, return an empty string (`''`). Your output must contain only the extracted data, with no extra text or formatting."
    )
    payload = {
        "model": "deepseek-chat",  # Specifying the model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": template}  # the tamplate goes here
        ]
    }
    # Making a POST request to the DeepSeek API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)

    # Checking the response
    if response.status_code == 200:
        result = response.json()
        print("DeepSeek API Response:", result)
        return result
    else:
        print("Failed to call DeepSeek API:",
              response.status_code, response.text)
        return response.text
