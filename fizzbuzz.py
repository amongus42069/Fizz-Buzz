#Josh Park, Feb 3 2022, Fizz Buzz assignment for the sound effects dinosaurs make when cut.
for dino in range(1,101): #Prints all dinos to 100, excluding 0
    if dino % 15 is 0: #If dinosaur can be cut 15 times evenly, it will print the sound effects fizz and buzz
        print("Fizzbuzz")
    elif dino % 3 is 0: #If dinosaur can only be cut 3 times evenly, it will only print the sound effect fizz
        print("Fizz")
    elif dino % 5 is 0: #If dinosaur can only be cut 5 times evenly, it will only print the sound effect buzz
        print("Buzz")
    else:
        print(dino) #Prints dinosaurs taht cannot be cut in 3 5 or 15 times evenly