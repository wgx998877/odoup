import web
from web.contrib.template import render_jinja


urls = (
	'/' , 'index',
)
render = render_jinja('templates',encoding='utf-8')

class index:

	def GET(self):
		return render.index()
		#return "hello, world"


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
