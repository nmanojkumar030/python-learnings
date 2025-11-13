from flask import Flask
from datetime import date, datetime
from flask import request
from collections import namedtuple

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "Title": "VeryOwnAPI",
        "Date": date.today(),
        "Timestamp": datetime.now().timestamp(),
    }


Response = namedtuple("Response", "response accuracy")


@app.route("/chat")
def chat(): 
    user_input: str = request.args.get("input")
    response: Response = get_response(user_input)
    return {
        "input": user_input,
        "accuracy": response.accuracy,
        "response": response.response,
    }


def get_response(user_input: str) -> Response:
    if user_input == "hello":
        return Response(response="Hello, how are you?", accuracy="1")
    elif user_input == "bye":
        return Response(response="Goodbye, see you later!", accuracy="1")
    else:
        return Response(response="I'm not sure what you mean.", accuracy="0")


if __name__ == "__main__":
    app.run(debug=True)
