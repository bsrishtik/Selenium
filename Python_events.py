from selenium import webdriver

path = "/Users/srishtik/Downloads/chromedriver"

driver = webdriver.Chrome(executable_path= path)

driver.get("https://www.python.org/")

time = driver.find_elements_by_css_selector('.event-widget time')

time_list = [ele.text for ele in time]

events = driver.find_elements_by_css_selector(".event-widget li a")
event_list = [ele.text for ele in events]

info = {}

for i in range(len(time_list)):
    info.update({i:{time_list[i]:event_list[i]}})

print(info)
driver.quit()