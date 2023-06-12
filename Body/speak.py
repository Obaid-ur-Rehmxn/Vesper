import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from gtts import gTTS
import playsound

def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    print("")
    print(f"Vesper: {text}")
    print("")
    engine.say(text)
    engine.runAndWait()

chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.headless = True
path="Database\\chromedriver.exe"
driver = webdriver.Chrome(path, options=chrome_options)
driver.maximize_window()

website=r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
buttonSelection=Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
buttonSelection.select_by_visible_text('US English / Matthew')

def Speak1(text):
    lengthofText=len(str(text))
    if lengthofText==0:
        pass

    else:
        print("")
        print(f"Vesper: {text}")
        print("")
        Data=str(text)
        xpathofsec='/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthofText>=30:
            sleep(4)
        
        elif lengthofText>=40:
            sleep(6)

        elif lengthofText>=55:
            sleep(8)

        elif lengthofText>=70:
            sleep(10)

        elif lengthofText>=100:
            sleep(13)

        elif lengthofText>=120:
            sleep(14)

        else:
            sleep(2)   

def Speak2(text):
    lengthofText=len(str(text))
    if lengthofText==0:
        pass

    else:
        print("")
        print(f"Vesper: {text}")
        print("")
        Data=str(text)
        tts = gTTS(Data, lang='en')
        tts.save("Database\\tts.mp3")
        playsound.playsound("Database\\tts.mp3")