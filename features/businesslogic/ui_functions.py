import os,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from features.businesslogic.locators import coinmarketcapLocators as commonlocators

from features.businesslogic.Authentication import ValidateAuthentication
obj_ValidateAuthentication = ValidateAuthentication()


class ValidateUIElements:
    def __init__(self):
        s = Service(executable_path=self.get_chrome_driver())
        self.driver = webdriver.Chrome(service=s)

    def get_chrome_driver(self):
        """
        Description:
            |  This method fetches the path of chrome driver
        """
        try:
            return os.getcwd() + os.sep + "browsers" + os.sep + "chromedriver.exe"
        except Exception as e:
            print("Error in get_chrome_driver method-->" + str(e))

    def navigate(self,pstr_url):
        """
        Description:
        |  This method navigates the user to the provided url
        """
        try:
            self.driver.get(pstr_url)
            self.driver.maximize_window()
            self.driver.find_element(By.XPATH, commonlocators.str_cookie_banner).click()
        except Exception as e:
            print("Error in navigate method-->" + str(e))

    def click_dropdown(self):
        """
        Description:
        |  This method performs click on the provided dropdown
        """
        try:
            self.driver.execute_script("window.scrollTo(0, 100)")
            dropdown_element = self.driver.find_elements(By.XPATH, commonlocators.str_showrows_dropdown)[0]
            dropdown_element.click()
            self.driver.find_elements(By.XPATH, commonlocators.str_100_value_selection)[0].click()
        except Exception as e:
            print("Error in click_dropdown method-->" + str(e))

    def click_filter(self,pstr_Filters):
        """
        Description:
        |  This method performs click on the provided filters
        """
        try:

            self.driver.execute_script("window.scrollTo(0, 100)")
            if pstr_Filters == 'Filters':
                self.driver.find_elements(By.XPATH, "(//button[text()='" + pstr_Filters +"'])")[1].click()
            if pstr_Filters == 'More Filters':
                button = self.driver.find_element(By.XPATH, commonlocators.str_More_Filters_button)
                time.sleep(5)
                button = self.driver.find_element(By.XPATH, commonlocators.str_More_Filters_button)
                button.click()
            if pstr_Filters == 'Show results':
                self.driver.find_element(By.XPATH, commonlocators.str_show_results_button).click()
        except Exception as e:
            print("Error in click_filter method-->" + str(e))

    def count_table_rows(self,pstr_rows):
        """
        Description:
        |  This method validates the counts of the list/rows
        """
        try:
            rows = len(self.driver.find_elements(By.XPATH,"(//table/tbody/tr)"))
            if int(rows) == int(pstr_rows):
                return True
            else:
                return False
        except Exception as e:
            print("Error in count_table_rows method-->" + str(e))

    def select_Filter_values(self,pstr_filter,pstr_value):
        """
        Description:
        |  This method sets the values in the filter section
        """
        try:
            self.driver.find_element(By.XPATH, "(//button[text()='"+ pstr_filter +"'])").click()
            self.driver.find_element(By.XPATH, "(//button[text()='" + pstr_value + "'])").click()
            self.driver.find_element(By.XPATH, commonlocators.str_apply_filter_button).click()
        except Exception as e:
            print("Error in select_Filter_values method-->" + str(e))

    def validate_filter_results(self):
        """
       Description:
       |  This method validates the grid with respect to applied filter criteria
       """
        try:
            list_price = self.driver.find_elements(By.XPATH,"(//table/tbody/tr/td/div[@class='sc-131di3y-0 cLgOOr'])")
            for line in list_price:
                if (line.text < "$101" and line.text > "$1000") == True:
                    return False
            list_MarketCap = self.driver.find_elements(By.XPATH,"(//table/tbody/tr/td/p/span[@class='sc-1ow4cwt-1 ieFnWP'])")
            for line in list_MarketCap:
                if (line.text < "$1000000000" and line.text > "$10000000000") == True:
                    return False
            return True
        except Exception as e:
            print("Error in validate_filter_results method-->" + str(e))