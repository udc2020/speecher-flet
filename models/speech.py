import pyttsx3 


class SpeechToText:

    def convert(self, text,gender,speed):
        engine = pyttsx3.init()  
        try:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[gender].id)
         
            if speed == 0:
                engine.setProperty('rate', 25 )
            elif speed == 2 :
                engine.setProperty('rate', 250 )
            else : 
                engine.setProperty('rate', 100 )
                
            engine.say(text)
            engine.runAndWait() 

        except:
            print(f'that is error ')
