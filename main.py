#coding:utf-8
import web
from web.contrib.template import render_jinja
from model import *
import json
import datetime
from web import form
web.config.debug = False
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


urls = (
	'/' , 'index',
	'/index', 'index',
	'/login', 'login',
	'/register', 'register',
	'/start', 'start',
	'/study', 'study',
	'/guide', 'guide',
  '/get_question', 'get_question',
  '/get_userlist', 'get_userlist',
)


app = web.application(urls, globals())
render = render_jinja('templates',encoding='utf-8')
session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'login':0,})
question = Question()
user = User(session)


class index:

  def GET(self):
		return render.index()
		#return "hello, world"

class login:

  def GET(self):
    if user.logged():
      return user.userinfo
    return render.login()

  def POST(self):
    postdata = web.input()
    username = web.net.websafe(postdata.username)
    password = web.net.websafe(postdata.password)
    userlist = user.get_user({'username':username})
    print userlist
    if userlist is None:
      return 'no user'
    u = userlist[0]
    if u['password'] != password:
      return 'password error'
    else:
      if user.signIn({'username':username,'password':password}):
        return True
      return False

class logout:
  def POST(self):
    user.logout()
    return render.logout()

class register:
  vusername= form.regexp(r".{3,20}$", '用户名长度为3-20位')
  vpass = form.regexp(r".{6,20}$", '密码长度为6-20位')
  vemail = form.regexp(r".*@.*", "must be a valid email address")
  regForm=web.form.Form(
        form.Textbox('username',vusername,description=u'用户名'),
        form.Password("password",vpass,description=u"密码"),
        form.Password("password2", description=u"确认密码"),
        form.Button(u"马上注册", type="submit", description="submit"),
        validators = [
            form.Validator("两次输入的密码不一致", lambda i: i.password == i.password2)]
        )
  def GET(self):
      return render.register()

  def POST(self):
      formdata = web.input()
      username = web.net.websafe(formdata.username)
      password = web.net.websafe(formdata.password)
      regip = web.ctx.ip
      regdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      if not self.regForm.validates():
        return render.register()
      else :
        if user.get_user({'username':username}) is not None:
          return render.register()
        else:
          u = {
              'username':username,
              'password':password,
              'regip'   :regip,
              'regdate' :regdate,
          }
          if user.add_user(u):
            return web.seeother('/start')
          else:
            return u'Register Failed!'
      return None


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
    result = json.dumps(result)
    return result

class get_userlist:
  def GET(self):
    query = {}
    result = user.get_user(query)
    for i in result:
      i['_id'] = str(i['_id'])
    result = {
        'count' : len(result),
        'userlist' : result
        }
    result = json.dumps(result)
    return result


if __name__ == "__main__":
  app.run()
