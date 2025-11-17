from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    response = make_response('Cookie is set!')
    # Set the cookie
    response.set_cookie(
        "my_cookie",
        "my_cookie_value_123",
        httponly=True,
        samesite="lax" # none|lax|strict
    )
    return response

@app.route("/cookie", methods=["GET"])
def see_cookie():
    c = request.cookies.get('my_cookie')
    if c is None:
        return "Cookie not found!!!", 404
    return f"{c}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)