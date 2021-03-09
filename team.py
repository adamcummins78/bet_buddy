from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'C:/chromedriver/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.sports-reference.com/cfb/schools/georgia/2020.html")
# print(driver.page_source)
# driver.quit()

elements = driver.find_elements_by_xpath("//td[@data-stat='opp_tot_yds']")
for element in elements:
    print(element.text)
