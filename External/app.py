from flask import Flask, render_template
import requests as req
import os
import datetime
# -*- coding: utf-8 -*-


WEATHER_FOLDER = os.path.join('static', 'weather_images')
#while (True): # constant loop
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = WEATHER_FOLDER
@app.route('/')
def index():
    file1 = open('response.txt','w')
    x = req.get("http://10.0.0.248:5000/") #this may change depending on the IP of PC running scraper code
    #string = x.text[2:]
    #string = string[:-3]
    string = x.text
    list = string.split(', ')
    print(list)

    now = datetime.datetime.now()
    

    if(list[1].find("Mostly") != -1):
        if(list[1].find("Sunny") != -1):
            weather_image = "weather_images/partly_cloudy.png"
        elif(list[1].find("Cloudy") != -1):
            weather_image = "weather_images/partly_cloudy.png"
        else:
            weather_image = "blank.png"

    elif(list[1].find("Partly") != -1):
        if(list[1].find("Cloudy") != -1):
            weather_image = "partly_cloudy.png"
    
    elif(list[1].find("Snow")!= -1):
        weather_image = "snow.png"
    
    elif(list[1].find("Thunderstorms")!= -1):
        weather_image = "storm.png"
    
    elif(list[1].find("Sunny")!= -1):
        weather_image = "sunny.png"
        print("CORRECT\n" + weather_image)

    elif(list[1].find("Cloudy")!= -1):
        weather_image = "cloudy.png"

    elif(list[1].find("Clear")!= -1):
        weather_image = "clear.png"

    elif(list[1].find("Rain")!= -1):
        weather_image = "rain.png"

    elif(list[1].find("Fair")!= -1):
        weather_image = "partly_cloudy.png"

    else:
        weather_image = "blank.png"

    bg_img_list = ["https://lh3.googleusercontent.com/proxy/eVZ21qircGexyTjOGYwmSN5jByPVBRcG0v7GQKviDGw_9op-mcpEa3HTr0hY8QVDigOn19IAL4ovyr0jzRXkZ6tTTayyyiMG0e1vdu0kLIAkddhyuGvf0iMLA6AflPYdrge30cMnzR1e4sRccnba4-8v4Atf0D1KOILS9so6eD6HF2vqox9O59vT_lbq3f6kC544l6FfT7R4cP8f5cXDfzVOsIBq8kTG27VdMXQcyUoT0QmqDPmquHLSNVhjoImIP67n2IpFg00JTJy8LQ=s2560-w2560-h1440-fcrop64=1,0000170afffffd6f-k-no-nd-mv",
    "https://lh6.googleusercontent.com/proxy/rBQOuf7xnHenT38uC_AY8jlRqxstbxYfONBsiX7NG84f3FFywliqC89gRsVIPoNCzPrVqrRgNTn5atJL23798IaR5Gnh0KbLGMdxCG2JKmyGLr3LTMSsFDZSPS1C7EMPMNUhyt4mgGWKWcDNvELObIi1JCN_qI4vKRqlIPDdrFgFlwtH0HFcDeTWlsL7ENSGwi4bdf3O7cYHd0wdNmrM0Ms9TrP_WJ2OPZob-fEmijqfly6cNY8I-IMaJlfZHDB67F4=s1920-w1920-h1200-fcrop64=1,00001999fffff3c7-k-no-nd-mv",
    "https://lh3.googleusercontent.com/proxy/t-_q1wdQGdjvSfTw9kvNC4jWzThbpUTPcSgyf1CKCHLAH493zCaKhDqke3a2S5AQLecRO6Fi0rM19LmAWxfy47mSNdLqVJi3w78b_Kuv0GlW4wUAAUxYQJBa0lMOXhLSLEbKTlXNypRck70JjmVzQxEvla6OejNelo6Y1vcMyyO--s9umYddjr-fVQQT2rnRkJZzSh3_PDpqY2j_gF4lcMT3jv3xXzIRQxD1gL3welSZhXCEZ-RKE802wCrKMJw7HQ=s1920-w1920-h1200-fcrop64=1,000023d6fffffe04-k-no-nd-mv",
    "https://lh5.googleusercontent.com/proxy/aj67cLMQ-Ybx3DUKTiUAQd_ilyatWpdT0V5KZ6n_7jJEKZ1KC-0I87d9yvpe3ro2KpAP2v485eBaVyeiicitrseOwZxfORqddFjt8Gw0bEC6TJso91ISWXrNBdlmkQt555cXrRWh7tgPajwYD5G8ZzHfmrBjo8uUnPSRAKxfhUSDjFmoxx7g4cO_RNqo0GdTEna5QDehEhI-xi2dvRdilL8QuWO-oKWTR78XoKSu7qGqttisAM3xiPNWEqbJkpxM-VTggN5rnJ_6=s1920-w1920-h1200-fcrop64=1,00001999fffff3c7-k-no-nd-mv",
    "https://lh6.googleusercontent.com/proxy/MVSgkRcC3Dd_XGw3lXaniWBL1qsnRYCBTGUUA2yHoXxtT7xrKAx8d1ly6USTJdcie-wqQg_10gn2PhNGRhozB5FkAu8qK_YeSoOb8Hj3eKWnr6-hO6kL8t9uPN6sIBdM3Ar5uQEfTCX45lrO5E0vY7i57CFfIXB6_EwswJUmsD-NhrNJPGLh4ld6aCwbZpCNgC0I57lykESvpe21CdfnNQ=s1920-w1920-h1200-p-k-no-nd-mv", 
    "https://lh4.googleusercontent.com/proxy/LOUNUIJlgEaGnhruqzmnhK40uaFKvebv2uTp208y9bndE8KCvIKAPov8_1B_61XKQ85Yl_WINpg0_D4R4eVrU_WPQ7YxtuTvKFrvQBP7b_LVtXfBd2hZOfKAhRQHuf3yrtBpUBWm8FvdbdRnjuGk6GbHfVUbkpIDseZboOOW8NUlI36fRut5NgEFzTErpCMxDADwlB4cLO8tiDfDe0sjDmk2-cPUk9JDPFf9mXtGrCEKb-M-77rGwZGQ1g=s1920-w1920-h1200-p-k-no-nd-mv",
    "https://lh3.googleusercontent.com/proxy/jKYxpPNQAF7V7p0QHb7g3us2BP0vY3sXdoQPj2R1COideMrl_mWWw7z2_ykHn3YCPYVNmqoITJXQ9z9RMQkZIVqVSfrCV2pWLVEf1qSiw9iW7pf1demP2k4e4WSDZe-nCeV1el_Xr7VO3HsG6BSy88Ze5kLr1JzLbgiXBRScyGBzTFLX6d_NPfPDNfQQNBdfRgpIW3NpHdWF0-4CQvFApTsUCGjX2QGQmGsxkz4AaFzG2lvft_MWa9zaEA=s1920-w1920-h1200-p-k-no-nd-mv",
    "https://lh5.googleusercontent.com/proxy/zJc9lcwMHkKSDgfdVr3VtcgjR3FJBMHQKdigk20i4B_h9b8mMoKuAHhLaqWNSxXnAbywDEGwalTdoytXUfiNtVwsaeVC4UfnsHuELq_R85DdAk930Q99CE0C=s1920-w1920-h1200-p-k-no-nd-mv",
    "https://lh6.googleusercontent.com/proxy/J94fUVlHnBo-S3o2COUQWFawij2AR8dky7GRguWkwVYWfp--el9dV5YIHeG8NkJyjETBCWdUwQ3g5Cp8mRGxdmd5JIETRc1BuftYMS0HGdEji_c97MiPhPVqpMfm78QexGYKWE-fe6LAycWcptMIzEnn_QN50eKQ62jlAsMTr2fzBZXCYqDD840rPJ-UvdNdaPQD-ANrY2dOWfnITZbABsHrnAX1tCTTD4HJZpxJmR-w-AkiRxa0mD_l7Oe4TpHAUU-QtXEvNAYF=s1920-w1920-h1200-p-k-no-nd-mv",
    "https://lh6.googleusercontent.com/proxy/0PEAQM_IB0AGxstPkB-fzxwP5PVq4uLBu17nBulNEJWdZJU9O3_L7HwP2kXRVC60GU8J75Y9vTIW93WXUEAnU50Xqky3AmCDEW4GThqSjeJS5nkma-1oFmk0nvzdcH45_mIH3NOjgr8REKxCBqA0Qgr3stsBLlXCnfWDk7l7V07OQg-earOgWDp5AxASV3s6T38WRc3JiWN6h2oEOGS3bTSTmtmOR8iEdYxFT6AwumON34nOW0WTK7AvgF0J2BZHUWVr9s-pSc7pMGG3qBeBsaKrnRA=s1920-w1920-h1200-fcrop64=1,000030a3ffffe4a2-k-no-nd-mv",
    "https://lh4.googleusercontent.com/proxy/5Dk06F0gvha6245-PeXi6i9VnTjyeAazuVwvneVuk2HIZEQgAeil5hpkoE-nKBfDTNgepbO00DtmjKCskiTKqxiSNscrZ3wCHJiwiXFGepM8IjuaagjPYjFJ9n5GLHCYjhKL99wcJUV5kWoIvG2hUfijbzoItOQjHZqzkqXLe8nCKNBL_cvWWfv-HRxYcRcqC29jAhq1rw6zXd6CV8m49v43teyN0HGA36zJifSbK3YwfukEgua2tTg=s1920-w1920-h1200-fcrop64=1,00001999fffff3c7-k-no-nd-mv",
    "https://lh5.googleusercontent.com/proxy/0KC6oxopZVaSCYzFZn2j4bNnIsldrZ9Xdd39e3xaM_7k36IYhVpYSbIXz0JKKj3Ro9OjlLvJbEuazY8nbZpL4W5HJO7iL_Uq_Ie0_JCZVJWQNKtH6EPXx5YUWv540JfB9YlEFYFDph0OO4jheiI1loP7TKHhsJdU2Nuq_tYIDo9Ehj5sfY9_CQ1p2NzyS5xkCnX52UofLSGmW3MTnVL-1E8_c2yZTYJjby9fbxCHXqT_=s1920-w1920-h1200-fcrop64=1,000023d6fffffe04-k-no-nd-mv"]
    
    
    temperature = list[0] + "° F"
    cond = list[1]
    hdline = list[2]


    print(str(int(now.strftime('%I'))))

    musicList = []
    i = 0
    musicStr = ""
    while(i < 10):
        musicStr += list[i+3] + "\n"
        i = i + 1

    file1.write("Current Temperature is " + list[0] + "° F" + "\n")
    file1.write("Current Condition is " + list[1] + "\n")
    file1.write("Todays Headline: " + list[2] + "\n")
    result = ("\n" + "Current Temperature is " + list[0] + "° F" + "\n" + 
            "\n" + "Current Condition is " + list[1] + "\n" + 
            "\n" "Todays Headline: " + list[2] + "\n")
    
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], weather_image)
    print("full filename: " + full_filename)
    
    with open('response.txt', 'r') as f: 
        #if(sensor):
        return render_template('index.html', text=result, user_image = full_filename, date = now.strftime('%A, %B %dth %Y'), time= now.strftime('%I:%M'), temp=temperature, condition=cond, headline=hdline, music = musicStr, bgi= bg_img_list[int(now.strftime('%I'))])
        #else:
            #return render_template('inactive.html')
        
    file1.close()
    #wait(100) # every 100s
