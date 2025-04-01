from openai import OpenAI
from environment.config.config import config

client = OpenAI(api_key='<KEY>')

llm_api_key = config['llm']['api_key']
llm_base_url = config['llm']['base_url']
client.api_key = llm_api_key
client.base_url = llm_base_url

def deepseek(model="deepseek-v3", system=None, user=None):
    response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ]
            )
    return response

def claude(model="claude-3-7-sonnet-20250219", system=None, user=None):
    response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ]
            )
    return response