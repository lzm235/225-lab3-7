from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestH5Tag(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def test_h5_tag_content(self):
        driver = self.driver
        driver.get("http://10.48.229.158:8081")  # ✅ 确认这里地址正确！
        
        # 等待 h5 元素出现
        h5_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h5"))
        )
        h5_text = h5_element.text
        
        self.assertEqual(h5_text, "Lab 3-7 Works!", "The <h5> tag does not contain the expected text")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
