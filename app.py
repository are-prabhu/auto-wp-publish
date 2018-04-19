'''
This app usage is 
#imsudo.com/v1/articles/publish/0/2/http://www.mikeperham.com/2014/07/07/use-runit/
'''

from flask import Flask, abort, request, render_template, Blueprint
from flask.views import MethodView, View
from processor.img_processor import Posters

app = Flask(__name__)

class Publish(MethodView):
    def get(self,description,category,url,status):
        if description == 1:
            state=Posters(url,category,status,description=False).post()
        elif description == 0:
            state=Posters(url,category,status,description=True).post()
        return str(state)


def help():
    return "<h2>Hey you landed in the wrong page, following is the hint to get it right Good Luck :)</h2><p><h4>/v1/artis/status/description(0/1)/catageory(6/7/5/7)/remoteurl</h4></p>"

app.add_url_rule('/v1/articles/<string:status>/<int:description>/<int:category>/<path:url>', view_func=Publish.as_view(''),methods=['POST','GET'])
app.add_url_rule('/', 'help', help)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5260, debug=True)

