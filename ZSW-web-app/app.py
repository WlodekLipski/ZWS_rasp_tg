import sys
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

app = Flask(__name__, static_url_path="")
socketio = SocketIO(app, async_mode='threading')

thread = None
observer = None

csvFileName = "static/exampleData.csv"

class CsvWatcher(RegexMatchingEventHandler):
    csv_file = [r".*\.csv"]
    def __init__(self):
        super().__init__(self.csv_file)

    def on_modified(self,event):
        global csvFileName
        data = readfile(csvFileName)
        socketio.emit('modified', {'data': data})


def background_thread():
    global observer
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CsvWatcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


@app.route('/')
def index():
    global csvFileName
    data = readfile(csvFileName)
    return render_template('index.html', data=data)


@socketio.on('connect')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

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
    return data

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    if observer is not None:
        observer.stop()
        observer.join()
