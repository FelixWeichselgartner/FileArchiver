from flask import Flask, request, render_template, send_file
from FileArchiver import FileArchiver


app = Flask(__name__)


@app.route('/get-files/', methods=['GET'])
def get_files():
    fa = FileArchiver()
    return send_file(fa.today(), download_name=fa.today())


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    """ run the flask app. """
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
