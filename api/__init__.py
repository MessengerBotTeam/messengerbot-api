import importlib
import pkgutil

from sanic import Blueprint
blueprints: list[Blueprint] = []

for finder, module_name, is_pkg in pkgutil.walk_packages(__path__):
    if not is_pkg:
        module = importlib.import_module(f'api.{module_name}')

        if hasattr(module, module_name):
            blueprint = getattr(module, module_name)
            blueprints.append(blueprint)

api = []
group = Blueprint.group(*blueprints, url_prefix='/')

api.append(group)
