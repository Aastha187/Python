counter=0
def increment():
    global counter
    counter+=1
    return counter
counter=increment()
print(counter)
