from selenium import webdriver
import time
mails=["mantanripper@hotmail.com","mantanripper1@hotmail.com","mantanripper2@hotmail.com","mantanripper3@hotmail.com","mantanripper4@hotmail.com","mantanripper5@hotmail.com","mantanripper6@hotmail.com","mantanripper7@hotmail.com","mantanripper8@hotmail.com","mantanripper9@hotmail.com"] #Add 10 emails within the quotes
users=["ardemsukiii","ardemsukiiia1","ardemsukiiin9","ardemsukiiik1","ardemsukiiin0","ardemsukiiin9","ardemsukiiin8","ardemsukiiis9","ardemsukiiis7","ardemsukiiis8"] #Add 10 usernames within the quotes
names=["demangan1","demangan2","demangan3","demangan4","demangan6","demangan5","demangan8","demangan9","demangan100","demangan1a"] #Add 10 names within the quotes
pas="zainal89100"
for x in range (0,len(mails)): 
browser=webdriver.Firefox()
browser.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(2)
email=browser.find_elements_by_class_name("_qy55y")[0]
name=browser.find_elements_by_class_name("_qy55y")[1]
username=browser.find_elements_by_class_name("_qy55y")[2]
password=browser.find_elements_by_class_name("_qy55y")[3]
email.send_keys(mails[x])
name.send_keys(names[x])
browser.execute_script("document.getElementsByClassName(\"_qy55y\")[2].value=\"\"")
username.send_keys(users[x])
password.send_keys(pas)
time.sleep(2)
browser.find_elements_by_class_name("_1on88")[1].click()
browser.quit()
