import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import subprocess

import Config

options = webdriver.ChromeOptions()
options.add_argument(Config.chromeprofile)
driver = webdriver.Chrome(chrome_options=options, executable_path=Config.chromedriver)


def startassistant():
    subprocess.Popen(Config.modassistant)


def killassistant():
    subprocess.call(["taskkill", "/F", "/IM", "ModAssistant.exe"])


def setfilters():
    driver.find_element_by_xpath('')


def nextpage():
    return driver.find_element_by_xpath("//a[contains(@class, 'next')]").click()


def prevpage():
    driver.find_element_by_xpath("//a[contains(@class, 'prev')]").click()


def downloadpage():
    songs = driver.find_elements_by_xpath("//a[contains(@class, '-one-click')]")
    for song in songs:
        song.click()
        time.sleep(2)


def run():
    driver.get(Config.url)

    while len(driver.find_elements_by_xpath("//a[contains(@class, 'next')]")) is not 0:
        downloadpage()
        killassistant()
        nextpage()
        time.sleep(1)

    driver.close()

run()
