import webbrowser

f = open('python_html.html','wb')

message = """<html>
<body>
<h1>
Stay tuned for our amazing summer sale!
</h1>
</body>
</html>"""

f.write(message.encode())
f.close()

webbrowser.open_new_tab('python_html.html')
