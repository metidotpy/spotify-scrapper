from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from create_all import create_all
import time


name_of_path = input("enter path name: ")
urls = json_.read_data(path=name_of_path, name=name_of_path)
iframes = {}

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
action = ActionChains(driver=driver)

for index, url in enumerate(urls):
    try:
        driver.get(url)
        if index == 0:
            time.sleep(5)
        else:
            time.sleep(3)
        name = driver.find_element(By.CSS_SELECTOR, '#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.contentSpacing.NXiYChVp4Oydfxd7rT5r.RMDSGDMFrx8eXHpFphqG > div.RP2rRchy4i8TIp1CTmb7 > span > h1').text
        author = driver.find_element(By.CSS_SELECTOR, '#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.contentSpacing.NXiYChVp4Oydfxd7rT5r.RMDSGDMFrx8eXHpFphqG > div.RP2rRchy4i8TIp1CTmb7 > div > div > span > a').text
        author_link = driver.find_element(By.CSS_SELECTOR, '#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.contentSpacing.NXiYChVp4Oydfxd7rT5r.RMDSGDMFrx8eXHpFphqG > div.RP2rRchy4i8TIp1CTmb7 > div > div > span > a').get_attribute('href')
        print(name, author, author_link)
        three_dot = driver.find_element(By.CSS_SELECTOR, '.jO1u19LFzKZZJcoX4OdB > button:nth-child(3)')
        action.move_to_element(three_dot).perform()
        three_dot.click()
        time.sleep(0.5)
        share = driver.find_element(By.XPATH, '/html/body/div[15]/div/ul/li[2]')
        action.move_to_element(share).perform()
        time.sleep(0.3)
        embed = driver.find_element(By.XPATH, '/html/body/div[15]/div/ul/li[2]/div/ul/li[2]')
        action.move_to_element(embed).perform()
        embed.click()
        time.sleep(1.7)
        pre = driver.find_element(By.TAG_NAME, 'pre')
        iframe = pre.text
        try:
            if iframe in iframes:
                continue
            else:
                iframes[url] = [name, author, author_link, iframe]
        except:
            if iframes:
                create_all.all_iframe(path=name_of_path, name='iframes', datas=iframes)
                break
    except Exception as e:
        print('error on this url => {0}, reason => {1}'.format(url, e))

if iframes:
    create_all.all_iframe(path=name_of_path, name='iframes', datas=iframes)
