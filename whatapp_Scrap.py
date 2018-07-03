#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

import time

target = str(input('Enter name of person/group you want to target:'))

driver = webdriver.Firefox("/usr/local/bin/")
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'

person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

person_title.click()
x=-50
chat=[]
while x > -2000:
	element=driver.find_element_by_xpath("//div[@class='_9tCEa']")
	driver.execute_script("arguments[0].scrollIntoView(500);",element);
	x=x-100
	time.sleep(1)
textget=driver.find_elements_by_class_name("selectable-text.invisible-space.copyable-text")
print("Number of tweets extracted: {}.\n".format(len(textget)))
for Text in textget:
    chat.append(Text.text)
    print(Text.text)
while 1 :
	quit=input("Press q for logout : ")
	if quit == 'q':
		menu=driver.find_elements_by_class_name("rAUz7")
		menu[2].click()
		list=driver.find_elements_by_class_name("_10anr.vidHz._28zBA")
		list[5].click()
		break

a=len(chat)
b=int(a/2)
data=chat[b:a]
print(data)

nltk.download('vader_lexicon')   
sid = SentimentIntensityAnalyzer()
neg=0
neu=0
pos=0
compound=0
for sentence in data:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    neg = neg+ float(ss['neg'])
    neu =  neu +float(ss['neu']) 
    pos = pos + float(ss['pos'])
    compound = compound+float(ss['compound'])
    print(ss)
    print(neg,"   ",neu,"   ",pos,"   ",compound)
 
total=neg+neu+pos+compound
print("negative =  ",(neg/total)*100,"%")
print("neutral =  ",(neu/total)*100,"%")
print("positive =  ",(pos/total)*100,"%")
print("compound =  ",(compound/total)*100,"%")
