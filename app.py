from typing import Any

import sanic
from sanic import Sanic

from api import api

REDIRECTS = {
    '/': '/docs/swagger'
}

app = Sanic("messengerbot-api")
app.ext.openapi.describe(
    title="MessengerBot API",
    version="1.0.0",
    description="JSON Api for MessengerBot",
)

app.config.OAS_UI_DEFAULT = 'swagger'

app.blueprint(api)


def get_static_function(value) -> Any:
    return lambda *_, **__: value


for src, dest in REDIRECTS.items():
    app.route(src)(get_static_function(sanic.response.redirect(dest)))
