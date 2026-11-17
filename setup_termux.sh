#!/data/data/com.termux/files/usr/bin/bash
# One-shot phone setup (Termux). Run: bash phone/setup_termux.sh
set -e
pkg update -y && pkg install -y python git
pip install --no-deps -e . 2>/dev/null || true
pip install httpx click rich tomlkit croniter psutil requests
read -r -p "Paste your Groq API key (gsk_...): " KEY
grep -q GROQ_API_KEY ~/.bashrc 2>/dev/null || echo "export GROQ_API_KEY=$KEY" >> ~/.bashrc
export GROQ_API_KEY=$KEY
echo "Done. Restart Termux, then: python phone/groq_chat.py"
