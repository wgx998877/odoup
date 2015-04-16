#!/usr/bin/env python
# encoding: utf-8

#-*- coding:utf-8 -*-

# Author: Peng Chao
# Copyright: EverString
# Date: 2013-10-27
# Distributed under terms of the EverString license.

import sys
import logging
logging.basicConfig()
import traceback
from pymongo import Connection


class Mongo(object):
    def __init__(self, **kwargs):
        """
        Input should be like this.
        mon = Mongo(host='www.everstring.net',
                    port=27017,
                    db='esdb',
                    user='test',
                    pswd='test')
        """
        self.logger = logging.getLogger(__name__ + '.log')

        # need keys
        keys = ['host', 'port', 'db', 'user', 'pswd']

        for key in keys:
            if key not in kwargs:
                self.logger.error(key + ' is needed.')
                sys.exit(-1)

        # connect to mongodb
        try:
            self.conn = Connection(kwargs['host'], kwargs['port'])
            self.logger.info('mongodb connect success.')

            # go to database
            self.db = self.conn[kwargs['db']]
            self.db.authenticate(kwargs['user'], password=kwargs['pswd'])
            self.logger.info('mongodb authorize success.')
        except Exception, e:
            self.logger.error('connect to mongodb failed')
            self.logger.error(traceback.format_exc(e))
            sys.exit()

    def get_id(self, collection):
        """ Mongodb Auto-increment id. """
        o = self.db['counters'].find_and_modify(
            query={'_id': collection}, update={'$inc': {'c': 1}})
        return o['c']

    def find_records(self, collection, find_dic):
        """ Find all records according to given restrict. """
        collect = self.db[collection]

        records = collect.find(find_dic, timeout=False).sort('_id', 1)
        for record in records:
            yield record


    def find_One(self, collection, find_dic):
        """ Find all records according to given restrict. """
        collect = self.db[collection]

        record = collect.find_one(find_dic, timeout=False)
        return record

    def find_by_id(self, collection, spec_or_id=None):
        """ Find all records according to given restrict. """
        collect = self.db[collection]

        record = collect.find_one(spec_or_id=None, timeout=False)
        return record

    def count(self,collection,query):
        collect = self.db[collection]
        return collect.find(query, {"_id" : 0}, timeout=False).count()


    def find_some_records(self, collection, find_dic, mount):
        """ Find several records according to given number. """
        collect = self.db[collection]

        records = collect.find(find_dic, timeout=False)\
            .sort('_id', 1).limit(mount)
        for record in records:
            yield record

    def find_record_with_fields(self, collection, find_dic, get_dic):
        """ Find all records and return certain fields. """
        collect = self.db[collection]

        records = collect.find(find_dic, get_dic, timeout=False)
        for record in records:
            yield record


    def find_some_records_with_fields(self, collection, find_dic,get_dic, mount):
        """ Find several records according to given number. """
        collect = self.db[collection]

        records = collect.find(find_dic,get_dic, timeout=False)\
            .sort('_id', 1).limit(mount)
        for record in records:
            yield record


    def update(self, collection, find_dic, new_record):
        """ Update record, add field if no. """
        collect = self.db[collection]

        # insert into collection
        collect.update(find_dic, {'$set': new_record},multi=True)

    def remove_filed(self, collection, find_dic, rm_record):
        """ Remove field of certain records. """
        collect = self.db[collection]

        # insert into collection
        collect.update(find_dic, {'$unset': rm_record},
                       False, False, False, True)

    def insert(self, collection, new_record):
        collect = self.db[collection]
        return collect.insert(new_record)

    def drop_collection(self, collection):
        self.db.drop_collection(collection)

    def ensureIndex(self, collection, index_list):
        collect = self.db[collection]
        collect.ensure_index(index_list,unique = False)

    def disconnect(self):
        self.conn.disconnect()
        self.logger.info('mongodb disconnect success.')

    def find_skip_limit_records(self, collection, find_dic, skip,limit):
        collect = self.db[collection]
        records = collect.find(find_dic, timeout=False)\
            .sort('_id', 1).skip(skip).limit(limit)
        for record in records:
            yield record
    def remove_records(self, collection, find_dic):
        """ Remove field of certain records. """
        collect = self.db[collection]
        collect.remove(find_dic)

if __name__ == "__main__":
    mon = Mongo(host='127.0.0.1',
                port=27017,
                db='odoup',
                user='',
                pswd='',
                )
    mon.find_records('question', {})
    mon.disconnect()

