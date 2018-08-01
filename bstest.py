#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import simpledialog
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

root = Tk()
w = Label(root, text="Program")
w.pack()
name = simpledialog.askstring("Name", "Insert Name")
print (name)

imdb = "http://www.imdb.com/" #url
im_search = "navbar-query" #search bar
im_person = '//*[@id="navbar-suggestionsearch"]/a[1]' #1st person on dropdown
im_pics = "Photo Gallery" #photo gallery link
im_imgs = '//*[@id="media_index_thumbnail_grid"]/a[1]/img' #1st image of the grid
im_next = '//*[@id="photo-container"]/div/div[2]/div/div[2]/div[2]/button[2]' #next arrow
im_lp_cnt = '//*[@id="name-overview-widget"]/div/div[2]/a[2]' #loop counter based on number of photos
im_dwn = '//*[@id="photo-container"]/div/div[2]/div/div[2]/div[1]/div[2]/div/img' #picture to save

fake = Faker()
rnd = fake.name() #save files name randomizer
b = webdriver.Chrome()

b.get(imdb)
b.find_element_by_id(im_search).send_keys(name)
time.sleep(1)
b.find_element_by_xpath(im_person).click()
ls = b.find_element_by_xpath(im_lp_cnt).text
loop = int(re.search(r'\d+', ls).group())
b.find_element_by_partial_link_text(im_pics).click()
b.find_element_by_xpath(im_imgs).click()

for x in range(loop):
    time.sleep(1)
    img = b.find_element_by_xpath(im_dwn)
    src = img.get_attribute('src')
    b.get(src)
    time.sleep(1)
    rnd = time.strftime("%Y%m%d-%H%M%S")
    b.save_screenshot('screenshot-' + rnd + ".png")
    print(f'should have saved a file called: {"screenshot-" + rnd + ".png"}')
    time.sleep(1)
    b.back()
    time.sleep(1)
    b.find_element_by_xpath(im_next).click()
    time.sleep(1)
if x == loop:
        w.close()