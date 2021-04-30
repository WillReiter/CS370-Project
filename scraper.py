from bs4 import BeautifulSoup
from time import sleep
from flask import Flask
import requests

app = Flask(__name__)
@app.route('/')


def scrape():

    #****************   Weather *********************
    #Currently only pulling fort collins
    file = requests.get("https://weather.com/weather/today/l/40.59,-105.08?temp=f")
    #file = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN") 
    soup = BeautifulSoup(file.content, "html.parser")

    file1 = open("info.txt","w")

    # create empty list 
    list =[] 

    #temp, condition, percip values pulled using code blow
    temp = soup.find("span", attrs={"class": "CurrentConditions--tempValue--3KcTQ"}).text
    condition = soup.find("div", attrs={"class":"CurrentConditions--phraseValue--2xXSr"}).text
    #percip = soup.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"}).text
    temp = temp[:-1] #remove deg symbol

    print(f"temp= {temp}")
    print(f"condition= {condition}")
    #print(f"percipitiation= {percip}")

    file1.write(temp + ", ")
    file1.write(condition + ", ")
    #file1.write(percip + "\n")

    list.append(temp + ", ")
    list.append(condition + ", ")


    #****************   News *******************

    file = requests.get("https://www.bbc.com/news/world")
    soup = BeautifulSoup(file.content, "html.parser")

    headline = soup.find("h3", attrs = {"class" : "gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text"}).text

    print(f"headline= {headline}")
    file1.write(headline + ", ")
    list.append(headline + ", ")


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

    #download CSV link --> https://spotifycharts.com/regional/global/daily/latest/download
    url =  "https://www.billboard.com/charts/hot-100"
    file0 = requests.get(url)
    soup = BeautifulSoup(file0.text, "html.parser")
    songs = []
    artists = []
    songs = soup.find_all("span", {"class":"chart-element__information__song text--truncate color--primary"})
    artists = soup.find_all("span", {"class":"chart-element__information__artist text--truncate color--secondary"})
    s_count = 0
    a_count = 0
    for x in songs:
        if s_count >= 10:
            break
        s_count = s_count + 1
        print (x.text)
    for y in artists:
        if a_count >= 10:
            break
        a_count = a_count + 1
        print (y.text)
    counter = 0
    while(counter <= 10):
        file1.write(songs[counter].text)
        file1.write(" by ")
        file1.write(artists[counter].text)
        if(counter != 10):
            file1.write(", ")
        counter=counter + 1

    file1 = open("info.txt", "r")
    '''
    string = ""
    for y in list:
        string += y + " "
    '''
    return file1.read()



if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #scrape()

#run with  --> flask run --host=0.0.0.0