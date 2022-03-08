# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:35:51 2021

@author: Kyle
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
"""while False:
    time.sleep(0.5)
    localtime = time.localtime(time.time())
    if  localtime.tm_hour==19 and localtime.tm_min==40:
        break"""

try:
    driver = webdriver.Chrome()
    driver.maximize_window()#放大視窗
    #driver.implicitly_wait(20)
    driver.get('*')
    #https://www.pcstore.com.tw/sapphiretech/M81063296.htm
    while True:
        #立即購買
        #buy_button=driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[3]/table/tbody/tr[11]/td/div[1]/a")
        try:
            buy_button=driver.find_element_by_xpath("//*[contains(text(),'立即購買')]")
            #buy_button_content=buy_button.get_attribute("href")
            buy_button.click()
            break
        except:
            driver.refresh()
        time.sleep(1)
    
    #選商品
            
    #登入
            
    account=driver.find_element_by_id("inpuid")
    account.clear
    account.send_keys("*") #帳號
    password=driver.find_element_by_name("userpass")
    password.clear
    password.send_keys("*")#密碼
    driver.find_element_by_xpath("//*[@id='container']/div[5]/table[2]/tbody/tr/td[1]/input").click()
    #登入

    #收貨人資料
    time.sleep(1)
    js = "document.getElementsByName('receiver')[0].value='*';"
    driver.execute_script(js)

    js = "document.getElementsByName('rectel')[0].value='*';"
    driver.execute_script(js)

    js = "document.getElementsByName('reczip')[0].value='*';"
    driver.execute_script(js)
 
    js = "document.getElementsByName('recaddress')[0].value='*';"
    driver.execute_script(js)
  
     #收貨人資料
    #訂購資料
    js = "document.getElementsByName('cust_name')[0].value='*';"
    driver.execute_script(js)

    js = "document.getElementsByName('cust_sex')[0].value='F';"
    driver.execute_script(js)
    
    js = "document.getElementsByName('cust_tel')[0].value='*';"
    driver.execute_script(js)

    js = "document.getElementsByName('invzip')[0].value='*';"
    driver.execute_script(js)
 
    js = "document.getElementsByName('invaddress')[0].value='*';"
    driver.execute_script(js)
  
    try:
        driver.find_element_by_xpath("//*[contains(text(),'發票需打統編請按此')]")
    except:
        js = "document.getElementsByName('osinvdonate')[1].click();"
        driver.execute_script(js)
    

    #訂購資料
    js="go_buyway('crd')"
    driver.execute_script(js)
   
            
    #信用卡資訊
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"cd01")))
    js="document.getElementById('cd01').value='****';"
    driver.execute_script(js)

    js="document.getElementById('cd02').value='****';"
    driver.execute_script(js)

    js="document.getElementById('cd03').value='****';"
    driver.execute_script(js)

    js="document.getElementById('cd04').value='****';"
    driver.execute_script(js)

    js="document.getElementById('expire_month').value='**';"
    driver.execute_script(js)

    js="document.getElementById('expire_year').value='****';"
    driver.execute_script(js)

    js="document.getElementById('cvv2no').value='***';"
    driver.execute_script(js)
    #certimg
    

    #信用卡資訊

    #驗證碼
    #驗證碼
                
    print("find")
except:
    print("no find")
    driver.close()
