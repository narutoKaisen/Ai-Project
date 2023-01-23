import pyttsx3  # A text-to-speech library.
import datetime #used for wishing on time
import speech_recognition as sr
import wikipedia
import webbrowser #for browsing the internet
import os  #for playing music
import pyjokes #for jokes

engine = pyttsx3.init('sapi5')   #Microsoft developed speech API.Helps in synthesis and recognition of voice and to use inbuild windows voice.

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id) #voiceid use to select different voices / [0]is for male voice and [1]is for female voice 
def speak(audio):

 engine.say(audio) 

 engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
   ''' This function is for wishing on time'''

   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
    speak("Good morning ")
   elif hour>=12 and hour<18:
    speak("Good Afternoon")
   else:
    speak("Good Evening")

   speak(" i am cortana sir how may i help you") 

def takecommand():
   ''' It takes microphone input from the user and returns string output '''   
   r = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 ## seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

   try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition and en-in is used for indian english.
        print(f"User said: {query}\n")  #User query will be printed.

   except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of inproper voice 
        return "None" #None string will be returned
   return query     

  

if __name__=="__main__" :

    wishme()
while True:
    query= takecommand().lower()

 # Logic for executing tasks based on query
    if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
    elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    elif 'open google' in query:
            webbrowser.open("google.com") 
    elif 'open facebook' in query:
            webbrowser.open("facebook.com")  
    elif 'open instagram' in query:
            webbrowser.open("instagram.com")   
    elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")   
    elif 'play music' in query:
          music_dir='C:\\Users\\asust\\Downloads\\music'
          songs = os.listdir(music_dir)
          print(songs)    
          os.startfile(os.path.join(music_dir, songs[0]))   
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
          codepath="C:\\Users\\asust\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"                      
          os.startfile(codepath)
    elif 'jokes' in query:
         speak(pyjokes.get_joke())