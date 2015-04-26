#!/usr/bin/env python
# encoding: utf-8

import pymongo
import config

class MongoAPI(object):
  def __init__(self, collection="course_tree"):
    self.conn = pymongo.Connection(config.host, config.port)
    self.db = self.conn.odoup
    self.collection = self.db[collection]

  def FindOne(self, query={}):
    return self.collection.find_one(query)

  def FindAll(self, query={}):
    return self.collection.find(query)

  def UseCollection(self, collection):
    self.collection = self.db[collection]

  def Insert(self, data):
    if not isinstance(data, dict):
      return
    self.collection.insert(data)

  def Save(self, data):
    if not isinstance(data, dict):
      return
    self.collection.save(data)

  def Update(self, query, data):
    if not isinstance(data, dict):
      return
    self.collection.update(query, data)
