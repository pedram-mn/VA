import os

def go_to():
    while True:
        try:
            print("enter \"stop\" to cancel and close this section")
            target = str(input("enter path : "))
            if target == "stop":
                break
            else:
                os.startfile(target)
        except FileNotFoundError:
            print("file not found, try again...")
