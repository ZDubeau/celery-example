from flask import Flask, redirect, render_template, request, url_for

from .celery import celery_app


app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/subscribe_sync", methods=["POST"])
def subscribe_sync():
    from .tasks import subscribe_to_newsletter

    email = request.form.get("email")
    subscribe_to_newsletter(email)

    return redirect(url_for("thanks"))


@app.route("/subscribe_async", methods=["POST"])
def subscribe_async():
    email = request.form.get("email")
    celery_app.send_task("tasks.subscribe_to_newsletter", args=[email])

    return redirect(url_for("thanks"))


@app.route("/thanks", methods=["GET"])
def thanks():
    return render_template("thanks.html")
