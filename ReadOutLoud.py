
import pyttsx3

# initialisation
engine = pyttsx3.init()
# var="Good night mummy ,Did you have your medicines and inhaler"
# testing
var = "Hello Sir"
engine.setProperty('rate',120)
engine.say(var)
engine.say("Thank you, MR EL for inventing me and bringing me alive ")
engine.say("I will obey you sir  ")


WPM = engine.getProperty('rate')   # getting details of current speaking rate

print(f"The current rate at which this speaks is {WPM}")




engine.runAndWait()






















# for reference
'''import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()'''