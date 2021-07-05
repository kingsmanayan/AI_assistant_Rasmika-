import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser 
import os
import requests
from pprint import pprint
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
from subprocess import call
import pyautogui
from PIL import Image, ImageGrab
import time
import cv2
import numpy as np
import face_recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I an Rosmikha ........sir. please tell me how may I help you")  


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("you can talk......  Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Ayan said: { query}\n")    
    except Exception as e:
        print(e)

        print("say that again please...Ayan")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:    
        query = takeCommand().lower()
     

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Hello Ayan ....... According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")   
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/") 
        elif 'play old song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=ua4GW8uAOcw")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/") 
        elif 'play new song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=nNCWKja8oxw")
        elif 'play patriotic song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=neG3U7DD4vc")     
        elif 'play romantic song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=pNrtRmvfSvk") 
        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")    
        elif'play music' in query:
            music_dir = 'D:\\aastha'
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[0]))  
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open Microsoft Word' in query:
            codePath = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codePath)
        elif 'hi how are you' in query:
            speak("I am fine sir..... how can I help you?")
            print("I am fine sir..... how can I help you?")
        elif 'tell something about you' in query:
            speak("hi sir I am rosmikha..... I am AI assistant.... verson  2.0 ...  developers Ayan bag made me on july 26, 2020...in india")     
        elif 'something about you' in query:
            speak("hi sir I am rosmikha..... I am AI assistant.... verson  2.0 ...  developers Ayan bag made me on july 26, 2020...in india")        
        elif "today's date" in query:
            strTime = datetime.datetime.now().strftime("%D Year")
            speak(f"sir, the Date is {strTime}")
        elif 'what is the date and time' in query:
            strTime = datetime.datetime.now().strftime("%D year %H:%M:%S ")
            speak(f"sir, the Date and time is {strTime}") 
        elif 'what is the date' in query:
            strTime = datetime.datetime.now().strftime("%D year ")
            speak(f"sir, the Date and time is {strTime}")
        elif 'please sing national anthem' in query:
            speak("Everyone.... stood up ......the national ...anthem was.. about to.... begin.............. .....   ")
            music_dir = 'D:\\india'
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[0])) 
            print("Everyone stood up the national anthem was about to begin.............. .....   ")
        elif 'weather update' in query:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=kolkata&appid=e357d5e0e0d17040923513c4993cd3ad&units=metri'

            res = requests.get(url)

            data = res.json()

            temp = data['main']['temp']
            temp= temp-273.15
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']

            description = data['weather'][0]['description']

            print('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('pressure : {}'.format(pressure))
            print('humidity : {}'.format(humidity))
            print('Description : {}'.format(description))
            speak('Temperature : {} degree celcius'.format(temp))
            speak('Wind Speed : {} meter per second'.format(wind_speed))
            speak('Latitude : {}'.format(latitude))
            speak('Longitude : {}'.format(longitude))
            speak('pressure : {}'.format(pressure))
            speak('humidity : {}'.format(humidity))
            speak('Description : {}'.format(description))
        elif 'news update' in query:
            googlenews= GoogleNews()
            googlenews= GoogleNews('en','d')
            googlenews.search('india')
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            print(news)
            speak(news)
        elif 'sports update' in query:
            googlenews= GoogleNews()
            googlenews= GoogleNews('en','d')
            googlenews.search('sports')
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            print(news)
            speak(news)    
        elif 'technology update' in query:
            googlenews= GoogleNews()
            googlenews= GoogleNews('en','d')
            googlenews.search('Technology')
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            print(news)
            speak(news)
        elif 'covid-19 update' in query:
            googlenews= GoogleNews()
            googlenews= GoogleNews('en','d')
            googlenews.search('Covid-19 cases')
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            print(news)
            webbrowser.open("https://www.google.com/search?sxsrf=ALeKk01NXRRBHTS5Otja1G5YE2YIqfVZfA%3A1595916937730&ei=icIfX-eZLPOW4-EP18WgkAc&q=Google+new+covid-19+cases&oq=Google+Technology&gs_lcp=CgZwc3ktYWIQEjIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABg_6BJaABwBHgAgAEAiAEAkgEAmAEAoAEGqgEHZ3dzLXdpesABAQ&gs_ivs=1&sclient=psy-ab#tts=0&wptab=s:H4sIAAAAAAAAAONgVuLVT9c3NMwySk6OL8zJecTozS3w8sc9YSmnSWtOXmO04eIKzsgvd80rySypFNLjYoOyVLgEpVB1ajBI8XOhCvHsYuL2SE3MKckILkksKV7EKumen5-ek6qQl1qukJxflpmia2ipkJxYnFoMAOlc_w6JAAAA")
            speak(news) 
 
        elif 'google search' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            speak("Hello Ayan ....... According to google")
            webbrowser.open("https://www.google.com/search?q="+query)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        elif ' google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            speak("Hello Ayan ....... According to google")
            webbrowser.open("https://www.google.com/search?q="+query)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        elif 'youtube ' in query:
            speak('Searching youtube...')
            query = query.replace("youtube", "")
            speak("Hello Ayan ....... According to youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif'play mohun bagan song' in query:
            music_dir = 'D:\\mohan'
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[0])) 
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            print(results) 
        elif 'hai ' in query:
            query = query.replace("hai", "")
            speak('hi. ayan... how can I help you?')
        elif 'hi ' in query:
            query = query.replace("hi", "")
            speak('hi. ayan... how can I help you?')    
        elif 'play game' in query:
            webbrowser.open("https://chromedino.com/") 
            print("game start in  5 second")
            speak("game start in  5 second")
            def hit(key):
                pyautogui.keyDown(key)
            def isCollide(data):
                for i in range(488, 550):
                    for j in range(300, 330):
                        if data[i, j] < 100:
                            hit('up')
                            return True
                for i in range(485, 551):
                    for j in range(200, 300):
                        if data[i, j] < 100:
                            hit('down')
                            return True            
                return False

            def takeScreenshot():
                image = ImageGrab.grab().convert('L')
    
                return image    
            if __name__ == "__main__":
                time.sleep(5)
                hit('up')
                while True:
                    image = ImageGrab.grab().convert('L')
   
                    data = image.load()
                    isCollide(data)
        elif 'news' in query:
            speak('Searching news')
            query = query.replace("news", "")
            googlenews= GoogleNews()
            googlenews= GoogleNews('en','d')
            googlenews.search(query)
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            print(news)
            speak(news)
        elif 'face' in query: 
            speak('Face Recognition and Attendance system start within 1 minute..')
            speak('if you went to stop this system .. then plese press      q' )
            query = query.replace("face", "")
            path = 'known_faces'
            images = []
            classNames = []
            myList = os.listdir(path)
            print(myList)
            for cl in myList:
                curImg = cv2.imread(f'{path}/{cl}')
                images.append(curImg)
                classNames.append(os.path.splitext(cl)[0])
            print(classNames)
            
            def findEncodings(images):
                encodeList = []
                for img in images:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    encode = face_recognition.face_encodings(img)[0]
                    encodeList.append(encode)
                return encodeList
            def markAttendance(name):
                with open('Attend.csv','r+') as f:
                    myDataList = f.readlines()
                    nameList = []
                    for line in myDataList:
                        entry = line.split(',')
                        nameList.append(entry[0])
                    if name not in nameList:
                        now = datetime.datetime.now()
                        dtString = now.strftime('%H:%M:%S/%d-%m-%y')
                        f.writelines(f'\n{name},{dtString}') 

            encodeListKnown = findEncodings(images)
            print('Encoding Complete')
            
            cap = cv2.VideoCapture(0)
            
            while True:
                success, img = cap.read()

                imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            
                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
            
                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                    matchIndex = np.argmin(faceDis)
            
                    if matches[matchIndex]:
                        name = classNames[matchIndex].upper()
                        print(name)
                        speak(name)
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                        markAttendance(name)
                        
            
                cv2.imshow('Webcam',img)
                key=cv2.waitKey(1)
                if key == ord('q'):
                    speak("thank for using this system")
                    break
        elif 'object' in query: 
            speak('object and human detection system start within 1 minute..')
            speak('if you went to stop this system .. then plese press      q' )
            query = query.replace("object", "")  
            video = cv2.VideoCapture(0)

            car_tracker_file = 'cars.xml'

            pedestrian_tracker_file =('haarcascade_fullbody.xml')
            car_tracker = cv2.CascadeClassifier(car_tracker_file)
            pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)
            while True:
                (read_successful, frame) = video.read()
                if read_successful:
                    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                else:
                    break
                cars = car_tracker.detectMultiScale(grayscaled_frame)
                pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)
                for (x, y, w, h) in cars:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3 )
                for (x, y, w, h) in pedestrian:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3 )    
                cv2.imshow('car detection', frame)

                key=cv2.waitKey(1)
                if key == ord('q'):
                    speak("thank for using this system")
                    break                     
        elif 'vinod' in query: 
            speak('Finding   binod')
            query = query.replace("vinod", "")  
            def isBinod(filename):
                with open(filename, "r") as f:
                    fileContent = f.read()
                if "binod" in fileContent.lower():
                    return True
                else:
                    return False

            if __name__ == "__main__":
                dir_contents = os.listdir()
                nBinod = 0
                for item in dir_contents:
                    if item.endswith('txt'):
                        print(f"Detecting Binod in {item}")
                        speak(f"Detecting     Binod        in {item}")
                        flag = isBinod(item)
                        if(flag):
                            print(f"      binod found  in   {item} ")
                            speak(f"      binod    found   in   {item} ") 
                            nBinod +=1
                        else:
                            print(f"binod not found {item}")
                print("       binod decation summary     ")
                speak("       binod      decation s      ummary     ")
                print(f"{nBinod} file found with binod")
                speak(f"{nBinod} file      found      with     binod")                
                 
        else:
            print("thank you")              