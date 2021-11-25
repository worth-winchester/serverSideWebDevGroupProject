import requests
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/movie", methods=['GET', 'POST'])
def movie():
    title = request.args.get("title")
    if title != None:
        requestUrl = "http://www.omdbapi.com/?apikey=a514574c&t=" + title
        apiResponse = requests.get(requestUrl)
        responseJson = apiResponse.json()
        responseText = apiResponse.text
        with open("test.txt", "w") as f:
            f.write(responseText)
    #return redirect("/", movieData=movieJson)
    return render_template("index2.html", movieData=responseJson)  

if __name__ == "__main__":
    app.run(debug=True)