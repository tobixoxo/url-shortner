from flask import Flask, jsonify, request, redirect
from pymongo import MongoClient
import hashlib
import json
import base62

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.flask_db
urls = db.urls


if __name__ == "__main__": 
    app.run(debug=True)

def shortenUrl(url):
    # Generate a unique hash using SHA-256
    sha256_hash = hashlib.sha256(url.encode()).digest()

    hash_bytes = sha256_hash[:8]

    # Encode the hash in base62
    short_hash = base62.encodebytes(hash_bytes)

    return short_hash

@app.route('/')
def home():
    return "Shorten your URL!"

@app.route('/shorten/')
def shorten():
    # take the url
    longUrl = request.args.get('url')
    # check if longUrl already exists
    record = urls.find_one({"longUrl":longUrl})
    shortUrl = ""
    if record is None:
        # pass it through some shortening service
        shortUrl = shortenUrl(longUrl)
        # save the new url against long url in db
        urls.insert_one({"longUrl": longUrl, "shortUrl": shortUrl })
        # return response from new url
    else :
        shortUrl = record["shortUrl"]
    return json.dumps({"shortUrl":f"{shortUrl}"})


@app.route('/<shortUrl>')
def extractUrl(shortUrl):
    #query the long url db from database
    record = urls.find_one({"shortUrl": shortUrl}) 
    if(record is not None):
        print(record)
        longUrl = record["longUrl"]
        return redirect("https://" + longUrl)
    else:
        return "invalid url"
    
@app.route('/deleteUrl/', methods=['DELETE'])
def deleteUrl():
    shortUrl = request.args.get('url')
    # check if longUrl already exists
    try:
        result = urls.delete_one({"shortUrl": shortUrl})
        print(f"Delete result: {result}")
        return "Url Deleted!"
    except Exception as e:
        print(f"Error deleting URL: {e}")
        return "Error deleting URL", 500  # Return a 500 Internal Server Error status code