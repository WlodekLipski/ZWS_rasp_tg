from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subprocess.Popen(['./switch_network.sh %s %s' % (request.form['ssid'], request.form['password'])], shell=True)
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
