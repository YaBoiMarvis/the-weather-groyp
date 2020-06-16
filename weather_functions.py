#**********LIBRARY TO EXTRACT WEATHER DATA FROM A GOOGLE SEARCH*******
# LOCATION IS DETERMINED BY GOOGLE USING IP ADDRESS
# 
#*********************MARVIS 140620***********************************



#**********INCLUDES***************************************************
#PUBLIC LIBRARIES
import requests 
from bs4 import BeautifulSoup as bs
#NON-PUBLIC LIBRARIES
#*********************************************************************



#**********FUNCTION TO DO GOOGLE WEATHER SEARCH AND SCRAP RESULTS*****
def get_weather(dictionary):
    
    #SET URL + LOCATION
    url = "https://www.google.com/search?r=lang_en&ie_UTF-8&q=weather"
    
    #CREATE A SESSION AND SET USER AGENT/LANGUAGE TO BROWSER
    #GOOGLE TRIES TO STOP WEB SCRAPPING ON THEIR PAGES (LOL)
    #SEND REQUEST AS BROWSER
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    #CONNECT TO URL AND STORE DATA (HTML)
    html = session.get(url)

    #CREATE SOUP TO PARSE
    soup = bs(html.text, "html.parser")
    
    #PARSE OUT WEATHER DATA
    dictionary['location'] = soup.find("div", attrs={"id": "wob_loc"}).text
    dictionary['time'] = soup.find("div", attrs={"id": "wob_dts"}).text
    dictionary['weather'] = soup.find("span", attrs={"id": "wob_dc"}).text
    dictionary['temp'] = soup.find("span", attrs={"id": "wob_tm"}).text
    dictionary['precip'] = soup.find("span", attrs={"id": "wob_pp"}).text
    dictionary['humid'] = soup.find("span", attrs={"id": "wob_hm"}).text
    dictionary['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

    return
#**********************************************************************



#**********RELEASED TO GITHUB BY MARVIS 1601620**********************
#https://github.com/YaBoiMarvis/the-weather-groyp
#********************************************************************