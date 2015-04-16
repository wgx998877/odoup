#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient
import config
import logging


class Question():
    def __init__(self):
        self.conn = MongoClient(config.host,config.port)
        self.db = self.conn.odoup.question
        self.logger = logging.getLogger()


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

if __name__ == "__main__":
    q = Question()
    r = q.get_question()
    import json
    print json.dumps(r)
