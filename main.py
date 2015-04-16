import web
from web.contrib.template import render_jinja
from model import *
import json

urls = (
	'/' , 'index',
	'/index', 'index',
	'/login', 'login',
	'/register', 'register',
	'/start', 'start',
	'/study', 'study',
	'/guide', 'guide',
'/get_question', 'get_question'
)
render = render_jinja('templates',encoding='utf-8')

class index:

	def GET(self):
		return render.index()
		#return "hello, world"

class login:

	def GET(self):
		return render.login()
		#return "hello, world"

class register:

	def GET(self):
		return render.register()
		#return "hello, world"

class start:

	def GET(self):
		return render.start()
		#return "hello, world"

class study:

	def GET(self):
		return render.study()
		#return "hello, world"

class guide:

	def GET(self):
		return render.guide()
		#return "hello, world"

class get_question:
    def GET(self):
        query = {}
        result = question.get_question(query)
        print result
        result = json.dumps(result)
        return result

question = Question()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
