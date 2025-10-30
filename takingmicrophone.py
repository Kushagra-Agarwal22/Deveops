# import speech_recognition as taking_input_from_microphone
# import webbrowser


# def listen_command():
#     recognizer = taking_input_from_microphone.Recognizer()

#     with taking_input_from_microphone.Microphone() as source:
#         print("listening...")

#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio).lower()

#         print('you said this command ' , command)
#         return command
    
#     except  taking_input_from_microphone.UnknownValueError:
#         print("Sorry I did'nt catch that coud you speak little louder ")
#         return  ""

#     except  taking_input_from_microphone.RequestError:
#             print("Nwetwork problem")
#             return ""


# def execute_command(command):
#     if "open google" in command  or "google it" in command:
#         print("Opening Google...")

#         webbrowser.open("https://www.google.com")
    
#     else:

#          print("Command not recognized.")

# if __name__ == "__main__":
#     while True:
#         cmd = listen_command()

#         if "friday" in cmd:
#             speak("how can i help you ")
#             command = listen_command()  # listen for next command
#             execute_command(command)

#             elif ("exit" in cmd or "quit" in cmd):
#                 print("Bye bye baad me miley ")
#                 break
#             execute_command(cmd)

    

import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print('You said:', command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you speak louder?")
        return ""
    except sr.RequestError:
        print("Network problem.")
        return ""

def execute_command(command):
    if "open google" in command or "google it" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    else:
        speak("Command not recognized.")

if __name__ == "__main__":
    speak("Assistant started. Say 'Friday' to activate.")
    while True:
        cmd = listen_command()

        if cmd:
            if "exit" in cmd or "quit" in cmd:
                speak("Bye bye, see you later!")
                break

            # Activate only if wake word "friday" is spoken
            if "friday" in cmd:
                speak("How can I help?")
                command = listen_command()
                if command:
                    if "exit" in command or "quit" in command:
                        speak("Goodbye!")
                        break
                    execute_command(command)
            else:
                print("Waiting for wake word 'Friday'.")
