from flask import Flask

import config

app = Flask(__name__)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.Config)

    with app.app_context():
        import routes

 #   cors = CORS()
  #  cors.init_app(app)

    return app


@app.route('/')  # to test api
def home():
    return "hello"


if __name__ == '__main__':
    app = create_app
    app.run(debug=True)
