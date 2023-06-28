import undetected_chromedriver as uc
from bardapi import Bard
import speech_recognition as sr
from selenium.webdriver.chrome.options import Options
import time
import re
import pyttsx3
import os

os.environ["_BARD_API_KEY"] = "Xwj7LOMOK9nE2xBv72qYfQpfwhCVn4s1tCHLyIHWNoRLNjS_eHMutuEpGHfFj1bc43s3-A."

options = Options()
options.add_argument('--profile-directory=Profile 5')
options.add_argument('--user-data-dir=C:\\Users\\onkar\\AppData\\Local\\Google\\Chrome\\User Data\\')
driver = uc.Chrome(driver_executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("बोला पाटील काय सेवा करु ")
    audio = r.listen(source)


m = r.recognize_google(audio)
print(m)
#this m is the promt that will give us output
message = f"hi my name is onkar ,{m} "

k = str((Bard().get_answer(str(message))))
#Here we will be selecting the movie keywords only
movie_list = re.findall(r"\*\*\s*(.*?)\s*\*\*", k)

result = []
[result.append(x) for x in movie_list if x not in result]
print(result)
text_speach = pyttsx3.init()
print(k)

p = []
for i in range(len(result)):
    #here we will be updating the query for the chrome driver
    p.append("https://drive.google.com/drive/u/0/search?q=" + f"{result[i]}")
print(p)

for j in p:
    driver.execute_script(f'window.open("{j}","_blank");')


text_speach.say(k)

text_speach.runAndWait()
time.sleep(500)
