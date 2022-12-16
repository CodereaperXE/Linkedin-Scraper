#Built by Rishab Budale 
from selenium import webdriver
from selenium.webdriver.common.by import By	
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver=webdriver.Firefox()#open firefox


username="username_here"
password="password_here"
search_query="company name"
search_get="https://www.linkedin.com/company/company_name/about/"

def write_file(name,content):
	with open(name,'wb') as text:
		text.write(content.encode())
		text.close()

def login(username,password):
	driver.get("https://linkedin.com")#go to linkedin
	time.sleep(1)
	driver.find_element(By.NAME,"session_key").send_keys(username)#username enter
	driver.find_element(By.NAME,"session_password").send_keys(password)#password enter
	driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()#click signin

def remove_message_popup():
	driver.execute_script("""var l = document.getElementsByClassName("msg-overlay-list-bubble ml4")[0];l.parentNode.removeChild(l); """)#delete message_popup

def search_by_query(search_query):
	search=driver.find_element(By.XPATH,"/html/body/div[5]/header/div/div/div/div[1]/input")#find search_box
	search.click()#click search_box
	search.send_keys(search_query)#search query
	time.sleep(1)
	search.send_keys(Keys.ENTER)#press enter

def search_by_GET(search_query):
	driver.get(search_query)

def search_by_GET_and_download(search_query):
	driver.get(search_query)
	time.sleep(3)
	return driver.page_source

def captcha_check():
	while(1):
		v=int(input("enter 1 after completing captcha "))
		if(v==1):
			break
	time.sleep(2)


#write content
def write_about(about_link):
	content=search_by_GET_and_download(about_link)
	write_file('linked_about.html',content)
	fp=open('linked_about.html')
	content=BeautifulSoup(fp,'html.parser')
	content=content.find(class_='artdeco-card p5 mb4')#find text in about
	content=content.get_text()#get text
	content=content.replace('\n','')
	write_file("linked_about.txt",content)


def write_affiliated(about_link):
	content=search_by_GET_and_download(about_link)
	write_file('linked_about.html',content)
	fp=open('linked_about.html')
	content=BeautifulSoup(fp,'html.parser')
	content=content.find(class_='scaffold-layout__aside')
	content=content.get_text()
	content=content.replace('\n','')
	write_file('linked_affilitated.txt',content)
  
  #operation
try:
	login(username,password)
except:
	captcha_check()

time.sleep(2)
#search_by_query(search_query)
#time.sleep(2)
write_about(search_get)
time.sleep(2)
write_affiliated(search_get)

