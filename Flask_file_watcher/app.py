import sys
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no_key'

socketio = SocketIO(app)

thread = None
observer = None

class CsvWatcher(RegexMatchingEventHandler):
    csv_file = [r".*\.csv"]
    def __init__(self):
        super().__init__(self.csv_file)

    def on_modified(self,event):
        socketio.emit('modified')


def background_thread():
    global observer
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CsvWatcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('connect')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app, debug=True)
    if observer is not None:
        observer.stop()
        observer.join()
