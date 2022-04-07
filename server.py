from flask import Flask, render_template
import connexion


app = Flask(__name__, template_folder="templates")


@app.route('/')
def home() -> 'home.html':
    return render_template('home.html')


if __name__ == '__main__':
   app.run(debug=True)