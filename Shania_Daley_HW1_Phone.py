#Shania Daley 
#Homework 1 
#Contact book and Sumulated Phone

# Define at least 1 class --done
# Define at least 1 function for each class --done
# Use list comprehension to create lists --done
# Use dictionary comprehension to create dictionary --done
# Use 1 if-elif --done
# Use 1 for or while --done
# Use 1 try-except --done
# Use input() function  for user input --done
# Produce interesting output
# Add comments

#Class for Individual Contacts
class Contact:
    def __init__(self, name, number, blocked=False, closeFriend=False):
        self.name = name
        self.number = number
        self.blocked = blocked
        self.closeFriend = closeFriend

#Prints Contact's Information 
    def contactInfo(self):
        print("Name:    " + self.name + "\nNumber:  " +
              self.number)
        
        if self.closeFriend == True:
            print("Close Friend\n")
            print("--------------------------")

        else:
            print("Not Close Fiend\n")
            print("--------------------------")       

#Function to block a contact. Gives user the option to cancel this decision 
    def blockContact(self):
        answer = input("Are you sure you want to block contact? ")
        if "Y" in answer.upper():
            self.blocked = True
            print(self.name + " is now blocked.")
        else:
            print(self.name + " will remain unblocked.")

#Function to unblock a contact. Gives user the option to cancel this decision 
    def unblockContact(self):
        answer = input("Are you sure you want to block contact? ")
        if "Y" in answer.upper():
            self.blocked = False
            print(self.name + " is now blocked.")
        else:
            print(self.name + " will remain blocked.")

#Function to add Contact to close friend list
    def makeCloseFriend(self):
        ("Adding " + self.name + " to your close friends...")
        self.closeFriend = True
        (self.name + "is now a close friend.")

#Function to edit the Contact's phone number
    def changeContactNumber(self):
        #user has 4 tries to input a valid phone number
        tries = 4
        while(tries >= 0):
            try:
                answer = input(
                    "Are you sure you want to change contact number? ")
                #If user inputs empty string case is handled and user is given another try
                if not answer:
                    print("You have " + str(tries) + " tries left to enter a correct option")
                    raise ValueError('You did not enter anything. Please try again with Yes or No')
            except ValueError as e:
                print(e)
                tries-=1
                continue

            if "Y" in answer[0].upper():
                prompt = ("What is the new number you would like to change the number " + self.number + " to? ")
                try:
                        newNumber = int(input(prompt))
                        if(len(str(newNumber)) != 10):
                            print("This is an invalid number, try again")
                            tries -= 1
                            print("You have " + str(tries) + " tries left to enter a correct option")
                            continue
                        else:
                           self.number = str(newNumber)
                           print("Ok, the new number under contact name " +
                                 self.name + " is " + self.number + ".")
                           break

                except ValueError:
                        ("This is an invalid number, try again")
                        tries -= 1
                        print("You have " + str(tries) + " tries left to enter a correct option")
                        continue

            elif "N" in answer[0].upper():
                print("Ok, " + self.name + " 's Number Will Remain The Same")
                break
                
            else:
                print("Invalid answer. Return to menu and Respond Yes or No")
                continue  


# initialize imported contacts (for test purposes)
mira = Contact("Mira","6262204628", closeFriend=True)
tyson = Contact("Tyson", "4322675287", closeFriend=True)
lianna = Contact("Lianna","6128796356",closeFriend=True)
ryan = Contact("Ryan", "6704847613", closeFriend=True)
peter = Contact("Peter", "2017089500")
caleb = Contact("Caleb","7814493424", closeFriend=True)
brandon = Contact("Brandon", "3342629876", closeFriend=True)
zack = Contact("Zack", "8567023991")
mom = Contact("Mom", "5037289334")
dad = Contact("Dad", "6785372728")
migos = Contact("Migos", "3186462051")
obama = Contact("Obama", "3393642180")
kylieJenner = Contact("Kylie Jenner", "3392353994")
katyPerry = Contact("Katy Perry", "4044332802")
ex = Contact("Ex", "6713557427", blocked=True)

#initialized contact list of objects
contactList = [mira,tyson,lianna,ryan,peter,caleb,brandon,zack,mom,dad,migos,obama,kylieJenner,katyPerry,ex]

#list comprehension
#list of just names
contactNameList = [friend.name for friend in contactList]
#list of just numbers
contactNumberList = [num.number for num in contactList]
#list of Contacts that blocked
blockedNames = [b.name for b in contactList if b.blocked == True]
#list of Numbers that blocked
blockedNumbers = [u.number for u in contactList if u.blocked == True]

# put contacts in a dictionary key is name value is number 
#dictionary comprehension 
phoneBook = {personName: personNumber for personName,personNumber in zip(contactNameList, contactNumberList)}

#blocked dictionary
#blocked phone book 
bphoneBook = {bpersonName: bpersonNumber for bpersonName,bpersonNumber in zip(blockedNames, blockedNumbers)}
user = ""                        

#Print out list of contacts
def showContacts():
    global contactList
    global user
    for initContact in contactList:
         initContact.contactInfo()

    print("Returning To Main Menu...")
    showMainMenu(user)

#Function changes blocked attribute to True if unblocked and False if blocked
def block(theName):
    global contactList
    global user
    for x in contactList:
        if (x.name.lower() in theName.lower() and x.blocked is False):
            x.blockContact()
            print("Returning To Main Menu...")
            showMainMenu(user)

        elif (x.name.lower() == theName.lower() and x.blocked is True):
            ans = input("This Contact Is Already Blocked. Would You Like To Unblock Them? Y or N")
            if "Y" in ans.upper():
                x.unblockContact()
            else: 
                print(theName + " Will Remain Blocked.")
                print("Returning To Main Menu...")
                showMainMenu(user)
        else:
            print("Returning To Main Menu...")
            showMainMenu(user)

#Shuts off phone and exits program
def shutdown():
     print("******** SHUTTING DOWN ********\n")
     print("           GOODBYE!              ")
     exit()
    
#Displays the main menu with options to pick from
#Poor input is mostly handled if an option entered is not present on the menu
def showMainMenu(userName):
    print("\n******** MAIN MENU ********\n")
    print("1. Add New Contact       2. Show Contacts       3. Look Up Contact")
    print("4. Block Contact         5. Turn Off Phone\n")
          
    global contactList
    global user
    menuOption = input(userName + ", What Would You Like To Do? ")
    try:
        if menuOption in {"1"}:
            print("******** ADDING NEW CONTACT ********\n")
            contactName = input ("Name: ")
            contactNumber = input("Number: xxx-xxx-xxxx ")
            isCloseFriend = input("Add to close friends? Y or N ")
            
            if "Y" in isCloseFriend.upper():
                newContact = Contact(contactName,contactNumber.replace("-",""), closeFriend=True)
                contactList.append(newContact)
                print(contactName + " added to Contact List")
                print("Returning to Main Menu...")
                showMainMenu(user)

            else:
                newContact = Contact(contactName,contactNumber.replace("-",""), closeFriend=False)
                contactList.append(newContact)
                print(contactName + " added to Contact List")
                print("Returning to Main Menu...")
                showMainMenu(user)

        elif menuOption in {"2"}:
            print("******** SHOWING CONTACTS ********\n")
            showContacts()

        elif menuOption in {"3"}:
            print("******** LOOKUP CONTACT ********\n")
            lookup = input("Who Would You Like To Lookup? ")
            print("Ok, Here Is Their Information...\n")
            for x in contactList:
                if x.name.lower() in lookup.lower():
                    x.contactInfo()
                    print("Returning to Main Menu...")
                    showMainMenu(user)

                else:
                    print("Contact Is Not In Phone.")
                    print("Returning to Main Menu...")
                    showMainMenu(user)

        elif menuOption in {"4"}:
            print("******** BLOCK/UNBLOCK CONTACT ********\n")
            blockName = input("Enter The Contact Name To Unblock/Block \n --> ")
            block(blockName)
    
        elif menuOption in {"5"}:
            shutdown()

        else:
            count = 2
            if ("" in menuOption or menuOption not in {"1,2,3,4,5,6"}):
                raise ValueError("That Is Not A Menu Option. Try Again. \n -->")
            else:
                print("Please Return To Main Menu And Try Again")
                showMainMenu(user)
    except ValueError as t:
        print(t)
        count-=1
        while count >= 0:
            continue
        
        if count == 0:
            shutdown()

#Startup Menu For the phone
def phoneOptions():
    attempt = 2
    while(attempt >= 0):
        global user
        user = input ("Enter Your Name To Activate Phone: \n --> ")
        try:
            if user and user.strip():
                print("\nWelcome " + user + "!\n")
                print("Activating Phone...")
                print("Importing Contacts...")
                print("Starting Up Phone...\n\n")
                showMainMenu(user)
                break
            else:
                print("You have " + str(attempt) + " tries left to enter a correct option")
                raise ValueError("I'm Sorry Did You Forget To Enter Your Name? Please try again!\n")
            
        except ValueError as x:
            print(x)
            attempt-=1
            if attempt >= 0:
                continue
            else:
                print("Failed to Enter Name")
                print("Shutting Down\n")
                break

#main
if __name__ == "__main__":
    phoneOptions()

