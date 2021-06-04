import random

outNick = ""
unicode = ["└├", "╣", "╢", "▓", "乡", " ψ", "✫", "妻", "☠", "⛥"]
wordList = ["zxc", "clown", "ghoul", "1v1", "wood", "mid", "inside", "SSS", "kill", "dead", "life", "stealer"]

for i in range(0, random.randint(2, 5)):
    outNick += random.choice(unicode)
outNick += " "

for i in range(0,3):
    outNick += wordList[random.randint(0,11)] + " "

for i in range(0, random.randint(2, 5)):
    outNick += random.choice(unicode)

print(outNick)
