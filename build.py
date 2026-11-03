"""Run all questions, verify the answers, and rebuild index.html."""
import subprocess, sys
subprocess.run([sys.executable, "questions.py"], check=True)
data = open("questions.json", encoding="utf-8").read().replace("</", "<\\/")
html = open("template.html", encoding="utf-8").read().replace("__DATA__", data)
open("index.html", "w", encoding="utf-8").write(html)
print("index.html rebuilt")
