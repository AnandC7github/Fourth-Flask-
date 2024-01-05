from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, now you are in the home page! add /home to move to the next page'


@app.route('/home')
def hello_home():
  return render_template('index.html')


@app.route('/view')
def hello_view():
  return render_template('view.html')


@app.route('/book')
def hello_book():
  return 'Hello, Books !'


#testing
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
  #print("Hello!")