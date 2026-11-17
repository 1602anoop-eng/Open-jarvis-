#!/usr/bin/env python3
"""Minimal Groq chat for phones (Termux/Pydroid). Usage:
    export GROQ_API_KEY=gsk_xxx
    python phone/groq_chat.py "Hello!"        # one-shot
    python phone/groq_chat.py                 # interactive
Needs only: pip install httpx
"""
import os, sys, httpx

URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

def ask(history):
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        sys.exit("Set GROQ_API_KEY first: export GROQ_API_KEY=gsk_...")
    r = httpx.post(URL, headers={"Authorization": f"Bearer {key}"},
                   json={"model": MODEL, "messages": history}, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def main():
    history = [{"role": "system", "content": "You are Jarvis, a concise assistant."}]
    if len(sys.argv) > 1:
        history.append({"role": "user", "content": " ".join(sys.argv[1:])})
        print(ask(history)); return
    while True:
        try: q = input("you> ").strip()
        except (EOFError, KeyboardInterrupt): break
        if not q: continue
        history.append({"role": "user", "content": q})
        a = ask(history); history.append({"role": "assistant", "content": a})
        print("jarvis>", a)

if __name__ == "__main__":
    main()
