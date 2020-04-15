![alt text](./public/logo.png "Wutpad logo")

![Vue CI](https://github.com/divy-work/wattpad-downloader/workflows/Vue%20CI/badge.svg)
![Heroku](https://heroku-badge.herokuapp.com/?app=wutpad)

Wattpad2Epub downloads and converts Wattpad books into Epub files you can use
with your favorite ebook reader.

## Features

* Multilingual source code as an example to young developers.
* Vue frontend with Python3 Flask backend.
* Multithreading for better performance.
* Automatically deletes files older than 7 days.

## Why use this?
Wattpad doesn't offer an option to download a book. This forces you to remain
online while reading, and use wattpad's application to access the stories.

Having those stories in epub format allows storing them as a backup, offline
reading and self publication.

## Requirements

These are the bare minimum requirements for hosting this.
* Python3 - you know what's this ;) - A general-purpose programming language
* Node.js - cmon don't know this? - Javascript runtime
* NPM - Node's packagae manager (inbuilt)
* PIP - Python's package manager

## Installing

```bash
$ git clone https://github.com/divy-work/wattpad-downloader
$ cd wattpad-downloader
$ npm install
$ pip install -r requirements.txt

# Now, we build the Vue frontend
$ npm run build

# Finally, let's start the server
$ FLASK_APP=server.py python3 server.py
```
