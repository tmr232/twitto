"""
RESTFactory.py
This module defines a class that creates a RESTHandler to a given Model.
Author: Arie Bro
"""
import json
import tornado.web
from backend.user_auth import user_required


class RESTHandler(tornado.web.RequestHandler):
    """
    A RequestHandler used as a RESTful controller for the given document_model
    """

    MODEL = None

    #@user_required
    def get(self, *args, **kwargs):
        """
        The GET Method function handler.
        returns the items of the given model.
        """
        items = [item.to_json() for item in self.__class__.MODEL.objects]
        self.write(json.dumps(items))

    @user_required
    def post(self, *args, **kwargs):
        """
        The POST Method function handler.
        creates a new item and adds it to the database.
        """
        new_item_data = json.loads(self.request.body)
        new_item_model = self.__class__.MODEL.from_json(new_item_data)
        new_item_model.save()

    @user_required
    def delete(self, id):
        """
        The DELETE Method function handler.
        deletes the item with the given id from the database.
        """
        item = self.__class__.MODEL.objects.get(id=id)
        item.delete()

    @user_required
    def put(self, id):
        """
        The PUT Method Function handler.
        updates a given item with the new data.
        """
        request_content = json.loads(self.request.body)
        item = self.__class__.MODEL.fromjson(request_content)
        requested_item = self.__class__.MODEL.objects.get(id)
        if not requested_item:
            raise tornado.web.HTTPError(404)

        requested_item.copy(item)  # copies the data from item to requested_item
        self.write(json.dumps(requested_item.serialize()))


class RESTHandlerFactory(object):
    """
    This class is a Factory that creates RESTHandlers.
    """
    def __init__(self):
        super(RESTHandlerFactory, self).__init__()
        self._handlers = dict()

    def get_model_rest_handler(self, document_model):
        """
        Creates and returns a RESTful tornado handler for a given model.
        only if there isn't a Handler for it already.
        """
        rest_handler = self._handlers.get(document_model)
        if rest_handler:
            return rest_handler

        class GeneratedHandler(RESTHandler):
            MODEL = document_model

        return GeneratedHandler
