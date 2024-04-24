temperature = input("temperature: ")

if int(temperature) > 80:
    print("It's a warm day!")
    print("Drink plenty of water!")
elif int(temperature) > 50: # (50, 80])
    print("It's a nice day!")
    print("Enjoy the outside!")
elif int(temperature) > 30: # (30, 50]
    print("It's quite chilly outside.")
elif int(temperature) > 0: # (0, 30])
    print("Too cold! Stay inside!")