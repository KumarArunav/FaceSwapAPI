
import awsgi
from flask import Flask
from routes import swap_faces_api_bp, swap_faces_client_bp,swap_faces_base64_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(swap_faces_api_bp)
app.register_blueprint(swap_faces_client_bp)
app.register_blueprint(swap_faces_base64_bp)


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == '__main__':
    app.run(debug=True)


