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
	'/logout', 'logout',
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
    if user.logged():
      u = user.userinfo
    else:
      u = None
    return render.index(user=u)

class login:

  def GET(self):
    if user.logged():
      return render.index(user=user.userinfo)
    return render.login()

  def POST(self):
    postdata = web.input(username='', password='')
    username = web.net.websafe(postdata.username)
    password = web.net.websafe(postdata.password)
    userlist = user.get_user({'username':username})
    if userlist is None:
      return 'no user'
    u = userlist[0]
    if u['password'] != password:
      return 'password error'
    else:
      if user.signIn({'username':username,'password':password}):
        return web.seeother('/index')
      return 'system error'

class logout:
  def GET(self):
    user.logout()
    return web.seeother('/index')

class register:
  def GET(self):
    return render.register()

  def POST(self):
    formdata = web.input()
    print formdata
    if 'username' not in formdata:
      return 'no username'
    else :
      username = web.net.websafe(formdata.username)
      password = web.net.websafe(formdata.password1)
      regip = web.ctx.ip
      regdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      if user.get_user({'username':username}) is not None:
        return 'user exits'
      else:
        u = {}
        u['username'] = username
        u['password'] = password
        u['regip'] = regip
        u['regdate'] = regdate
        if user.add_user(u):
          return web.seeother('/start')
        else:
          return u'Register Failed!'
    return None


class start:

  def GET(self):
    return render.start()

class study:

  def GET(self):
    q = question.get_question()['result'][0]
    return render.study(question=q)

class guide:

  def GET(self):
	return render.guide()

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
    if result is None:
        return ''
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
