import random, easygui

words = ["paper", "sammy"]
letters = "qwertyuiopasdfghjklzxcvbnm"

answer = random.choice(words)
easygui.buttonbox("Word", choices=letters)
