#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import redis

class RedisHandler:
  def __init__(self):
    self.r = redis.Redis(
      host='localhost',
      port='6379'
    )

  # Set 'value' in 'key'
  def set(self, key, value):
    self.r.set(key, value)

  # Get the value for 'key'
  def get(self, key):
    return self.r.get(key)

  # Get a list of keys matching pattern (term)
  def keys(self, term):
    return self.r.keys(term)

  # Removes the specified keys
  # A key is ignored if it does not exist
  def delete(self, key):
    self.r.delete(key)

  ##########
  # COMBOS #
  ##########

  # Remove all keys matching pattern (keys + del)
  def remove_all_match_keys(self, term):
    keys = self.keys(term)

    for key in keys:
      print 'Removing %s...' % key
      self.delete(key)


# if __name__ == '__main__':
#   my_redis = RedisHandler()

#   my_redis.set('12345', 'test11')
#   my_redis.set('12346', 'test11')
#   my_redis.set('12347', 'test11')
#   my_redis.set('12348', 'test11')
#   my_redis.set('12349', 'test11')

#   my_redis.remove_all_match_keys('*123*')

#   print my_redis.keys('*123*')
