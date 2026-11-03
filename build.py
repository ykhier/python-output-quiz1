"""Run all questions, verify the answers, and rebuild index.html."""
import subprocess, sys
subprocess.run([sys.executable, "questions.py"], check=True)
data = open("questions.json", encoding="utf-8").read().replace("</", "<\\/")
page = open("template.html", encoding="utf-8").read().replace("__DATA__", data)
html = (
    '<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    '</head>\n<body>\n' + page + '\n</body>\n</html>\n'
)
open("index.html", "w", encoding="utf-8").write(html)
print("index.html rebuilt")
