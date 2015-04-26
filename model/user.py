#!/usr/bin/env python
# encoding: utf-8

from base import Base
class User(Base):
  @classmethod
  def FindAll()
  def __init__(self, data_dict={}):
    self.data_dict = data_dict
    self.__class__.db.UseCollection("User")
    self.Init(data_dict)

  def Init(self, data_dict):
    self.user_id = ""
    self.nickname = ""
    self.password = ""
    self.tel = ""
    self.email = ""
    self.school = ""
    self.grade = ""
    self.task_list = []
    self.history_task_list = []
    if "user_id" in data_dict:
      self.user_id = data_dict["user_id"]
    if "nickname" in data_dict:
      self.nickname = data_dict["nickname"]
    if "password" in data_dict:
      self.password = data_dict["password"]
    if "tel" in data_dict:
      self.tel = data_dict["tel"]
    if "email" in data_dict:
      self.email = data_dict["email"]
    if "school" in data_dict:
      self.school = data_dict["school"]
    if "grade" in data_dict:
      self.grade = data_dict["grade"]
    if "task_list" in data_dict:
      self.task_list = data_dict["task_list"]
    if "history_task_list" in data_dict:
      self.history_task_list = data_dict["history_task_list"]

if __name__ == '__main__':
  #新建user
  #user = User({"user_id":"15201017684"})
  #保存user
  #user.Save()
  user = User.FindAll({"user_id":"15201017684"})
  for i in user:
