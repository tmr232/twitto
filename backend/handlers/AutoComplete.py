import tornado.web
from backend.user_auth import user_required

class AutoCompleteHandler(tornado.web.RequestHandler):
    """
    The Base type of a RequestHandler that handles requests from
    the autocomplete handlers.
    """
    def initialize(self, model, autocomplete_field, exclude_fields=None):
        self._model = model
        self._autocomplete_field = autocomplete_field
        self._exclude_fields = exclude_fields
        if exclude_fields is None:
            self._exclude_fields = {}

    @user_required
    def get(self, filter_option):
        """
        The GET Handler for the AutoCompleteHandler.
        """
        filter_query = {}
        if filter_option:  # if a filter is given in the url we search like with '__startswith'
            filter_query = {self._autocomplete_field: {"$regex": u"^{}".format(filter_option)}}
        results = self._model.objects.filter(__raw__=filter_query).only(*self._exclude_fields)
        if not results:
            raise tornado.web.HTTPError(404)

        self.write(results.to_json())
