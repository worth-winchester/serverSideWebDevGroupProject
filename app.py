import requests
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movieTitle")
def movieTitle():
    return render_template("searchByTitle.html")

@app.route("/movieID")
def movieID():
    return render_template("searchByID.html")

# @app.route("/movieTitle", methods=['GET', 'POST'])
# def getTitle():
#     if request.method == 'POST':
#         if request.form["movieTitle"] != "":
#             title = request.form["movieTitle"]
#             requestUrl = "http://www.omdbapi.com/?apikey=a514574c&t=" + title
#             apiResponse = requests.get(requestUrl)
#             responseJson = apiResponse.json()
#             responseText = apiResponse.text
#             with open("test.txt", "w") as f:
#                 f.write(responseText)
#             return render_template("searchByTitle.html", movieData=responseJson)

@app.route("/movieTitle", methods=['GET', 'POST'])
def getTitle():
    if request.method == 'POST':
        if request.form["movieTitle"] != "":
            title = request.form["movieTitle"]
            requestUrl = "http://www.omdbapi.com/?apikey=a514574c&t=" + title
            apiResponse = requests.get(requestUrl)
            responseJson = apiResponse.json()
            responseText = apiResponse.text
            test = responseJson["Title"]
            with open("test.txt", "w") as f:
                f.write(responseText)
            return render_template("searchByTitle.html", movieData=test)

@app.route("/movieID", methods=['GET', 'POST'])
def getID():
    if request.method == 'POST':
        if request.form["movieID"] != "":
            imdbID = request.form["movieID"]
            requestUrl = "http://www.omdbapi.com/?apikey=a514574c&i=" + imdbID
            apiResponse = requests.get(requestUrl)
            responseJson = apiResponse.json()
            responseText = apiResponse.text
            with open("test.txt", "w") as f:
                f.write(responseText)
            return render_template("searchByID.html", movieData=responseJson)

if __name__ == "__main__":
    app.run(debug=True)