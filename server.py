from flask import Flask, render_template, jsonify, request, send_from_directory
from random import *
from threading import Thread
from flask_cors import CORS
from wattpad2epub import get_book
import time
import os
import platform

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

def cleanupFiles():
  while (1 == 1):
    current_time = time.time()
    for f in os.listdir("./books"):
      creation_time = os.path.getctime(os.path.join("./books", f))
      if (current_time - 7 * 24 * 60 * 60 > creation_time):
        os.unlink(os.path.join("./books", f))
        print('{} removed'.format(f))
    time.sleep(10)

app = Flask(__name__,
            static_folder = "./dist/",
            template_folder = "./dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory('./', filename)

@app.route('/api', methods=["POST"])
def random_number():
    return get_book(request.get_json()["url"])

@app.route('/')
def catch_all():
    return render_template("index.html")

cleanup = Thread(target=cleanupFiles)
cleanup.start()
