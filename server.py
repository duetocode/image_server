from flask import Flask, make_response
import binascii

from database import Database


app = Flask(__name__)

database = Database("data/databasea.sqlite")


@app.route("/_alpha/image/<md5_sum>")
def hello_world(md5_sum: str) -> str:
    checksum = binascii.a2b_hex(md5_sum)
    data = database.get_image(checksum)

    if data is None:
        return make_response("NOT FOUND", 4040)

    resp = make_response(data, 200)
    resp.headers["Content-Type"] = "image/jpeg"
    return resp
