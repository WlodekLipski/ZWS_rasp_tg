from flask import Flask, render_template
from concurrent.futures import ThreadPoolExecutor
import time

executor = ThreadPoolExecutor(2)

app = Flask(__name__, static_url_path="")


@app.route('/')
def mainpage():
    data = readfile("static/exampleData.csv")
    return render_template("index.html", data=data)


def readfile(path):
    data = []
    f = open(path, "r")
    line = f.readline()
    line = line.strip('\n')
    while line:
        arr = [line]
        data.append(arr)
        line = f.readline()
        line = line.strip('\n')
    if line:
        arr = [line]
        data.append(arr)
    print(data)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
