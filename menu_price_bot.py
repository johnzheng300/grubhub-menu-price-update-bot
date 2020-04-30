from selenium import webdriver
from time import sleep

class MenuBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://restaurant.grubhub.com/')
        username = self.driver.find_element_by_xpath('//*[@id="appScrollContainer"]/div[1]/section/div/div[1]/div[1]/div/label/input')
        username.click()
        username.send_keys('username/email')
        password = self.driver.find_element_by_xpath('//*[@id="appScrollContainer"]/div[1]/section/div/div[1]/div[2]/div/div[1]/label/input')
        password.click()
        password.send_keys('password')
        login_btn = self.driver.find_element_by_xpath('//*[@id="appScrollContainer"]/div[1]/section/div/div[1]/button')
        login_btn.click()
    
    def get_to_menu(self):
        self.driver.find_element_by_xpath('//*[@id="reactRoot"]/div/div/div[1]/div/div[4]/div/div[1]').click()
   
    def change_price(self, price):
        price_input = self.driver.find_element_by_name('price')
        cur_price = price_input.get_attribute('value').replace('$', '')
        price_input.clear()
        new_price = str(round(float(cur_price) + price, 2))
        if (len(str(new_price))-str(new_price).index('.')-1) == 1:
            new_price = new_price + '0'
        price_input.send_keys(new_price)
        save_btn = self.driver.find_element_by_xpath('//*[@id="appScrollContainer"]/div[1]/div[3]/div/div/div[3]/div/div/div[2]/button')            
        save_btn.click()
    
    def get_categories(self):
        categories = self.driver.find_elements_by_class_name('menu-nav-list__link-name')
        return categories
    
    def get_items(self):
        items = self.driver.find_elements_by_css_selector('div.sc-bdVaJa.sc-bxivhb.fWfMYh')
        return items
    
    #update the prices of each item given a category
    def update_price(self, inc_price):
        # get menu items on each page
        items = self.get_items()
        for i in range(len(items)):
            print('Working on item', str(i+1)+'...')
            try:
                items[i].click()
                self.change_price(inc_price)
                sleep(2.5)
                items = self.get_items()
            except:
                print('waiting for server...')
                sleep(5)
                items[i].click()
                self.change_price(inc_price)
                sleep(2)
                items = self.get_items()
