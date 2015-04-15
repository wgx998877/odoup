import web
from web.contrib.template import render_jinja


urls = (
	'/' , 'index',
	'/index', 'index',
	'/login', 'login',
	'/register', 'register',
	'/start', 'start',
	'/study', 'study',
	'/guide', 'guide',
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


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
