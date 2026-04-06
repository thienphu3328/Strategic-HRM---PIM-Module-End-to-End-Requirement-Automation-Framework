import logging


logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        logger.info(f"Navigate to URL: {url}")
        self.page.goto(url)
        
    def click(self, locator):
        logger.info(f"Click element: {locator}")
        self.page.locator(locator).click()
    
    def fill(self, locator, text):
        logger.info(f"Fill element: {locator} with value: {text}")
        self.page.locator(locator).fill(text)
  
    def get_text(self, locator):
        text = self.page.locator(locator).inner_text()
        logger.info(f"Get text from element: {locator}: {text}")
        return text
    
