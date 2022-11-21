from time import sleep
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from cookies.py import cookies
chrome_options = Options()
chrome_options.add_argument("--headless")
import json

with open ('cookies.json', 'r') as myfile:
 data=myfile.read()

fruit_detail = json.loads(data)
# print(data);
driver = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chrome_options)
# driver.set_window_size(1853, 1240);
driver.maximize_window();
url = "https://www.instagram.com/explore/tags/germany/"
driver.get(url)

sleep(10);
# test = driver.get_screenshot_as_file('foo1.png');
# print(driver.page_source);

Button = driver.find_element(By.CLASS_NAME,"_a9-- _a9_0");
sleep(3);
print(Button);

for cookie in fruit_detail:
    driver.add_cookie(cookie)

driver.refresh();

# sleep(10);
# print(cookies);
# element = driver.find_element("CLASS_NAME", "x1n2onr6 x6s0dn4 x78zum5")
# element.click();
# driver.fin
sleep(30);
# print(dir(driver));
test = driver.get_screenshot_as_file('foo.png');

# url = "https://www.instagram.com/explore/tags/germany/"
# driver.get(url)
# sleep(4);
# test = driver.get_screenshot_as_file('foo.png');
# test.contains();
# test.save_screenshot('screen.png');
# print(dir(driver));
driver.quit();

exit(1);
h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
print(h1)

# browser.quit()