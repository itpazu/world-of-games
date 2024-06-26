import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
def test_scores_service():
    driver.get('http://wog-app:5000')
    scores_elements = driver.find_elements(By.CSS_SELECTOR, 'body > section > div > ul > li > span')
    total_score = driver.find_element(By.CSS_SELECTOR, 'body > section > div > h2 > span')
    scores_elements.append(total_score)
    if not len(scores_elements) > 0 or not total_score:
        raise AssertionError('False')
    for element in scores_elements:
        int(element.text)
    driver.close()

def main():
    try:
        test_scores_service()
        return sys.exit(0)
    except (AssertionError, ValueError, NoSuchElementException) as error:
        print(error)
        return sys.exit(-1)

main()