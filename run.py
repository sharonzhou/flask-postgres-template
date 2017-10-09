from app import app
import os

port = int(os.environ.get("PORT", 5000))
host = os.environ.get("HOST", "0.0.0.0")
app.run(debug=True, host=host, port=port)