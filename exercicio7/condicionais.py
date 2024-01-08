#Trabalhando com condicionais IF - ELSE - ELIF

userReply = input("Do you need to ship a package? (Enter yes or no): ")

if userReply == "yes":
  print('We can help you with that package!')
  userPackage = input("What's the type of cargo? (Enter stamps, envelope or copy)")

  if userPackage == "stamps":
    print("We have too many stamps designs for you choose from.")
  elif userPackage == "envelope":
    print("We have too many envelope sizes for you choose from.")
  elif userPackage == "copy":
    copies = input("How many copies would you like? (Enter a number, plz): ")
    print("Ok, we'll make you {} copies".format(copies))
  else:
    print("None of the options? ok then.")
else:
  print('Please, come back when you need. Thankz')
