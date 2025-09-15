import speech_recognition as sr
import time
import distutils
print("distutils is installed and available.")


r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"Recognized text: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Optional: Short delay to avoid rapid looping
    time.sleep(1)
