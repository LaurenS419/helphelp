from openai import OpenAI
import sys


PROMPT = "Given the following question and response, in 100 words or less what are the ways the response can be improved in terms of confidence, clarity, and professionalism."


def get_key():
    file = open("openai-key.txt", "r")
    key = file.read()
    file.close()
    return key


def get_feedback(question, response):
    client = OpenAI(api_key=get_key())


    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": PROMPT + " " + question + " " + response
        }
        ]
    )

    phrase = completion.choices[0].message
    return phrase