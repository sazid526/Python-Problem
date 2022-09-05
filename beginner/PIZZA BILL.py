print("Welcome to our pizza delevery shop")

size = input("Which size of pizza do you want?S,M OR L? ")
add_pepperomi = input("Do you want add pepperomi?If yes,press Y otherwise N. ")
extra_chese = input("Do you want to add exta_chese?If yes,press Y otherwise N ")
bill = 0
if size == "S":
    if add_pepperomi == "Y":
        bill = 20+2
    elif add_pepperomi == "N":
        bill = 20   
    if extra_chese == "Y":
        bill = 20+1
    elif extra_chese == "N":
        bill = 20    
print(f"Your bill is ${bill}")    