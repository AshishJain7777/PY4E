while True:
    line = input(">")  
    if line[0] == "#":  
        continue  # this will keep looping up until we enter the desired amount it asks to exit the loop.
    if line =="done":
        break
    print(line)
print("All Done")