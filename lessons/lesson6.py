from colorama import Fore, Back, Style
#
#
# print(Fore.RED + "Some text" + Style.RESET_ALL)
# print(Back.GREEN + "Some text" + Style.RESET_ALL)


from rich import print
from time import sleep
import pyttsx3
import threading


def speak_text(text, rate=180):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Скорость речи
    engine.say(text)
    engine.runAndWait()


def print_lyrics():
    lines = [
        ("I wanna da-", 0.06),  # 1
        ("I wanna dance in the lights", 0.05),  # 2
        ("I wanna ro-", 0.07),  # 3
        ("I wanna rock your body", 0.08),  # 4
        ("I wanna go", 0.08),  # 5
        ("I wanna go for a ride", 0.068),  # 6
        ("Hop in the music and", 0.07),  # 7
        ("Rock your body", 0.08),  # 8
        ("Rock that body", 0.069),  # 9
        ("come on, come on", 0.035),  # 10
        ("Rock that body", 0.05),  # 11
        ("(Rock your body)", 0.03),  # 12
        ("Rock that body", 0.049),  # 13
        ("come on, come on", 0.035),  # 14
    ]

    for text, delay in lines:
        speech_thread = threading.Thread(target=speak_text, args=(text,))
        speech_thread.start()

        for char in text:
            print(char, end='', flush=True)
            sleep(delay)
        print()

        speech_thread.join()
        sleep(0.3)


# print_lyrics()