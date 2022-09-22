import json

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


class Main:
    def __init__(self, file_name=None):
        self.__file_name = file_name

    @staticmethod
    def get_cred(name, age, country):
        content = {
            "name": name,
            "age": age,
            "country": country
        }
        return redirect(url_for("success", name=content))

    @staticmethod
    @app.route("/", methods=["GET", "POST"])
    def form():
        print(request)
        if request.method == "POST":
            return Main.get_cred(
                request.form["name"],
                request.form["select"],
                request.form["select-country"])
        return render_template("index.html")

    @staticmethod
    @app.route('/success/<name>')
    def success(name):
        json_acceptable_string = name.replace("'", "\"")
        name = json.loads(json_acceptable_string)
        print(name['name'])
        return render_template("result.html", name=name)

    @staticmethod
    def run():
        app.run()


if __name__ == '__main__':
    Main.run()
