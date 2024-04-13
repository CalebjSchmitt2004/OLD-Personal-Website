from flask import Flask
from Website.views import views
from Website.images import images

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(images, url_prefix="/images")

if __name__ == "__main__":
    app.run(port=8000, host="10.42.1.10")
