#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
#
# Created:     13/07/2017
# Copyright:   (c) 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Fuctions that need to be imported
import random
import time
members = []

def main():
    loadData()
    usersChoice = menu()
    while (usersChoice != "Q"):
        if usersChoice == ("A"):
            addMember()
            saveData()
        elif usersChoice == ("S"):
            searchBySurname()
        elif usersChoice == ("B"):
            bookNights()
            saveData()
        elif usersChoice == ("T"):
            total()
        elif usersChoice == ("D"):
            displayAllMembers()
        usersChoice = menu()
    print ("Goodbye")

if __name__ == '__main__':
    main()

#Different ways to generate random numbers({:03d} allows the 3 digits to be produced between 1 and 100 e.g. 001, 005 etc.)

#for randNum in range (0,5):
 #   randomNumber = random.randint(1,10)
  #  print(randomNumber)
def randomDigits():
        randomNumber = random.randrange(1,999)
        myID = ("{:03d}".format(randomNumber))
        #print (myID)
        return (myID)

def surname():
    alpha = False
    while alpha == False:
        surname = input("Please enter surname: ")
        surname = (surname.capitalize())
        alpha = (surname.isalpha())
        if alpha == False:
            print ("Error")
        else:
            return (surname)

#Getting the first 3 charachters from someones name. Keeps the first charachter capitalised.
def surnameID(pName):
    surname = pName[0:3]
    #print (surname)
    surnameLower = (surname.lower())
    surnameHigher = (surnameLower.capitalize())
    return (surnameHigher)

#Getting the last 2 digits of the current year
def year():
    year = (time.strftime("%Y"))
    #print (year[2:4])
    return (year[2:4])

def getMemID(pSurname):
    three = randomDigits()
    sur = (surnameID(pSurname))
    currentyear = year()
    memID = ((sur)+(three)+(currentyear))
    return (memID)

def loadData(): #Loads the data from a CSV file
    infile = open ("SampleData2017.txt",'r')
    for theLine in infile:
        theLine = theLine.strip("\n")
        theSplitLine = theLine.split(",")

        littleList = []
        littleList.append  (theSplitLine[0])
        littleList.append  (theSplitLine[1])
        littleList.append  (int(theSplitLine[2]))
        littleList.append  (theSplitLine[3])
        littleList.append  (int(theSplitLine[4]))
        littleList.append  (int(theSplitLine[5]))

        members.append(littleList) #Puts all info into one big list

    infile.close()

def saveData():  # NEW FEATURE: Save data to file
    with open("SampleData2017.txt", "w") as outfile:
        for person in members:
            line = ",".join([str(x) for x in person])
            outfile.write(line + "\n")
    print("Data saved to file.")

def menu():
    inChoice = ""

    while (inChoice != "A" and inChoice != "B" and inChoice != "S" and inChoice !="T" and inChoice != "Q" and inChoice !="D"):
        print ("="*76)
        print ("A   Add new member")
        print ("B   Book nights")
        print ("D   Display all members")
        print ("S   Search for member")
        print ("T   Total numbers of guests")
        print ("Q   Quit this program")
        print ("\n")
        inChoice = input ("Please choose an option ")
        inChoice = inChoice.upper()
    return (inChoice)

def addMember():
    littleList = []
    theSurname = surname()
    littleList.append (getMemID(theSurname))
    littleList.append (theSurname)
    littleList.append (int(time.strftime("%Y")))
    littleList.append ("Silver")
    littleList.append (0)
    littleList.append (0)
    members.append (littleList)
    print (littleList[0],littleList[1],littleList[2],littleList[3],littleList[4],littleList[5])
    print("New member added.")

def findRecord(inID):
    index = 0
    found = False
    while (found == False) and (index < len(members)):
        person = members[index]
        if (person[0]==inID):
            found = True
        else:
            index = index +1
    if found == True:
        return (person)
    else:
        return (None)

def bookNights():
    alpha = False
    while alpha == False:
        membersID = input ("Please enter members ID: ")
        membersIDCap = (membersID.capitalize())
        theMember=findRecord(membersIDCap)
        if theMember != None:
            alpha = True
            print("                        ", "{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format("ID", "Surname", "Year", "Membership", "Nights", "Points"))
            print("The original record is: " ,"{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format(theMember[0],theMember[1],theMember[2],theMember[3],theMember[4],theMember[5]))
        else:
            print("Member not found.")

    a = False
    while a == False:
        try:
            nights = int(input("How many nights? "))
            if (nights > 14):
                print ("ERROR: Max nights booking is 14.")
            else:
                theMember[4] += nights
                #Updating status
                if (theMember[4]<30):
                    theMember[3]=("Silver")
                elif (theMember[4] >= 30) and (theMember[4] < 100):
                    theMember[3] = ("Gold")
                elif (theMember[4] >= 100):
                    theMember[3] = ("Platinum")
                #Updating points
                if theMember[3] == ("Silver"):
                    theMember[5] += 2500*nights
                elif theMember[3] ==("Gold"):
                    theMember[5] += 3000*nights
                elif theMember[3] == ("Platinum"):
                    theMember[5] += 4000*nights
                #Redeeming points
                custAnswer = input ("Would customer like to redeem points? Y/N ")
                custAnswer = (custAnswer.capitalize())
                if custAnswer == ("Y") and (theMember[5]>25000*nights):
                    theMember[5] -= 25000*nights
                elif custAnswer == ("N"):
                    print ("Customer chosen not to redeem")
                else:
                    print ("Not enough points to redeem.")
                print("The updated record is : " , "{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format(theMember[0],theMember[1],theMember[2],theMember[3],theMember[4],theMember[5]))
                a = True
        except ValueError:
            print("ERROR: Please enter a valid number of nights.")

def displayAllMembers():
    print ("{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format("ID", "Surname", "Year", "Membership", "Nights", "Points"))
    print ("-"*50)
    for item in members:
        print ("{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format(item[0], item[1], item[2], item[3], item[4], item[5]))

def total():
    print ("The total number of members is: ",len(members))

# NEW FEATURE: Search by surname (instead of only by ID)
def searchBySurname():
    name = input("Enter surname to search: ").capitalize()
    found = False
    for person in members:
        if person[1] == name:
            print("Found: ", "{:^10} {:^10} {:^4} {:^10} {:^6} {:^6}".format(person[0], person[1], person[2], person[3], person[4], person[5]))
            found = True
    if not found:
        print("No member found with that surname.")

#def membershipStatus():
 #   for item in range (len(members)):
  #      membership = (item[3])
   # return membership
