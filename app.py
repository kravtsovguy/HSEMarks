# -*- coding: utf-8 -*-

from flask import *
import os

app = Flask(__name__)
#app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    #return render_template("index.html")
    return app.send_static_file("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)