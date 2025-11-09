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
# Load our .env file
load_dotenv()

# If any of the environment variables aren't in our .env file, exit with status code 1.
try:
    apikey = os.environ["OPEN_WEBUI_APIKEY"]
    base_url = os.environ["OPEN_WEBUI_URL"]
    model = os.environ["TRANSLATION_MODEL"]
except KeyError as e:
    print(f"Couldn't find {e} in your .env file.")
    exit(1)

port = os.environ.get("PORT", 5000)

def translate_image(image_file):
    # Set up PaddleOCR
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False
    )
    # Perform OCR and get our results
    result = ocr.predict(input=image_file.name)

    # For each result, get the bounding boxes and text that were returned by PaddleOCR.
    for res in result:
        pprint(res)
        boxes = res["rec_boxes"].tolist()
        texts = res["rec_texts"]
        with Image.open(image_file) as img:
            # b is for bounding boxes, t is for text
            for b, t in zip(boxes, texts):
                # Translate our extracted text
                translated_text = translate_text(t)["choices"][0]["message"]["content"]
                draw = ImageDraw.Draw(img)
                # Draw both the bounding boxes and translated text to our image.
                # xy is the upper left corner of the bounding box.
                draw.rectangle(b, fill="black", outline="green")
                draw.text(xy=(b[0], b[1]), text=translated_text, fill="white")
            img.save(image_file.name)

# Send our extracted text to Open-WebUI for translation
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
    return response.json()

# The endpoint that Retroarch interacts with
@app.route("/", methods=["POST"])
def retroarch_to_open_webui():
    data = request.get_json(force=True)

    # Retroarch sends images as a Base64 encoded string, so we have to decode it
    image_data = b64decode(data["image"])
    image_file = tempfile.NamedTemporaryFile(suffix=".png",delete=False)

    with open(image_file.name, "wb") as f:
        f.write(image_data)

    translate_image(image_file)

    # Take our translated image and re-encode it with Base64 and send it back to Retroarch
    return jsonify({"image": b64encode(open(image_file.name, "rb").read()).decode()})

if __name__ == "__main__":
    app.run(debug=True, port=port)
