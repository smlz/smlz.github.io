import json
from werkzeug.exceptions import (HTTPException, UnprocessableEntity, NotFound,
                                 Unauthorized)
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

class Application:
    def __init__(self):
        self.url_map = Map()
        self.url_map.add(Rule('/<entity>/', methods=('GET',), endpoint='list'))
        self.url_map.add(Rule('/user/', methods=('POST',), endpoint='create'))
        self.url_map.add(Rule('/user/<int:id>', methods=('GET',), endpoint='read'))
        self.url_map.add(Rule('/user/<int:id>', methods=('PUT',), endpoint='update'))
        self.url_map.add(Rule('/user/<int:id>', methods=('DELETE',), endpoint='remove'))
        self.filename = 'db.json'
        self.users = [{"id": 1, "name": "Kurt Müller", "email": "kuere@ch.ch"}]

    def __call__(self, environ, start_response):
        request = Request(environ)
        # for key, val in environ.items():
        #     print(key, val)
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            response = getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            response = e
        return response(environ, start_response)

    def on_list(self, request, entity):
        print('***** on_list *****')
        with open(self.filename) as f:
            return Response(f.read(), mimetype='text/json')

    def on_create(self, request):
        print('**** on_create *****')
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            data.append(json.loads(request.data))
            f.seek(0)
            json.dump(data, f, indent=2)
            return Response(json.dumps({'status': 'OK'}), mimetype='text/json')

    def on_read(self, request, id):
        with open(self.filename) as f:
            data = json.load(f)
            if 0 <= id < len(data):
                return Response(json.dumps(data[id], indent=2), mimetype='text/json')
            else:
                raise NotFound()


if __name__ == '__main__':
    app = Application()
    run_simple('127.0.0.1', 5000, app, use_debugger=True,
               use_reloader=True, threaded=False)
