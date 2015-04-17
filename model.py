#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient
import config
import logging
logging.basicConfig()


class Base(object):

  def __init__(self):
    self.conn = MongoClient(config.host,config.port).odoup
    self.logger = logging.getLogger(__name__ + '.log')

class Question(Base):

  def __init__(self):
    super(Question, self).__init__()
    self.db = self.conn.questions

  def save_question(self, question):
    if not isinstance(question, dict):
      return None
    try:
      self.db.save(question)
      return True
    except:
      return False

  def get_question(self,query = {}):
    result = {}
    if not isinstance(query, dict):
      return None
    result['query'] = query
    try:
      r = []
      for i in self.db.find(query):
        i['_id'] = str(i['_id'])
        r.append(i)
      result['result'] = r
      result['count'] = len(result['result'])
      result['status'] = config.NORMAL
    except Exception, e:
      self.logger.error(e)
      result['status'] = config.ERROR
    return result



class User(Base):

  def __init__(self, session = None):
    super(User, self).__init__()
    self.db = self.conn.user
    self.session = session
    self.userinfo = None


  def logged(self):
    if self.session.login == 1:
      return True
    else:
      return False

  def add_user(self, userinfo):
    if not isinstance(userinfo, dict):
      return False
    try:
      return self.db.save(userinfo)
    except:
      return False

  def del_user(self, userinfo):
    if not isinstance(userinfo):
      return False
    if 'username' not in userinfo or 'password' not in userinfo:
      return False
    if not self.has_user(userinfo):
      return False
    try:
      return self.db.remove(userinfo)
    except:
      return False

  def update_user(self, query, userinfo):
    if not isinstance(query):
      return False
    if 'username' not in query or 'password' not in query:
      return False
    if not self.has_user(query):
      return False
    if not isinstance(userinfo):
      return False
    if 'username' not in userinfo or 'password' not in userinfo:
      return False
    if not self.has_user(userinfo):
      return False
    try:
      return self.db.update(query, {'$unset': userinfo}, False, False, False, True)
    except:
      return False

  def get_user(self, userinfo):
    if not isinstance(userinfo, dict):
      return None
    try:
      result = list(self.db.find(userinfo))
      if len(result) == 0:
        return None
      return result
    except:
      return None

  def has_user(self, userinfo):
    if not isinstance(userinfo, dict):
      return False
    if self.db.find_one(userinfo) is not None:
      return True
    else:
      return False

  def signIn(self, userinfo):
    if not isinstance(userinfo, dict):
      return False
    if 'username' not in userinfo or 'password' not in userinfo:
      return False
    if not self.has_user(userinfo):
      return False
    try:
      self.session.login = 1
      self.userinfo = self.get_user(userinfo)[0]
      return True
    except:
      return False

  def signUp(self, userinfo):
    if not isinstance(userinfo, dict):
      return False
    if self.has_user(userinfo):
      return False
    try:
      self.db.save(userinfo)
      return True
    except:
      return False

  def checkItems(self, keys):
    key = []
    for i in keys:
      if i not in key:
        return False
    return True

  def get_current_user(self):
    if self.session is None or self.session.login != 1:
      return None
    return self.userinfo

  def logout(self):
    self.session.login = 0
    self.session.kill()
    self.userinfo = None
    return True

if __name__ == "__main__":
  q = Question()
  r = q.get_question()
  import json
  print json.dumps(r)
