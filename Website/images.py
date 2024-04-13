from flask import Blueprint, send_file
import flask

images = Blueprint("images", __name__)


@images.route("/homepage/message")
def homepage_message_image():
    return send_file("./images/homepage-message.jpeg")


@images.route("/about/me")
def about_profile_image():
    return send_file("./images/me.jpeg")


@images.route("/website/icon")
def icon():
    return send_file("./images/icon.png")
