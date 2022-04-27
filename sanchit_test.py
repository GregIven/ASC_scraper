from cgitb import html
from lib2to3.pgen2 import driver
from pickle import FALSE
import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-software-rasterizer")

page = requests.get("https://www.advancingsurgicalcare.com/asc/findanasc")
soup = BeautifulSoup(page.content, "html.parser")
state_id_elem = soup.find('select', {'id' : 'state'})
state_children = state_id_elem.findChildren(recursive=FALSE)
# print(state_children[1:])

driver = webdriver.Chrome()
driver.get("https://www.advancingsurgicalcare.com/asc/findanasc")

# dropdown = driver.find_elements(By.ID, value="state")
# time.sleep(5)
drop_down = driver.find_element(By.ID, value="headingTwo")

time.sleep(3)

drop_down.click()

time.sleep(3)

selectTag = Select(driver.find_element(By.ID, value="state"))

for stateTag in state_children:
    time.sleep(3)
    selectTag.select_by_value(stateTag['value'])

driver.close()
