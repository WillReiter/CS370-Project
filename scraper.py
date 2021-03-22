from bs4 import BeautifulSoup

import requests


#****************   Weather *********************
#Currently only pulling fort collins
file = requests.get("https://weather.com/weather/today/l/bf4dfbdf5c25eebacf57cc23a0f1561ae0604737bd0c64b1c960dd741a1fb29e")
#file = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN") 
soup = BeautifulSoup(file.content, "html.parser")



# create empty list 
list =[] 

#temp, condition, percip values pulled using code blow
temp = soup.find("span", attrs={"class": "CurrentConditions--tempValue--3KcTQ"}).text
condition = soup.find("div", attrs={"class":"CurrentConditions--phraseValue--2xXSr"}).text
percip = soup.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"}).text
   
print(f"temp= {temp}")
print(f"condition= {condition}")
print(f"percipitiation= {percip}")

list.append(temp)
list.append(condition)


#****************   News *******************

file = requests.get("https://www.bbc.com/news/world")
soup = BeautifulSoup(file.content, "html.parser")

headline = soup.find("h3", attrs = {"class" : "gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text"}).text

print(f"headline= {headline}")


#************** Spotify *****************\

class Music:
    def __init__(self, position, title, artist, streams):
        self.position = position
        self.title = title
        self.artist = artist
        self.streams = streams
    def __repr__(self):
        return "pos= %s title= %s artist= %s streams= %s" % (self.position, self.title, self.artist, self.streams)

    
musicList = []
tempList = []
#music list:
    #[0] = position
#position = ""
    #[1] = Title and Artists
#title = ""
#artist = ""
    #[2] = Streams
#streams = ""


file = requests.get("https://spotifycharts.com/regional/us/daily/latest")
soup = BeautifulSoup(file.content, "html.parser")

table = soup.find("table", attrs= { "class" : "chart-table" })
table_body = table.find('tbody')
rows = table_body.find_all('tr')
counter = 0
for row in rows:
    if(counter == 10): #only get top 10
        break
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    tempList.append([ele for ele in cols if ele]) # Get rid of empty values
    counter = counter + 1 
for elem in tempList:
    position = elem[0]
    title = elem[1].split("\n")[0]
    artist = elem[1].split("\n")[1]
    streams = elem[2]
    m1 = Music(position,title,artist,streams)
    musicList.append(m1)
for x in musicList:
    print(x.title)

