#functions..
import datetime
from speak import Say
import webbrowser
#2 Types

#1 - Non input

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

   


    



#2 - input
def InputExecution(tag, query):
    if "youtube" in tag:
        Say("ok sir , searching youtube")

        query = query.replace("martin", "")
        query = query.replace("search youtube", "")
        query = query.replace("search in youtube", "")
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        Say("searching done sir!")
    
    elif "google" in tag:
        Say("ok sir , searching google")

        query = query.replace("martin", "")
        query = query.replace("search google", "")
        query = query.replace("search in google", "")
        query = query.replace("google", "")
        query = query.replace("google search", "")
        web = 'https://www.google.com/search?q=' + query
        webbrowser.open(web)
        Say("searching done sir!")  