import web


class index:

	def GET(self):
		return "hello, world"

urls = (
	'/' , 'index',
)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
