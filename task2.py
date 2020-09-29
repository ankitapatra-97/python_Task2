import os
import pyttsx3
import datetime
import webbrowser as wb
import speech_recognition as sr

print("--------------------------------------------------------------------")
print("Welcome to PyTools.I am Typsy, your technical voice assistant.How can I help you?")
print("--------------------------------------------------------------------")
pyttsx3.speak("Welcome to PyTool. I am Typsy, your technical voice assistant")
pyttsx3.speak("How can I help you?")
pyttsx3.speak("I am here to help you with executing Linux commands, launching and stoping docker containers")
print("It's my pleasure to serve you.",end='')

while True:
  p=input("Enter your requirements: ")
  print(p)
  
  if(('run' in p) or ('open' in p) or ('execute' in p)) and (("chrome" in p) or ("browser" in p)):
      pyttsx3.speak("Opening Chrome")
      os.system("chrome")
  elif(('run' in p) or ('open' in p) or ('execute' in p)) and (("notepad" in p) or ("editor" in p)):
      pyttsx3.speak("Opening Notepad")
      os.system("notepad")
  elif(('run' in p) or ('open' in p) or ('execute' in p)) and (("zoom" in p) or ("meeting app" in p)):
      pyttsx3.speak("Opening Zoom meetings")
      os.system("zoom")
  elif(("open" in p) or ("run" in p) or ("execute" in p)) and (("kmplayer" in p) or ("media player" in p)):
      pyttsx3.speak("Opening KM Player")
      os.system("kmplayer")
  elif(('check' in p) or ('what is' in p) or ('show' in p)) and ("IP address" in p):
      pyttsx3.speak("Showing IP")
      os.system("ipconfig")
  elif('open' in p) and ("telegram" in p):
      pyttsx3.speak("Opening Telegram")
      os.system("telegram")
  elif(('run' in p) or ('execute' in p)) and (('linux' in p) or ('command' in p)):
      wb.open("http://192.168.99.103/linuxcmd.html")
      pyttsx3.speak("From here you can execute Linux commands.")
  elif(('launch' in p) or ('run' in p)) and (('docker' in p) or ('container' in p)):
      wb.open("http://192.168.99.103/dockerrun.html")
      pyttsx3.speak("From here you can launch Docker container.")
  elif('stop' in p) and (('docker' in p) or ('container' in p)):
      wb.open("http://192.168.99.103/dockerstop.html")
      pyttsx3.speak("From here you can stop Docker container.")
  elif('open' in p) and (('facebook' in p) or ('fb' in p)):
      wb.open("https://www.facebook.com")
      pyttsx3.speak("Welcome to Facebook")
  elif('open' in p) and (('listen to my beat' in p) or ('music channel' in p)):
      wb.open("https://www.youtube.com/channel/UCnQUeMaJsI1KG2clbrU4ocw")
      pyttsx3.speak("Welcome to Listen to my beat Ankita")
  elif('open' in p) and ('linkedin' in p):
      wb.open("https://www.linkedin.com")
      pyttsx3.speak("Opening Linkedin")
  elif(('quit' in p) or ('exit' in p) or ('close' in p) or ("stop" in p)):
      break
  else:
      print("Command not supported")

print("Hope you enjoyed the service.Thank You!!")
pyttsx3.speak("Hope you enjoyed the services")
pyttsx3.speak("Thank you")