from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://media2.giphy.com/media/czpet1H4pnyAE/giphy.gif?cid=ecf05e47yigvxle31tfu3twdv9vf8nrq2429z9v7gr4t67gm&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/wTrXRamYhQzsY/200w.webp?cid=ecf05e47yigvxle31tfu3twdv9vf8nrq2429z9v7gr4t67gm&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/pCyN4mn4MbGCY/200.webp?cid=ecf05e47yigvxle31tfu3twdv9vf8nrq2429z9v7gr4t67gm&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/eYM0ad6oiKioU/200w.webp?cid=ecf05e472c69qab9pincy3lzipb41vbs2jittw1ocw7sim0y&rid=200w.webp&ct=g",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
