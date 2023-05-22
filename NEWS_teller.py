import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
 #while True:
       speak("WHICH NEWS WOULD YOU LIKE ME TO TELL NATIONAL OR INTERNATIONAL")
       print("which news would you like me to tell?")
       speak("type N for National news or type I for International news")

       print("Enter N for NATIONAL\nEnter I FOR INTERNATIONAl") #\nENTER P TO PAUSE NEWS\nENTER R TO RESUME NEWS\nENTER E TO EXIT NEWS TELLER")
       _input = input()

       if _input == ("N"):
            speak(" NationalNews for today are as follows")
            speak("This news is brought to you by NDTV News")
            url1 = "https://newsapi.org/v2/top-headlines?country=in&apiKey=6aaf3b20b83b426592cf46e65dfa8571"
            news = requests.get(url1).text
            news_py = json.loads(news)
       # print(news_py["articles"])
            arts = news_py["articles"]

            for article in arts:
                speak(article['title'])
       # speak("moving on to the next news")

       elif _input == ("I"):
            speak("International News for today are as follows")
            speak("This news is brought to you by BBC News")
            url2 =("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=6aaf3b20b83b426592cf46e65dfa8571")
            news2 = requests.get(url2).text
            news_py2 = json.loads(news2)
       # print(news_py["articles"])
            arts2 = news_py2["articles"]

            for article in arts2:
                speak(article['title'])
       # speak("moving on to the next news")

       """elif _input ==(" P "):
             speak("Pausing  news")

       elif _input ==(" R "):
             speak("Resuming  news")


       elif _input==("E"):
             speak("Existing News Teller")
else :
     print("you have entered a wrong input")"""