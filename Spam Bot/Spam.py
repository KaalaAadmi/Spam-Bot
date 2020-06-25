# Run this program and visit any site(whatsapp or instagram) and select the user you want to send the messages and the press any key in the trminal to send messages.
import pyautogui, time

input("Please press any key to continue: ")

f = open("BeeMovie.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")