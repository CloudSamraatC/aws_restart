#If loop

userReply = input("Do you need to ship a package? (Enter yer or no)")
if userReply == "yes":
    print ("we can help you ship that pacakage!")

else:
    print("please come back when you need to ship. Thank you.")


#elif statement

yourReply = input ("would you like to buy stamps, an envelop, or make a copy? (Enter stamps, envelop, copy)")

if yourReply == "stamps":
    print("we have many stamps to choose from.")
elif yourReply == "envelop":
    print ("we have differnet size envelop to choose from.")
elif yourReply == "copy":
    copy = input("how many copies would you like? (Enter a number)")
    print ("here are {} copies".format(copy))
else:
    print("Thank you, plese come again.")
    
    

    