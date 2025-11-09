# Retroarch2Open-WebUI
A very basic proof of concept that allows Retroarch to get translations from models hosted on an Open-WebUI instance. 

In order to use this script you will need to a create a .env file with all of the following environment variables:

|Environment Variable|Description                                                     |
|--------------------|----------------------------------------------------------------|
|TRANSLATION_MODEL   |The model that you want to use to translate, e.g. aya-expanse:8b|
|OPEN_WEBUI_APIKEY   |Your Open-WebUI API key, can also be the JWT Token.             |
|OPEN_WEBUI_URL      |The URL for your Open-WebUI instance.                           |

### Example .env file:
```Dotenv
TRANSLATION_MODEL=aya-expanse:8b
OPEN_WEBUI_APIKEY=myapikeymyapikeymyapikey
OPEN_WEBUI_URL=https://my.open.webui.com
```

### Modules/Libraries:
- dotenv: https://github.com/theskumar/python-dotenv
- Flask: https://github.com/pallets/flask/
- PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
- Pillow: https://github.com/python-pillow/Pillow
- requests: https://github.com/psf/requests