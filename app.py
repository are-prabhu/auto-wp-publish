'''
This app usage is 
#imsudo.com/v1/articles/publish/0/2/http://www.mikeperham.com/2014/07/07/use-runit/
'''

from flask import Flask, abort, request, render_template, Blueprint
from flask.views import MethodView, View
from processor.img_processor import Posters

app = Flask(__name__)

class Publish(MethodView):
    def post(self,description,category,url,status):
        if description == 1:
            state=Posters(url,category,status,description=False).post()
        elif description == 0:
            state=Posters(url,category,status,description=True).post()
        return state

app.add_url_rule('/v1/articles/<string:status>/<int:description>/<int:category>/<path:url>', view_func=Publish.as_view(''),methods=['POST','GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

