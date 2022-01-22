while True :
    inputs = input("> ")

    if inputs[0] == "#" :
        continue
    elif inputs == "done" :
        print(inputs)
        break
    else:
        print(inputs)
