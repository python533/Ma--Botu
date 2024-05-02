import pandas as pd
import requests
from bs4 import BeautifulSoup

file=open("Macyayınları.txt","w")


link=requests.get('https://www.sporx.com/tvdebugun/')
soup=BeautifulSoup(link.content,"html.parser")

kayitlar=soup.find_all("div",attrs={"class":"pg-left wide-682"})

for kayıt in kayitlar:
    print(kayıt)