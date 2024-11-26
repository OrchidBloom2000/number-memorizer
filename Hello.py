print("hello! this code helps you memorize digits!")
input("press a key and press enter to continue :P")

print("so,")
goal = input("what's the number u want to memorize?")

counter = 0

while counter < len(goal):
    if input("ok, what's the next digit?") == goal[counter]:
        counter += 1
    else: 
        print("oopsie, that wasn't the correct number!") 
        break
print("done")