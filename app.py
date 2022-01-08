import os
from src import init_app
app = init_app()

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = os.getenv("FLASK_ENV")

    app.run(host='0.0.0.0', port=8000, debug=True)
