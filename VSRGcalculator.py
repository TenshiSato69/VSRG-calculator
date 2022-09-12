def uif():
    print ("VSRG Calculator")
    print ("by TenshiGamer69")
    print ()
    print ("   1. Accuracy/Ratio Calculator")
    print ("   2. Dan Course Accuracy Calculator")
    print ("   3. Exit")
    print ()

def accuracy():
    print ("Games Available")
    print ()
    print ("   1. osu!mania")
    print ("   2. Malody")
    print ("   3. Exit")
    print ()

def malody():

    print ("Malody Accuracy Calculator")
    print ("Note: Judge Timing doesn't matter here")
    print () 
    best = int(input("Enter Best: "))
    cool = int(input("Enter Cool: "))
    good = int(input("Enter Good: "))
    miss = int(input("Enter Miss: "))
    print () 

    total = best + cool + good + miss

    malody = ((best*1)+(cool*(3/4))+(good*(2/5)))/total
    finalmalody = round((malody*100),2)

    if finalmalody == 100:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M5")
    elif finalmalody > 94.9999 and miss == 0:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M4")  
    elif finalmalody > 89.9999 and miss > 0:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M3")
    elif finalmalody > 79.9999 and miss > 0:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M2")
    elif finalmalody > 69.9999 and miss > 0:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M1")
    else:
        print ("Malody Accuracy: {}".format(finalmalody))
        print ("Malody Rank:M0")
    print () 
    

def osu():

    print ("osu!mania Accuracy Calculator")
    print () 
    marvelous = int(input("Enter 320: "))
    perfect = int(input("Enter 300: "))
    great = int(input("Enter 200: "))
    good = int(input("Enter 100: "))
    bad = int(input("Enter 50: "))
    miss = int(input("Enter 0: "))
    print () 

    total = marvelous + perfect + great + good + bad + miss

    accuracy = (((marvelous+perfect)*1)+(great*(2/3))+(good*(1/3))+(bad*(1/6)))/total
    finalacc = round((accuracy*100),2)
    accv2 = ((marvelous*1)+(perfect*(9836/10000))+(great*(6557/10000))+(good*(3279/10000))+(bad*(1639/10000)))/total
    finalaccv2 = round((accv2*100),2)
              
    if perfect == 0:
        print ("MA:PA = ±∞:1")
    else:
        ratio = round((marvelous/perfect),2)
        print ("MA:PA = {}:1".format(ratio))
    print () 
    if finalacc == 100:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Score v1 Rank:SS")
    elif finalacc > 94.9999:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Score v1 Rank:S")  
    elif finalacc > 89.9999:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Rank:A")
    elif finalacc > 79.9999:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Score v1 Rank:B")
    elif finalacc > 69.9999:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Score v1 Rank:C")
    else:
        print ("Score v1 Accuracy: {}".format(finalacc))
        print ("Score v1 Rank:D")
    print () 
    if finalaccv2 == 100:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:SS")
    elif finalaccv2 > 94.9999:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:S")  
    elif finalaccv2 > 89.9999:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:A")
    elif finalaccv2 > 79.9999:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:B")
    elif finalaccv2 > 69.9999:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:C")
    else:
        print ("Score v2 Accuracy: {}".format(finalaccv2))
        print ("Score v2 Rank:D")
    print ()

    
def dan():
    print("Dan Course Acc Simulator")
    print () 
    first = float(input("Enter First Accuracy: "))
    second = float(input("Enter Second  Accuracy: "))
    third = float(input("Enter Third Accuracy: "))
    fourth = float(input("Enter Fourth Accuracy: "))
    print () 


    sec = round((second*2)-(first),2)
    trd = round((third*3)-(first+second),2)

    print ("1st Song Accuracy: {}".format(first))
    print ("2nd Song Accuracy: {}".format(sec))
    print ("3rd Song Accuracy: {}".format(trd))

    if fourth != 0 or "":
        fth = round((fourth*4)-(first+second+third),2)
        print ("4th Song Accuracy: {}".format(fth))
    print ()

def end():
    print()
    print()
    print()
    print("Process finished with exit code 0")

def fail():
    print("Enter the valid number")
    print()


uif()
choice = int(input("Enter number of choice: "))
print()
if choice == 1:
    accuracy ()
    choiceacc = int(input("Choose the number of choice: "))
    print () 
    if choiceacc == 1:
        osu ()
    elif choiceacc == 2:
        malody()
    elif choiceacc == 3:
        uif()
    elif choiceacc > 3:
        fail()
    while choiceacc != 3:
        accuracy()
        choiceacc = int(input("Choose the number of choice: "))
        print () 
        if choiceacc == 1:
            osu ()
        elif choiceacc == 2:
            malody()
        elif choiceacc == 3:
            uif()
        elif choiceacc > 3:
            fail()
elif choice == 2:
    dan()
elif choice == 3:
    end()
elif choice > 3:
    fail()
while choice != 3:
    uif()
    choice = int(input("Enter number of choice: "))
    print ()
    if choice == 1:
        accuracy()
        choiceacc = int(input("Choose the number of choice: "))
        print () 
        if choiceacc == 1:
            osu ()
        elif choiceacc == 2:
            malody()
        elif choiceacc == 3:
            uif()
        elif choiceacc > 3:
            fail()
        while choiceacc != 3:
            accuracy()
            choiceacc = int(input("Choose the number of choice: "))
            print () 
            if choiceacc == 1:
                osu ()
            elif choiceacc == 2:
                malody()
            elif choiceacc == 3:
                uif()
            elif choiceacc > 3:
                fail()
    elif choice == 2:
        dan()
    elif choice == 3:
        end()
    elif choice > 3:
        fail()
