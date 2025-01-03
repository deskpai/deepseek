import json
import requests
from deepseek.const import *


class DeepSeekAPI:
    def __init__(self, api_key=DEEPSEEK_API_KEY):
        if api_key is None:
            raise ValueError("DEEPSEEK_API_KEY is missing")
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }


    def user_balance(self):
        response = requests.get(API_USER_BAL, headers=self.headers)
        return response.json()

    def _post_request(self, api_url, payload, stream):
        response = requests.post(api_url, headers=self.headers, data=json.dumps(payload), stream=stream)
        if response.status_code >= 300:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        return response

    def completion_impl(self, response, type_='chat'):
        for line in response.iter_lines():
            if line:  # Process non-empty lines
                # Remove 'data: ' prefix if present
                line = line.decode('utf-8').strip()
                if line.startswith('data: '):
                    line = line[6:].strip()
                # Skip empty or invalid lines
                if not line or line == '[DONE]':
                    break
                # Parse valid JSON
                decoded_line = json.loads(line)
                if 'choices' in decoded_line:
                    finish_reason = decoded_line['choices'][0].get('finish_reason', None)
                    if type_ == 'chat':
                        delta_content = decoded_line['choices'][0].get('delta', {}).get('content', '')
                    elif type_ == 'fim':
                        delta_content = decoded_line['choices'][0].get('text', '')
                    if delta_content:
                        yield delta_content
                    if finish_reason == 'stop':
                        break

    def chat_completion(self, prompt=DEFAULT_USR_PROM, prompt_sys=DEFAULT_SYS_PROM, stream=False, model='deepseek-chat',
                        **kwargs):
        payload = {"model": model, "frequency_penalty": 0, "max_tokens": 2048, "presence_penalty": 0,
                   "response_format": {"type": "text"}, "stop": None, "stream": stream, "stream_options": None,
                   "temperature": 1, "top_p": 1, "tools": None, "tool_choice": "none", "logprobs": False,
                   "top_logprobs": None, 'messages': [
                {"content": prompt_sys, "role": "system"},
                {"content": prompt, "role": "user"}
            ] if isinstance(prompt, str) else prompt}
        payload.update(kwargs)

        response = self._post_request(API_CHAT_COM, payload, stream)
        return self.completion_impl(response, 'chat') if stream else \
            response.json()['choices'][0].get('message', {}).get('content', '')

    def fim_completion(self, prompt=DEFAULT_USR_PROM, stream=False, model='deepseek-chat', **kwargs):
        payload = {
            "model": model,
            "prompt": prompt,
            "echo": False,
            "frequency_penalty": 0,
            "logprobs": 0,
            "max_tokens": 1024,
            "presence_penalty": 0,
            "stop": None,
            "stream": stream,
            "stream_options": None,
            "suffix": None,
            "temperature": 1,
            "top_p": 1
        }

        payload.update(kwargs)
        response = self._post_request(API_CHAT_FIM, payload, stream)
        return self.completion_impl(response, 'fim') if stream else \
            response.json()['choices'][0].get('text', '')

    def get_models(self):
        response = requests.get(API_CHAT_MOD, headers=self.headers)
        r = response.json()
        models = []
        for i in r['data']:
            models.append(i['id'])
        return models
