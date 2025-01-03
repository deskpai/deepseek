# DeepSeek API Library

![Github release](https://img.shields.io/badge/release-v1.0.0-red) ![License](https://img.shields.io/badge/License-Apache--2.0-red)

![Deepseek](https://raw.githubusercontent.com/deskpai/deepseek/main/img/logo.png)

DeepSeek-V3 delivers groundbreaking improvements in inference speed compared to earlier models. It leads the performance charts among open-source models and competes closely with the most advanced proprietary models available globally.

This Python library provides a lightweight client for seamless communication with the DeepSeek server.

For deepseek GUI support, welcome to check out [DeskPai](https://github.com/deskpai/deskpai/tree/main/src#llmimage-chat).

---

## 📥 Installation

```bash
pip install deepseek
```

---

## 🥔 Preparation - DEEPSEEK_API_KEY

You need to obtain a DeepSeek API Key. If you don't have one, visit [here](https://platform.deepseek.com/api_keys) to generate it.

You can configure your API key as an environment variable.

### On macOS or Linux:
```bash
export DEEPSEEK_API_KEY=<YOUR_API_KEY>
```

### On Windows (PowerShell):
```powershell
setx DEEPSEEK_API_KEY <YOUR_API_KEY>
```

If DEEPSEEK_API_KEY is not set, you need to manually pass api_key in code `DeepSeekAPI(api_key)`.

---

## 💎 Usage

- [Video Demo 1](https://cms.deskpai.com/view?m=l9tcCdrZA)

### Initialize the API Client
```python
from deepseek import DeepSeekAPI
api_client = DeepSeekAPI()
```

### Retrieve Account Balance
```python
api_client.user_balance()
```

### List Available Models
```python
api_client.get_models()
```

### Chat (Streaming Disabled)
```python
response = api_client.chat_completion(prompt='Hi')
print(response)
```

### Chat (Streaming Enabled)
```python
for chunk in api_client.chat_completion(prompt='Hi', stream=True):
    print(chunk, end='', flush=True)
```

### Chat (Multi-turn Mode)

For multi-turn mode, you need to construct prompt as a list with chat history. An example is as below:

```python
prompt = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is the capital of China?"},
    {"role": "assistant", "content": "The capital of China is Beijing."},
    {"role": "user", "content": "What is the capital of the United States?"}
]
for chunk in api_client.chat_completion(prompt=prompt, stream=True):
    print(chunk, end='', flush=True)
```

[This](https://github.com/deskpai/deskpai/tree/main/src#multiturn-chat) is another multi-turn chat example in [Deskpai Image Chat](https://github.com/deskpai/deskpai/tree/main/src#llmimage-chat).

### Fill-In-the-Middle (Streaming Disabled)
```python
response = api_client.fim_completion(prompt='Hi', max_tokens=64)
print(response)
```

### Fill-In-the-Middle (Streaming Enabled)
```python
for chunk in api_client.fim_completion(prompt='Once upon a time, ', stream=True):
    print(chunk, end='', flush=True)
```

### Customized Model Inference Parameters
```python
use_case = 'Creative Writing'
kwargs = {'max_tokens': 7680, 'temperature': TEMPERATURE_MAP[use_case]}
api_client.chat_completion(prompt='Hi', **kwargs)
```

---

## 🔗 Contact

> Maintained by [deskpai.com](https://deskpai.com) 2025  
> Contact: [dev@deskpai.com](mailto:dev@deskpai.com)

