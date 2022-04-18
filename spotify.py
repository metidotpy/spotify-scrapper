from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from create_all import create_all
import time
import os


name = input("enter your file name: ")
url = input('enter playlists url: ')
playlists = []

driver = webdriver.Chrome(".\chromedriver.exe")
try:
    driver.get(url)
    time.sleep(5)
    try:
        plays = driver.find_elements(By.CSS_SELECTOR, '.Nqa6Cw3RkDMV8QnYreTr')
    except NoSuchElementException:
        print('cant find a playlist link.')
    for play in plays:
        try:
            if play.get_attribute('href') in playlists:
                continue
            else:
                playlists.append((play.get_attribute('href')))
        except:
            if playlists:
                if '.' in name:
                    new_name = name[:name.find('.')]
                    os.mkdir(new_name)
                    create_all.all(path=new_name, name=name, datas=playlists)
                else:
                    os.mkdir(name)
                    create_all.all(path=name, name=name, datas=playlists)
except Exception as e:
    print('error on this url => {0}, reason => {1}'.format(url, e))
if playlists:
    if '.' in name:
        new_name = name[:name.find('.')]
        os.mkdir(new_name)
        create_all.all(path=new_name, name=name, datas=playlists)
    else:
        os.mkdir(name)
        create_all.all(path=name, name=name, datas=playlists)