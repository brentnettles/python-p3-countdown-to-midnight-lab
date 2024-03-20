import time


def countdown(i):
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    if i == 0:
        print("HAPPY NEW YEAR!")
    return i

def countdown_with_sleep(i):
    while i > 0:
        print(f'{i} SECOND(S)!')
        time.sleep(1) 
        i -= 1
    if i == 0:
        print("HAPPY NEW YEAR!")

countdown(5)
countdown_with_sleep(10)
# print()