# Retroarch2Open-WebUI
A very basic proof of concept that allows Retroarch to get translations from models hosted on an Open-WebUI instance. 

### How to use this script:
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


| Environment Variable  |Description                                                     |
|-----------------------|----------------------------------------------------------------|
| **TRANSLATION_MODEL** |The model that you want to use to translate, e.g. aya-expanse:8b|
| **OPEN_WEBUI_APIKEY** |Your Open-WebUI API key, can also be the JWT Token.             |
| **OPEN_WEBUI_URL**    |The URL for your Open-WebUI instance.                           |

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

### Modules/Libraries:
- dotenv: https://github.com/theskumar/python-dotenv
- Flask: https://github.com/pallets/flask/
- PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
- Pillow: https://github.com/python-pillow/Pillow
- requests: https://github.com/psf/requests