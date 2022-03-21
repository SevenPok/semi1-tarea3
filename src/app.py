from flask import Flask, request
from decouple import config
import boto3
import base64


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/tarea3-201800586", methods=["POST"])
def tarea3():
    try:
        image = request.json["image"]
        rekognition = boto3.client("rekognition", aws_access_key_id=config(
            "AWS_ACCESS_KEY_ID"), aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"), region_name=config("AWS_REGION"))
        foto = base64.b64decode(image)

        res = rekognition.detect_faces(
            Image={"Bytes": foto}, Attributes=["ALL"])
        return res
    except Exception as e:
        return "Ocurrio un error al procesar la imagen: " + str(e)
