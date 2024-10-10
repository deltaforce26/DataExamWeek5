from flask import Flask
from controllers.crash import crash_bp
from controllers.index import index_bp

app = Flask(__name__)


app.register_blueprint(crash_bp)
app.register_blueprint(index_bp)



if __name__ == '__main__':
    app.run(debug=True)
