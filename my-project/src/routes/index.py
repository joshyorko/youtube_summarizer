from flask import Blueprint
from .controllers.index import Controller

routes = Blueprint('routes', __name__)
controller = Controller()

@routes.route('/youtube', methods=['GET'])
def get_youtube_data():
    return controller.get_youtube_data()