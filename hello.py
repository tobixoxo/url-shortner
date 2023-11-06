from flask import Flask, jsonify, request, redirect
import json

app = Flask(__name__)

if __name__ == "__main__": 
    app.run(debug=True)

def shortenUrl(longUrl):
    return "xyz123"

@app.route('/')
def home():
    return "hello World"

db = {}

@app.route('/shorten/')
def shorten():
    # take the url
    longUrl = request.args.get('url')
    # pass it through some shortening service
    shortUrl = shortenUrl(longUrl)
    # save the new url against long url in db
    db[shortUrl] = longUrl
    # return response from new url
    return json.dumps({"shortUrl":f"{shortUrl}"})


@app.route('/<shortUrl>')
def extractUrl(shortUrl):
    #query the long url from database
    if(shortUrl in db.keys()):
        longUrl = db[shortUrl]
        return redirect("https://" + longUrl)
    else:
        return "invalid url"