#!/usr/bin/python
# -*- coding: utf8 -*-
# ============================================================
#  Author: chusiang / chusiang.lai (at) gmail.com
#  Blog: http://note.drx.tw
#  Filename: play.py
#  Modified: 2016-04-18 10:07
#  Description: Auto checkin the WID with Selenium and Firefox.
# =========================================================== 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ConfigParser
import logging
from time import sleep


"""
profile = ['<URL>', '<MY_WID>', '<FRIEND_WID>']
"""
def load_setting():
  config = ConfigParser.ConfigParser()
  config.read('setting.ini')
    
  url = config.get('profile', 'url')
  my_wid = config.get('profile', 'my_wid')
  profile = [url, my_wid]

  # load all friends_wid.
  _friends_wid = config.items("friends_wid")
  for item in _friends_wid:
    print "key = %s, valule = %s" % (item[0], item[1])

  print _friends_wid

  logging.info('Load setting.')
  return profile


"""
Open Firefox and verify new friend's WID on official website.
"""
def checkin(profile):

  # Open the Firefox and go to the verify website.
  _url = str(profile[0])
  driver.get(_url)
  assert "COMMUNITY - Walkr - Galaxy Adventure in Your Pocket" in driver.title
  logging.info('Go to website.')
  
  # keyin the my_wid.
  elem_my_wid = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/input')
  elem_my_wid.send_keys(profile[1])
  logging.info('Keyin my WID: ' + profile[1])
  
  # keyin the friend_wid.
  elem_friend_wid = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/div[3]/input')
  elem_friend_wid.send_keys(profile[2])
  logging.info('Keyin new friend\'s WID: ' + profile[2])
  
  # click submit.
  elem_submit = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/a/div[1]')
  elem_submit.click()
  logging.info('Click verify buttion')
  
  # review result.
  sleep(3)


"""
Close the Firefox.
"""
def close():
  driver.close()

if __name__ == "__main__":

  try:
    logging.basicConfig(filename='runtime.log', \
      format='[%(asctime)s] %(levelname)s: %(message)s', \
      level=logging.INFO)
    profile = load_setting()

    driver = webdriver.Firefox()
    checkin(profile)

  finally:
    close()
    pass

