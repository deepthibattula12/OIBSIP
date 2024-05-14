import speech_recognition as sr
import pyttsx3
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)  # Recognize speech using Google Speech Recognition
            print(f"User say: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Main function to handle user interactions
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I assist you today?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hi there!")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "goodbye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand. Can you please repeat that?")