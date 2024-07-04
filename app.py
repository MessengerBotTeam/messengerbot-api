from sanic import Sanic

from api import api

app = Sanic("messengerbot-api")
app.ext.openapi.describe(
    title="MessengerBot API",
    version="1.0.0",
    description="JSON Api for MessengerBot",
)

app.config.OAS_UI_DEFAULT = 'swagger'

app.blueprint(api)
