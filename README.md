# Retroarch2Open-WebUI
A very basic proof of concept that allows Retroarch to get translations from models hosted on an Open-WebUI instance. 

## How To Use This Script
1. Clone this repository.
```Shell
git clone https://github.com/shagohalanthropus/retroarch2open-webui.git
```
2. Install dependencies.
```Shell
cd retroarch2open-webui
python3 -m pip install -r requirements.txt
```
3. Create your .env file with the following environment variables:


| Environment Variable | Required |                                                              Description                                                              |
| :----: | :----: |:-------------------------------------------------------------------------------------------------------------------------------------:|
| **TRANSLATION_MODEL** | :heavy_check_mark: |                                   The model that you want to use to translate, e.g. aya-expanse:8b                                    | 
| **OPEN_WEBUI_APIKEY** | :heavy_check_mark: |                                          Your Open-WebUI API key, can also be the JWT Token.                                          |
| **OPEN_WEBUI_URL** | :heavy_check_mark: |                                                 The URL for your Open-WebUI instance.                                                 |
| **PORT** | :heavy_multiplication_x: |                                        The port the script should run on. <br/>(Default: 5000)                                        |
| **BG_TYPE** | :heavy_multiplication_x: | The type of background the translated text should have.  <br/><br/>Options:  <br/>- **solid**  <br/>- **blur**  <br/>(Default: solid) |
| **BG_COLOR** | :heavy_multiplication_x: |                                          The background color to use. <br/>(Default: black)                                           |
| **BORDER_COLOR** | :heavy_multiplication_x: | The color of the border surrounding the translated text. <br/>(Default: green) |
| **FONT_COLOR** | :heavy_multiplication_x: | The color to use for the font. <br/>(Default: white) |
| **FONT_OUTLINE_COLOR** | :heavy_multiplication_x: | The color to use as the outline for the font. </br>(Default: black) |

<sub>*All variables that define color accept common HTML color names, e.g. "red" or hex codes, e.g. "#FF0000".</sub>

### Example .env file:
```Dotenv
TRANSLATION_MODEL=aya-expanse:8b
OPEN_WEBUI_APIKEY=myapikeymyapikeymyapikey
OPEN_WEBUI_URL=https://my.open.webui.com
```

4. Set up Retroarch to use this script. By default, only the computer running this script will have access to flask
endpoint. Open Retroarch then go to **Settings > Input > Hotkeys > AI Service** and set the key you want to use to activate
translations. Once set, go back to **Settings** and choose **Accessibility > AI Service** toggle **AI Service** to **ON**, **AI Service
Mode** to **Image**, **AI Service URL** to **http://localhost:5000**, and **Pause During Translation** to **ON**.<br/><br/>
5. Start the python script.
```Shell
python3 ./app.py
```
6. Open a game you want to translate and try using the hotkey you set up in Retroarch and see if the translation service
works.

## TODO
- Stop sending fragmented texts to Open-WebUI, instead send as one whole group for more accurate translation.
- Increase the quality of the image returned by the script.
- Perform manipulations on the image Retroarch sends for higher OCR accuracy.
- Etc.

## Modules/Libraries
- dotenv: https://github.com/theskumar/python-dotenv
- Flask: https://github.com/pallets/flask/
- PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
- Pillow: https://github.com/python-pillow/Pillow
- requests: https://github.com/psf/requests
