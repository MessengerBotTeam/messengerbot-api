import os.path

from sanic import Blueprint, Request
from sanic.response import JSONResponse, json
from sanic_ext import openapi

from api.models.socials import SocialsResponse
from config import social_links

socials: Blueprint = Blueprint(os.path.basename(__file__).strip('.py').__str__())


@socials.route('/socials', methods=['GET'])
@openapi.definition(
    summary='Get Socials information',
    response=[SocialsResponse]
)
async def socials_get(request: Request) -> JSONResponse:
    data: dict[str, dict] = {"socials": social_links}
    return json(data, status=200)
