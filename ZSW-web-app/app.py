from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread
import time

async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        async_mode = 'threading'

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()


app = Flask(__name__, static_url_path="")
socketio = SocketIO(app, async_mode=async_mode)
thread = None

@app.route('/')
def mainpage():
    global thread
    if thread is None:
        thread = Thread(target=readfile, args=("static/exampleData.csv",))
        thread.daemon = True
        thread.start()
    return render_template("index.html", data=[])

def readfile(path):
    print("STAART")
    while True:
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
        socketio.emit('modified', )
        time.sleep(5)

def printSmth():
    print("TROLOLO")



if __name__ == '__main__':
    socketio.run(app, debug=True)
