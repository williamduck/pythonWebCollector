import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# Create new Selenium driver
driver = webdriver.PhantomJS(executable_path='E:\Program Files (x86)\phantomjs-2.1.1-windows\\bin\phantomjs.exe')

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# Click the preview button
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# Wait for the page loading finish
time.sleep(5)
# Click on the right arrow, to right turn the page.
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # Get the loaded page.
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# Tesseract processing the loaded images.
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())

