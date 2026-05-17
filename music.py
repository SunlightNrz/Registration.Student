import time
import sys

def print_lyrics():
    lyrics = [
        "Maybe it's 6:45",
        "Maybe I'm barely alive",
        "Maybe you have taken my shit for the last time yeah",
        "Maybe I know I'm drunk",
        "Maybe I know you are the one",
    ]
    
    delays = [0.7, 0.2, 0.5, 0.5, 1.1]
    
    print("Girls like you:\n")
    time.sleep(1.4)
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()  # move to next line after full line is printed
        time.sleep(delays[i])

print_lyrics()