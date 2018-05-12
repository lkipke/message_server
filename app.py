from flask import Flask, render_template
from controllers.main import main

# Initialize Flask app
app = Flask(__name__)

# Register the controllers
app.register_blueprint(main)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(port=3000, debug=True)
