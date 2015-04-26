#!/usr/bin/env python
# encoding: utf-8

import sys
sys.path.append("../api")
from api import mongo_api

class Base(object):
  db = mongo_api.MongoAPI()

  @classmethod
  def FindAll(cls, query_dict={}):
    return cls.db.FindAll(query_dict)

  def Save(self):
    self.__class__.db.Save(self.data_dict)
