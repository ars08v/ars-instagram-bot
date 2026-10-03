from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Nano Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def start_keepalive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

