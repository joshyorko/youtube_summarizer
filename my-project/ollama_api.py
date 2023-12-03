"""
Calls the Ollama API to generate a completion using the specified model and prompt.

"""

import json
import requests


class OllamaAPI:
    def __init__(self):
        """
        Initializes the API client for the OnlyLlama service.

        The API client is responsible for making requests to the OnlyLlama API.

        Args:
            None

        Returns:
            None
        """

        self.url = "http://localhost:11434/api/generate"
        self.headers = {"Content-Type": "application/json"}

    def generate_completion(self, model, prompt):
        """
        Generates a completion using the specified model and prompt.

        Args:
            model (str): The model to use for completion.
            prompt (str): The prompt for completion.

        Returns:
            str: The generated completion response.
        """
        payload = {"model": model, "prompt": prompt}
        response = requests.post(
            self.url,
            data=json.dumps(payload),
            headers=self.headers,
            stream=True,
            timeout=10,
        )
        response_parts = []
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                response_json = json.loads(decoded_line)
                if "response" in response_json:
                    response_parts.append(response_json["response"])
        response_text = "".join(response_parts)
        return response_text

    def process_prompt(self, user_model_key, user_prompt):
        """
        Process the user prompt by generating a completion using the selected model.

        Args:
            user_model_key (str): The key of the user-selected model.
            user_prompt (str): The user prompt to generate the completion.

        Returns:
            None
        """
        # Now use the user selected model to generate the completion
        completion = self.generate_completion(user_model_key, user_prompt)
        print(completion)
        with open("completion.md", "w", encoding="utf-8") as f:
            f.write(completion)

        return completion


if __name__ == "__main__":
    # Initialize the API client
    ollama_api = OllamaAPI()
    USER_PROMPT = input("Enter prompt: ")
    ollama_api.process_prompt("mistral", USER_PROMPT)
