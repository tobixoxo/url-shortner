from flask import Flask, jsonify, request, redirect
from pymongo import MongoClient
import hashlib
import json

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.flask_db
urls = db.urls


if __name__ == "__main__": 
    app.run(debug=True)

def shortenUrl(longUrl):
    return "xyz123"

@app.route('/')
def home():
    return "hello World"

@app.route('/shorten/')
def shorten():
    # take the url
    longUrl = request.args.get('url')
    # pass it through some shortening service
    shortUrl = shortenUrl(longUrl)
    # save the new url against long url in db
    urls.insert_one({shortUrl: longUrl })
    # return response from new url
    return json.dumps({"shortUrl":f"{shortUrl}"})


@app.route('/<shortUrl>')
def extractUrl(shortUrl):
    #query the long url db from database
    record = urls.find_one({shortUrl: {'$exists': True}}) 
    if(record is not None):
        print(record)
        longUrl = record[shortUrl]
        return redirect("https://" + longUrl)
    else:
        return "invalid url"