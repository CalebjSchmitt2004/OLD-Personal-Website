from flask import Flask
from views import views
from images import images

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(images, url_prefix="/images")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
