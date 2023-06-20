from django.conf import settings
from time import sleep
import requests
import json


def get_ai_answer_via_request(prompt, number_of_tokens=128):
    api_key = settings.OPENAI_KEY

    url = "https://api.openai.com/v1/completions"

    payload = json.dumps({
                "model":"text-davinci-003",
                "prompt":str(prompt),
                "temperature":0.7,
                "max_tokens":int(number_of_tokens),
                "top_p":1,
                "frequency_penalty":0,
                "presence_penalty":0
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
    }

    generated = False
    while not generated:
        try:
            response = requests.request("POST", url, headers=headers, data=payload).json()
            print(response)
            generated = True
        except Exception as e:
            print(f"Exception occured : {e}")
            sleep(0.5)

    output = {}
    output["text"] = response["choices"][0]["text"]
    output["id"] = response["id"]
    output["model"] = response["model"]
    output["object"] = response["object"]
    output["completion_tokens"] = response["usage"]["completion_tokens"]
    output["prompt_tokens"] = response["usage"]["prompt_tokens"]
    output["total_tokens"] = response["usage"]["total_tokens"]
    print(output)
    
    #Update DB
    return output["text"]