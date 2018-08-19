#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:47:55 2018

@author: Zuricho
"""

"""
Before using, you should install "selenium". You can use "pip install selenium" to do this.
Also, you should download and install chrome driver. You can follow the below link:
http://blog.csdn.net/u012359618/article/details/52556127

This is a crawler for crawing down iGEM2017 Judging forms
The results are used for academic analyse as part of the Human Practice of team iGEM2018 SJTU-BioX-Shanghai
If have any question please contact my github or by email: zbztzhz@sjtu.edu.cn
"""

# You need to change the username and password before you use. The code is in line 33 and 37

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f_log = open("JForm_crawler-log","w")

driver = webdriver.Chrome()
driver.get("https://igem.org/Login2")

element_usr = driver.find_element_by_name("username")
element_usr.clear()
element_usr.send_keys("USERNAME")

element_psw = driver.find_element_by_name("password")
element_psw.clear()
element_psw.send_keys("PASSWORD")
element_psw.send_keys(Keys.RETURN)

driver.implicitly_wait(50)

# 2017 Judging Form starts from 2190 to 2528

for i in range(2190,2195):
    file_name = "Team.cgi_"+str(i)+".txt"
    f = open(file_name,"w")
    try:
        URL = "http://igem.org/2017_Judging_Form?id=" + str(i)
        driver.get(URL)
        driver.implicitly_wait(10)
        f.write("Judging Form\nNo."+str(i)+'\n\n')
    except:
        f_log.write("|open failed")

    try:
        # Write the team basic information
        element_teaminfo = driver.find_element_by_xpath("//TABLE[1]")
        f.write((element_teaminfo.text).encode('ascii','replace'))
        f.write("\n\n******\n\n")
    except:
        f_log.write("|form_1 failed")
        
    try:
        # Write the team medal requirements
        element_teammedal = driver.find_element_by_xpath("//TABLE[2]")
        f.write((element_teammedal.text).encode('ascii','replace'))
        f.write("\n\n******\n\n")
    except:
        f_log.write("|form_2 failed")
 
    try:
        # Write the team special prize information
        element_teamprize = driver.find_element_by_xpath("//TABLE[3]")
        f.write((element_teamprize.text).encode('ascii','replace'))
        f.write("\n\n******\n\n")
    except:
        f_log.write("|form_3 failed")

    try:
        # Write the team parts information
        element_teampart = driver.find_element_by_xpath("//TABLE[4]")
        f.write((element_teampart.text).encode('ascii','replace'))
    except:
        f_log.write("|form_4 failed")
 
    f.close()

    driver.implicitly_wait(10)
    
    f_log.write("|No."+str(i)+" finished|\n")

driver.close()
