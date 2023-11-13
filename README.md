# url-shortner
url-shortner coding challenge

design -    
- 2 apis
    - create shortlink
    - redirect shortlink

- create shortlink (url): 
    - shorturl = someHash(url)
    - db.save (primaryKey: shorturl, realUrl: url)
    - return shorturl

- redirect shortlink (shortlink):
    - realurl = db.query(shortlink)
    - return response(realurl)

- language: python
- framework: flask
- dbms: MongoDB (pyMongo)

dbms record:    
```
{          
    longUrl: "www.amazon.com",          
    shortUrl: "s0m3hAsHsTr1Ng"  
}
```

