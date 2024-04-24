temperature = 48

if temperature > 80:
    print("It's a warm day!")
    print("Drink plenty of water!")
elif temperature > 50: # (50, 80])
    print("It's a nice day!")
    print("Enjoy the outside!")
elif temperature > 30: # (30, 50]
    print("It's quite chilly outside.")
elif temperature > 0: # (0, 30])
    print("Too cold! Stay inside!")