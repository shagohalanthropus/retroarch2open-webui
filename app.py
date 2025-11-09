#!/bin/python3

import os
import requests
import tempfile

from base64 import b64decode, b64encode
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from paddleocr import PaddleOCR, TextRecognition
from PIL import Image, ImageDraw
from pprint import pprint


app = Flask(__name__)
load_dotenv()

try:
    apikey = os.environ["OPEN_WEBUI_APIKEY"]
    base_url = os.environ["OPEN_WEBUI_URL"]
    model = os.environ["TRANSLATION_MODEL"]
except KeyError as e:
    print(f"Couldn't find {e} in your .env file.")
    exit(1)

def translate_image(image_file):
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False
    )
    result = ocr.predict(input=image_file.name)

    for res in result:
        pprint(res)
        boxes = res["rec_boxes"].tolist()
        texts = res["rec_texts"]
        with Image.open(image_file) as img:
            for b, t in zip(boxes, texts):
                translated_text = translate_text(t)["choices"][0]["message"]["content"]
                draw = ImageDraw.Draw(img)
                draw.rectangle(b, fill="black", outline="green")
                draw.text(xy=(b[0], b[1]), text=translated_text, fill="white")
            img.save(image_file.name)

def translate_text(text):
    endpoint = "/api/chat/completions"
    full_url = base_url.removesuffix("/") + endpoint

    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {
            "role": "user",
            "content": text
            }
        ]
    }

    response = requests.post(full_url, headers=headers, json=data)
    pprint(response.json())
    return response.json()

@app.route("/", methods=["POST"])
def retroarch_to_open_webui():
    data = request.get_json(force=True)

    image_data = b64decode(data["image"])
    image_file = tempfile.NamedTemporaryFile(suffix=".png",delete=False)

    with open(image_file.name, "wb") as f:
        f.write(image_data)

    translate_image(image_file)

    return jsonify({"image": b64encode(open(image_file.name, "rb").read()).decode()})

if __name__ == "__main__":
    app.run(debug=True)
