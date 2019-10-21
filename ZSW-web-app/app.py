from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread
import time, os

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
lastModified = None

@app.route('/')
def mainpage():
    global thread
    if thread is None:
        thread = Thread(target=readfile, args=("static/exampleData.csv",))
        thread.daemon = True
        thread.start()
    return render_template("index.html", data=[])

def readfile(path):
    global lastModified
    while True:
        checkModified = os.path.getmtime(path)
        if checkModified != lastModified:
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
            socketio.emit('modified', {'data': data})
            lastModified=checkModified
        time.sleep(5)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
