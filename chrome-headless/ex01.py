from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
url = "https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver"
driver.get(url)

sleep(5)
print(driver.get_screenshot_as_png());
# print(dir(driver));

exit(1);
h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
print(h1)
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# chromeOptions = Options()
# chromeOptions.headless = True
# browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chromeOptions)
# browser.get("https://www.google.com/")

# time.sleep(5);

# html = browser.find_element_by_xpath;
# print(html);
# nameList = browser.find_element_by_xpath('/html/body/div[1]/div[3]');
# # print(browser);
# # browser.find_elements_by_css_selector();
# nameList = browser.find_elements_by_css_selector('body > div.L3eUgb > div.o3j99.LLD4me.yr19Zb.LS8OJ > div')
# for name in nameList:
#   print(name.text)
# browser.quit()