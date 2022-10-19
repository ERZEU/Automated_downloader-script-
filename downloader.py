from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import httplib2


def downloader_img():
    month_int = datetime.date.today().month                     #получение номера месяца
    month_str = (datetime.date.today().strftime("%B")).lower()  #получение текущего месяца формата "june"
    year = datetime.date.today().strftime("%Y")                 #получение текущего года

    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    options.add_argument('--headless')
    url = f"https://www.smashingmagazine.com/{year}/0{month_int-1}/desktop-wallpaper-calendars-{month_str}-{year}/"
    driver = webdriver.Chrome(executable_path=r"C:\Users\Erzeu\Desktop\welp\chromedriver\chromedriver.exe", 
                              options=options)

    driver.get(url=url)
    kio = driver.find_elements(By.LINK_TEXT, "1366x768")

    for i in kio:
        url_img = i.get_attribute('href')
        title = i.get_attribute('title')

        h = httplib2.Http('.cache')    
        response, content = h.request(url_img)

        if (url_img.find('nocal') > -1):
            out = open(f'image_without_calendar\{title}.jpg','wb')
        else:
            out = open(f'image_with_calendar\{title}.jpg','wb')
        out.write(content)
        out.close()

    driver.close()
    driver.quit()
