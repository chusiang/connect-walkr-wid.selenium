#!/usr/bin/python
# -*- coding: utf8 -*-
# ============================================================
#  Author: chusiang / chusiang.lai (at) gmail.com
#  Blog: http://note.drx.tw
#  Filename: play.py
#  Modified: 2020-04-07 11:15
#  Description: Auto checkin the WID with Selenium and Firefox.
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ConfigParser
import logging
from time import sleep


# profile = ['<URL>', '<MY_WID>', '<FRIEND_WID>']
def load_setting():
    config = ConfigParser.ConfigParser()
    config.read('setting.ini')

    url = config.get('profile', 'url')
    my_wid = config.get('profile', 'my_wid')
    _profile = ["url", url, "my_wid", my_wid]

    # Load all friends_wid.
    _friends_wid = config.items("friends_wid")
    _profile.append(_friends_wid)

    logging.info('Load setting.')
    return _profile


# Open Firefox and verify new friend's WID on official website.
def checkin(_profile):

    # Open the Firefox and go to the verify website.
    driver.get(_profile[1])
    logging.info('Go to website.')
    assert "COMMUNITY - Walkr - Galaxy Adventure in Your Pocket" in driver.title

    # Loop for keyin firends wid.
    _friends_wid = _profile[4]
    for _item in _friends_wid:

        # Keyin the my_wid.
        elem_my_wid = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/input')
        elem_my_wid.send_keys(_profile[3])
        logging.info('Keyin my WID: ' + _profile[3])

        # Keyin the friend_wid.
        elem_friend_wid = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/div[3]/input')
        elem_friend_wid.send_keys(_item[1])
        logging.info('Keyin new friend\'s WID: ' + _item[1])

        # Click submit.
        elem_submit = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div[3]/a/div[1]')
        elem_submit.click()
        logging.info('Click verify buttion')

        # Review result.
        sleep(60)

        # Refresh web page.
        driver.refresh()


# Close the Firefox.
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
