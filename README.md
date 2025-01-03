# DeepSeek API Library

![Github release](https://img.shields.io/badge/release-v1.0.0-red) ![License](https://img.shields.io/badge/License-Apache--2.0-red)

![Deepseek](https://raw.githubusercontent.com/deskpai/deepseek/main/img/logo.png)

DeepSeek-V3 achieves a significant breakthrough in inference speed over previous models. It tops the leaderboard among open-source models and rivals the most advanced closed-source models globally at the time of this writing.

This library is a thin client to communicate with the deepseek server.

## 📥 Installation

```
pip install deepseek
```

## 🥔  Preparation

- You need to have Deepseek API Key. If not, go [here](https://platform.deepseek.com/api_keys) to get one.
- Set your api key as an environment variable.

Export an environment variable on macOS or Linux systems:
```
export DEEPSEEK_API_KEY=<YOUR_API_KEY>
```

Export an environment variable in PowerShell in Windows
```
setx DEEPSEEK_API_KEY <YOUR_API_KEY>
```

## 💎 Usage

```
from deepseek import DeepSeekAPI
api_client = DeepSeekAPI()
```

- Get your account balance

```
api_client.user_balance()
```

- Chat (with streaming off)

```Python
r = api_client.chat_completion(prompt='Hi')
print(r)
```

- Chat (with streaming on)

```Python
for chunk in api_client.chat_completion(prompt='Hi', stream=True):
    print(chunk, end='', flush=True)
```

- Fill-In-the-Middle (with streaming off)

```Python
r = api_client.fim_completion(prompt='Hi', max_tokens=64)
print(r)
```

- Fill-In-the-Middle (with streaming on)

```
for chunk in api_client.fim_completion(prompt='Once upon a time, ', stream=True):
    print(chunk, end='', flush=True)
```


> Maintained by [deskpai.com](https://deskpai.com) 2025, Contact: [dev@deskpai.com](mailto:dev@deskpai.com)

