import speech_recognition as sr 
from voice_pepe.voicepepe_module import pepe_say
import cowsay
def main():
    listen_then_recognize()
    
    
    
def listen_then_recognize():
    # first of all here we're going to make recognizer through initializing it with recognizer's constructor
    recogniser = sr.Recognizer() # this creates a recognizer instance
    
    #now we're going to take audio-input stream by acessing the system's default microphone
    '''
    Using the with statement in Python, particularly when working with resources like files or hardware devices, 
    it ensures that the resource is properly managed and released when it's no longer needed. 
    In the context of the SpeechRecognition library and the Microphone instance, using the with statement ensures proper initialization and cleanup of the microphone resource.

    Here's why the with statement is used when working with the default microphone:

    Resource Management: When you create a Microphone instance using sr.Microphone(), you're essentially accessing an audio input device (microphone). 
    This device is a system resource that needs to be properly managed. The with statement ensures that the Microphone instance is properly initialized before the indented block is executed 
    and that it's properly released afterward.
    
    Context Manager: The Microphone class is designed to act as a context manager in Python. This means it implements the __enter__() and __exit__() methods, 
    allowing it to be used with the 'with' statement. When you enter the with block, the __enter__() method of the Microphone class is called, which initializes the microphone resource. 
    When you exit the with block, the __exit__() method is called, which releases the microphone resource.
    Error Handling: The with statement also provides a built-in mechanism for error handling and cleanup. If an exception occurs within the with block, 
    the __exit__() method of the context manager (in this case, the Microphone instance) is still called, allowing for proper cleanup of resources, such as releasing the microphone.
    '''
    with sr.Microphone() as source:
        print(""" 
  ⠀⠀⠀⠀ ⠀⠀⠀   ⠀⠀⠀  ⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀   ⠀⠀ ⠀ ⠠⠶⠿⠿⣿⣿⠿⠿⠶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀   ⠀⠀⠀ ⠀ ⠤⠤⠤⠤⣿⣿⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀   ⠀⠀⠀⠀ ⠀ ⠤⠤⠤⠤⣿⣿⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⢀⣀⣀⣀⣀ ⠀⠶⠶⠶⠶⠿⠿⠶⠶⠶⠶⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀     ⠀⠈⠉⠛⠉⠉⠀⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠀⠉⠉⠛⠉⠁⠀⠀
𝙒𝙚'𝙧𝙚 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙪𝙨𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝘿𝙚𝙛𝙖𝙪𝙡𝙩 𝙢𝙞𝙘𝙧𝙤𝙥𝙝𝙤𝙣𝙚⠀⠀
⠀⠀   ⠀ ⠀⠀ ⠀⣶⠀⠀⠀⣶⣶⣶⣶⡆⢰⣶⣶⣶⣶⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀    ⠀⠀ ⣿⡀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀    ⠀ ⢹⡇⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀    ⠀ ⠈⢿⡄⠀⠈⠻⢿⣿⡇⢸⣿⡿⠟⠁⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀   ⠀⠀ ⠀ ⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀   ⠀⠀ ⠀ ⠀⠈⠛⠷⠶⢶⣶⣶⡶⠶⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀   ⠀⠀⠀ ⠀ ⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀   ⠀  ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀
         𝕃𝕚𝕤𝕥𝕖𝕟𝕚𝕟𝕘...𝔾𝕠 𝕒𝕙𝕖𝕒𝕕!!
            ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉
        """)

        
        #adjusting the recogniser sensitivity to ambient noise
        recogniser.adjust_for_ambient_noise(source)
        #now going to record audio from microphone 
        audio = recogniser.listen(source)
    try:
         # Using Google Web Speech API to recognize the audio and transcribe it 
        text = recogniser.recognize_google(audio)
        pepe_say(text)
    except sr.UnknownValueError:
        cowsay.cow("Google Speech Recognition could not understand you ..please try again")
    except sr.RequestError as e:
        cowsay.tux(f"Could not request results from Google Speech Recognition service; {e}")
        
if __name__ == "__main__":
    main()
    
