# OpenJarvis — Phone Edition (Groq)

Lightweight build (<25 MB): no desktop binaries, tests, docs, or Rust.
Runs on Android via Termux; inference happens on Groq's cloud, so no GPU/RAM needed.

1. Get a free key: https://console.groq.com/keys
2. In Termux: `bash phone/setup_termux.sh`
3. Quick chat: `python phone/groq_chat.py "hi"`
4. Full framework: `mkdir -p ~/.openjarvis && cp phone/config.toml ~/.openjarvis/ && jarvis`

Python use:
```python
from openjarvis.engine.groq import GroqEngine
from openjarvis.core.types import Message, Role
e = GroqEngine()   # reads GROQ_API_KEY
print(e.generate([Message(role=Role.USER, content="Hi")], model="llama-3.3-70b-versatile"))
```
Never commit your key; keep it in the env var.
