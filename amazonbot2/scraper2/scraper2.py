import types
import typing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import os
from selenium.webdriver.common.keys import Keys as keys
import time 
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from prettytable import PrettyTable 
from scraper2.constants import link_list
import os
from selenium import webdriver
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class amazon(webdriver.Edge):  # Inherit from Edge WebDriver class
    def __init__(self, driver_path=r"C:\Users\Lenovo", teardown=False, headless=True) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        self.headless = headless
        chrome_options = webdriver.ChromeOptions()
        if self.headless:
            chrome_options.add_argument("--headless")
        os.environ['PATH'] += os.pathsep + self.driver_path
        super(amazon, self).__init__(options=chrome_options)
        self.implicitly_wait(3)
        self.maximize_window()
        
    def search_items(self):
        j = 0
        all_items_info = []
        for i in link_list:
            item_info = self.search_url(i)
            all_items_info.append(item_info)
            j += 1
        return all_items_info

    def search_url(self, item_link):
        flag=self.perform_search(item_link)
        if(flag==0):
             return [None]
        title= self.gettitle()
         
        # price = self.get_price()
        # seller_name = self.get_seller_name()
        # if(price== None and seller_name ==None):
            # return [None,None]
        x =[title]
        print(x)
        return [title]
    
    def perform_search(self, item_link):
        try:
            search_bar = self.get(f"https://www.amazon.in/d/{item_link}")
            time.sleep(0.2)
        except Exception as e:
            print("An error occurred:", str(e))# Return 0 to indicate error
            return 0  
    # def bulletpoints(self):
    #     try:
    #         # Wait for the bulletpoints element to be visible using XPath
    #         bulletpoints_element = WebDriverWait(self, 10).until(
    #             ec.visibility_of_element_located((By.XPATH, '//div[@id="feature-bullets"]//ul[@class="a-unordered-list a-vertical a-spacing-mini"]'))
    #         )
            
    #         bulletpoints_text = bulletpoints_element.text
    #         bulletpoints_list = bulletpoints_text.split('\n')
    #         # Ensure there are at least 7 bullet points
    #         while len(bulletpoints_list) < 7:
    #             bulletpoints_list.append("None")

    #         # Take only the first 7 bullet points
    #         bulletpoints_list = bulletpoints_list[:7]
    #     except (NoSuchElementException, TimeoutException):
    #         bulletpoints_list = ["None"] * 7  # Return a list of 7 "None" elements
    #     except Exception as e:
    #         print(f"An unexpected error occurred: {e}")
    #         bulletpoints_list = ["None"] * 7  # Return a list of 7 "None" elements
    #     return bulletpoints_list

    def gettitle(self):
        try:
            productTitle = WebDriverWait(self, 10).until(
                ec.visibility_of_element_located((By.ID, 'productTitle'))
            )
            productTitle=productTitle.get_attribute('innerText')
            return productTitle
        except Exception as e:
            print("An error occurred in get_merchant_info:", str(e))
            return None

    # def get_price(self):
    #     try:
    #         print("Attempting to find price element...")
    #         price_element = WebDriverWait(self, 5).until(
    #             ec.presence_of_element_located((By.XPATH, '//span[@class="a-price-whole"]'))
    #         )
    #         print("Price element found.")
    #         if price_element:
    #             price = price_element.text.strip()
    #             print("Price retrieved successfully:", price)
    #         else:
    #             price = None
    #             print("Price element found, but text retrieval failed.")

    #     except Exception as e:
    #         print(f"An error occurred while getting price: {e}")
    #         price = None

    #     return price
    # def get_seller_name(self):
    #     try:
    #         print("Attempting to find seller name element...")
    #         seller_name_element = WebDriverWait(self, 5).until(
    #             ec.presence_of_element_located((By.ID, 'sellerProfileTriggerId'))
    #         )
    #         print("Seller name element found.")
    #         if seller_name_element:
    #             seller_name = seller_name_element.text.strip()
    #             print("Seller name retrieved successfully:", seller_name)
    #         else:
    #             seller_name = None
    #             print("Seller name element found, but text retrieval failed.")

    #     except Exception as e:
    #         print(f"An error occurred while getting seller name: {e}")
    #         seller_name = None
    #     return seller_name
    
    # def mrp(self):
    #     try:
    #         print("Attempting to find price element...")
    #         # Wait for the price element to be present
    #         price_element = WebDriverWait(self, 10).until(
    #             ec.visibility_of_element_located((By.XPATH, '//span[@class="a-size-small a-color-secondary aok-align-center basisPrice"]'))
    #         )
    #         print("Price element found.")
            
    #         # Extract the text of the price element
    #         mrp_text = price_element.text.strip()
    #         print("Price retrieved successfully:", mrp_text)
            
    #         # Remove non-numeric characters and convert to integer
    #         mrp_numeric = int(''.join(filter(str.isdigit, mrp_text)))

    #     except Exception as e:
    #         print(f"An error occurred while getting price: {e}")
    #         mrp_numeric = None

    #     return mrp_numeric

    # def click_see_more_reviews(self):
    #     try:
    #         print("Attempting to find 'See more reviews' button...")
    #         see_more_reviews_button = WebDriverWait(self, 5).until(
    #             ec.visibility_of_element_located((By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]'))
    #         )
    #         print("'See more reviews' button found.")
            
    #         # Scroll to the button to ensure it's clickable
    #         self.execute_script("arguments[0].scrollIntoView(true);", see_more_reviews_button)
            
    #         see_more_reviews_button.click()
    #         print("Clicked on 'See more reviews' button.")

    #         review_count_element = WebDriverWait(self, 5).until(
    #             ec.visibility_of_element_located((By.XPATH, '//div[@data-hook="cr-filter-info-review-rating-count"]'))
    #         )
            
    #         # Extract the text of the review count element
    #         review_count_text = review_count_element.text.strip()
            
    #         # Extract and return the number of reviews
    #         review_count = review_count_text.split(',')[1].strip().split()[0]
    #         print("Total reviews:", review_count)

    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         review_count = None
        
    #     return review_count


    # def extract_rating_stars(driver):
    #     try:
    #         # Wait for the rating element to be present
    #         rating_element = WebDriverWait(driver, 10).until(
    #             ec.presence_of_element_located((By.XPATH, '//span[@data-hook="rating-out-of-text"]'))
    #         )

    #         # Extract the text containing the rating
    #         rating_text = rating_element.text

    #         # Extract only the numeric part (stars) from the rating text
    #         stars = rating_text.split()[0]

    #         print("Stars:", stars)
    #         return stars

    #     except Exception as e:
    #         print(f"An error occurred while extracting rating stars: {e}")
    #         return None