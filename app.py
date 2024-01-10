from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Return a beautiful HTML message
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the Beautiful World of Flask!</title>
    </head>
    <body style="text-align: center; padding: 50px;">
        <h1 style="color: #336699; font-family: 'Arial', sans-serif;">Welcome to the Beautiful World of Flask!</h1>
        <p style="font-size: 18px; color: #555;">This is a simple Flask web application.</p>
        <img src="https://your-image-url.com" alt="Flask Logo" style="max-width: 300px; margin-top: 20px;">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
