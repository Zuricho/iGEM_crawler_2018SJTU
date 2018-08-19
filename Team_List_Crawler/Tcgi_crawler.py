#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:47:55 2018

@author: Zuricho
"""


# Before using, you should install "selenium". You can use "pip install selenium" to do this.
# Also, you should download and install chrome driver. You can follow the below link:
# http://blog.csdn.net/u012359618/article/details/52556127

# This is a crawler for crawing down iGEM2017 Judging forms
# The results are used for academic analyse as part of the Human Practice of team iGEM2018 SJTU-BioX-Shanghai
# If have any question please contact my github or by email: zbztzhz@sjtu.edu.cn

# You need to change the username and password before you use. The code is in line 33 and 37


from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


f_log = open("Teamcgi_crawler-log","w")

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

# The full list for iGEM teams starts from 0011 to 2900 (till 2018 iGEM)

for i in range(5,13):
    file_name = "Team_"+str(i)+".txt"
    f = open(file_name,"w")
    
    print(driver.title)

    try:
        URL = "http://igem.org/Team.cgi?team_id=" + str(i)
        driver.get(URL)
        driver.implicitly_wait(10)
        print(driver.title)
        if driver.title == "Team List For iGEM 2018 Championship":
            continue
        f.write(driver.title+'\n'+"Team Form No."+str(i))
        f.write("\n******\n")
    except:
        f_log.write("|open failed")

    try:
        # Write the team basic information
        element_teaminfo = driver.find_element_by_xpath("//TABLE[1]")
        f.write((element_teaminfo.text).encode('ascii','replace'))
        f.write("\n******\n")
    except:
        f_log.write("|form_1 failed")
        
    try:
        # Write the team medal requirements
        element_teamtrack = driver.find_element_by_xpath("//TABLE[8]")
        f.write((element_teamtrack.text).encode('ascii','replace'))
        f.write("\n******\n")
    except:
        f_log.write("|form_2 failed")
 
    try:
        # Write the team special prize information
        element_teamabs = driver.find_element_by_xpath("//TABLE[10]")
        f.write((element_teamabs.text).encode('ascii','replace'))
        f.write("\n******\n")
    except:
        f_log.write("|form_3 failed")

    try:
        # Write the team parts information
        element_teamteach = driver.find_element_by_xpath("//TABLE[12]")
        f.write((element_teamteach.text).encode('ascii','replace'))
        f.write("\n******\n")
    except:
        f_log.write("|form_4 failed")

    try:
        # Write the team parts information
        element_teamrost = driver.find_element_by_xpath("//TABLE[13]")
        f.write((element_teamrost.text).encode('ascii','replace'))
    except:
        f_log.write("|form_5 failed")
        
    f.close()

    driver.implicitly_wait(10)
    
    f_log.write("|No."+str(i)+" finished|\n")

driver.close()
