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

@app.route("/movieTitle", methods=['GET', 'POST'])
def getTitle():
    if request.method == 'POST':
        if request.form["movieTitle"] != "":
            search = request.form["movieTitle"]
            requestUrl = "http://www.omdbapi.com/?apikey=a514574c&t=" + search
            apiResponse = requests.get(requestUrl)
            responseJson = apiResponse.json()
            responseText = apiResponse.text
            title = "Title: " + responseJson["Title"]
            posterUrl = responseJson["Poster"]
            posterText = "View Movie Poster"
            year = "Year: " + responseJson["Year"]
            rated = "Rated: " + responseJson["Rated"]
            runtime = "Runtime: " + responseJson["Runtime"]
            genre = "Genre: " + responseJson["Genre"]
            director = "Director: " + responseJson["Director"]
            writer = "Writer: " + responseJson["Writer"]
            actors = "Actors: " + responseJson["Actors"]
            plot = "Plot: " + responseJson["Plot"]
            awards = "Awards: " + responseJson["Awards"]
            metascore = "Metascore: " + responseJson["Metascore"]
            imdbRating = "IMDB Rating: " + responseJson["imdbRating"]
            imdbVotes = "IMDB Votes: " + responseJson["imdbVotes"]
            imdbID = "IMDB ID: " + responseJson["imdbID"]
            boxOffice = "BoxOffice: " + responseJson["BoxOffice"]
            with open("test.txt", "w") as f:
                f.write(responseText)
            return render_template("searchByTitle.html", dataTitle=title, dataPosterUrl=posterUrl, dataYear=year, dataRated=rated, dataRuntime=runtime, dataGenre=genre, dataDirector=director, dataWriter=writer, dataActors=actors, dataPlot=plot, dataAwards=awards, dataMetascore=metascore, dataImdbRating=imdbRating, dataImdbVotes=imdbVotes, dataImdbID=imdbID, dataBoxOffice=boxOffice, dataPosterText=posterText)

@app.route("/movieID", methods=['GET', 'POST'])
def getID():
    if request.method == 'POST':
        if request.form["movieID"] != "":
            search = request.form["movieID"]
            requestUrl = "http://www.omdbapi.com/?apikey=a514574c&i=" + search
            apiResponse = requests.get(requestUrl)
            responseJson = apiResponse.json()
            responseText = apiResponse.text
            title = "Title: " + responseJson["Title"]
            posterUrl = responseJson["Poster"]
            posterText = "View Movie Poster"
            year = "Year: " + responseJson["Year"]
            rated = "Rated: " + responseJson["Rated"]
            runtime = "Runtime: " + responseJson["Runtime"]
            genre = "Genre: " + responseJson["Genre"]
            director = "Director: " + responseJson["Director"]
            writer = "Writer: " + responseJson["Writer"]
            actors = "Actors: " + responseJson["Actors"]
            plot = "Plot: " + responseJson["Plot"]
            awards = "Awards: " + responseJson["Awards"]
            metascore = "Metascore: " + responseJson["Metascore"]
            imdbRating = "IMDB Rating: " + responseJson["imdbRating"]
            imdbVotes = "IMDB Votes: " + responseJson["imdbVotes"]
            imdbID = "IMDB ID: " + responseJson["imdbID"]
            boxOffice = "BoxOffice: " + responseJson["BoxOffice"]
            with open("test.txt", "w") as f:
                f.write(responseText)
            return render_template("searchByTitle.html", dataTitle=title, dataPosterUrl=posterUrl, dataYear=year, dataRated=rated, dataRuntime=runtime, dataGenre=genre, dataDirector=director, dataWriter=writer, dataActors=actors, dataPlot=plot, dataAwards=awards, dataMetascore=metascore, dataImdbRating=imdbRating, dataImdbVotes=imdbVotes, dataImdbID=imdbID, dataBoxOffice=boxOffice, dataPosterText=posterText)
            with open("test.txt", "w") as f:
                f.write(responseText)
            return render_template("searchByID.html", movieData=responseJson)

if __name__ == "__main__":
    app.run(debug=True)