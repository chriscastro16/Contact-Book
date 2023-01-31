Data = []


while True:
    name = input("Enter Contact's name: ")
    number = input("Enter Contact's phone number: ")

    Data.append(name)
    Data.append(number)


    option = input("Would you like to enter another Contact? (y / n) : ")
    if option.casefold() == 'n':
        break



for contact in Data:
    print(contact)