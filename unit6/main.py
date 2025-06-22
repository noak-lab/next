import base64
from file2 import BirthdayCard
from file1 import GreetingCard
import pyttsx3
import os
################## 6.1.4 ##################


def convert_from_b64():
    x = base64.b64decode(("CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAg" +
                         "ICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8" +
                         "ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgI" +
                         "CAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19" +
                         "fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX1" +
                         "9fX3wvCgo=").encode("utf-8"))
    print(x)

################## 6.2.5 ##################

def greeting_cards():
    gcard = GreetingCard()
    bcard = BirthdayCard()

    gcard.greeting_msg()
    bcard.greeting_msg()

################## 6.3.3 ##################


def text_to_speech():
    text = "first time i'm using a package in next.py course"
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    convert_from_b64()
    greeting_cards()
    text_to_speech()

if __name__ == '__main__':
    main()
