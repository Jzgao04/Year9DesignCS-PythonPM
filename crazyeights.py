

import random

hearts = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H']
diamonds = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D']
spades = ['1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S']
clubs = ['1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C']


def dealCard():
    mainDeck = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H',  '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S']
    play1 = []
    for i in range(0,8):
        indexV = random.randint(0,len(mainDeck)-1)
        print(indexV)
        play1.append(mainDeck[indexV])
        print(play1)
        mainDeck.pop(indexV)
        
    
        
    comp1 = []
    for j in range(0,8):
        indexV = random.randint(0,len(mainDeck)-1)
        print(indexV)
        comp1.append(mainDeck[indexV])
        print(comp1)
        cardRemove = mainDeck.pop(indexV)
        print(mainDeck)
        
    return mainDeck, play1, comp1

    
    
def firstCard(mainDeck):
    
    index = random.randint(0,22)
    topCard = mainDeck.pop(index)
    
    return topCard



#def cardValid(topcard, play1, comp1):
    #for i in range(0,len(comp1)-1)
        
    
   
    
# def play1():

    

def main():
    mainDeck, play1, comp1 = dealCard()
    topCard = firstCard(mainDeck)
    cardPile = []
    cardPile.append(topCard)
    print ("The top card is {}").format(topCard)
    print ("Your card pile consists of {}").format(cardPile) 


main()


def compTurn(cardPile,comp1,mainDeck):
    
    cardInfo = cardValid(sameNum, snList, sameSuit, ssList, haveEight, eList)
    
    if sameNum == True:
        cardPile.append(snList)
        comp1.remove(snList)
        # print cardPile
        topCard = snList[snList(len)-1]
        return cardPile
        return topCard
        return comp1
    elif sameSuit == True and sameNum == False:
        suitChoice = random.choice(ssList)
        cardPile.append(suitChoice)
        comp1.remove(ssList)
        # print cardPile
        topCard = suitChoice
        # print topCard
        return cardPile
        return topCard
        return comp1
    elif haveEight == True and sameSuit == False and sameNum == False:
        eightChoice = random.choice(eList)
        cardPile.append(eightChoice)
        comp1.remove(eight)
        # print cardPile
        topCard = eightChoice
        # print topCard
        return cardPile
        return topCard
        return comp1
    else:
        drawnCard = random.choice(mainDeck)
        comp1.append(drawnCard)


#KARANS NEW FUNCTION THATS KINDA  IFFY 


def cardValid(topcard, play1, comp1):
    
    suit = topCard[0]
    number = topCard[1]
    
    ssList = []
    snList = []
    eList = [] 
    ssList2 = []
    snList2 = []
    eList2 = []
  
    sameNumLoc=-1
    for i in range(0,len(play1)-1):
          if number in play1[i] and sameNumLoc!=-1:
            sameNum == True 
            sameNumLoc = i
            snList.append( play1[sameNumLoc])
            
          elif suit in play1[i] and sameNumLoc!=-1:
            sameSuit == True 
            sameNumLoc = i
            ssList.append(play1[sameNumLoc])
            
          elif '8' in play1[i] and sameNumLoc!=-1:
            haveEight == True
            sameNumLoc = i
            eList.append(play1[sameNumLoc])
            
    for k in range(0,len(comp1)-1):
        
        if number in comp1[k] and sameNumLoc != -1:
            sameNum == True
            sameNumLoc = k
            snList2.append(comp1[sameNumLoc])
            
        elif suit in comp1[k] and sameNumLoc!=-1:
            sameSuit == True
            sameNumLoc = k
            ssList2.append(comp1[sameNumLoc])
            
        elif '8' in comp1[k] and sameNumLoc!=-1:
            haveEight == True
            sameNumLoc = k
            eList2.append(comp1[sameNumLoc])
            

        
        
    return sameNum,sameSuit,haveEight,ssList, snList, eList, ssList2,snList2,eList2







#KAITLYN STARTS HERE


import random
hearts = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H']
diamonds = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D']
spades = ['1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S']
clubs = ['1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C']

def dealCard():
    mainDeck = ['1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'JH', 'QH', 'KH', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'JD', 'QD', 'KD', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'JC', 'QC','KC','1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S','JS','QS','KS']
    
    play1 = []
    for i in range(0,8):
        indexV = random.randint(0,len(mainDeck)-1)
        #print indexV
        play1.append(mainDeck[indexV])
        mainDeck.pop(indexV)
    print(play1)
     
    comp1 = []
    for j in range(0,8):
        indexV = random.randint(0,len(mainDeck)-1)
        #print indexV
        comp1.append(mainDeck[indexV])
        cardRemove = mainDeck.pop(indexV)
    print(comp1)
    
        #print mainDeck
        
    return mainDeck,play1,comp1
    
def playTurn(play1,comp1,topCard, cardPile, mainDeck):
    playWin, compWin = endProgram(play1,comp1)
    
    while playWin == False and compWin == False:
        print("here are your cards: {}").format(play1)
        userChoice = raw_input("enter the card you wish to play:")
        
    sameNum, sameSuit, haveEight, ssList, snList, eList = cardValid(topCard,player)
    
    if sameNum == True:
        cardPile.append(snList)
        comp1.remove(snList)
        print(cardPile)
        topCard = snList[snList(len)-1]
        playWin, compWin = programEnd(play1,comp1)
        return topCard, cardPile, play1
    
    elif sameSuit == True and sameNum == False:
        suitChoice = random.choice(ssList)
        cardPile.append(suitChoice)
        comp1.remove(ssList)
        print(cardPile)
        topCard = suitChoice
        playWin, compWin = programEnd(play1,comp1)
        print(topCard)
        return cardPile, topCard, play1

    elif haveEight == True and sameSuit == False and sameNum == False:
        eightChoice = random.choice(eList)
        cardPile.append(eightChoice)
        comp1.remove(eight)
        print(cardPile)
        topCard = eightChoice
        playWin, compWin = programEnd(play1,comp1)
        print(topCard, cardPile, play1)
                
        # while userChoice not in play1 or userChoice[0] not in play1[i] and userchoice[1] != 8 or  userChoice[1] not in play[i] and userchoice[1] != 8:
        #     while userChoice not in play1:
        #             print "you don't have this card. please try again."
        #         #print "here are your cards: {}" .format(play1)
        #             userChoice = raw_input("enter the card you wish to play:")
        #     for i in range(0,len(play1)-1):
        #         while userChoice[0] not in play1[i] and userchoice[1] != 8:
        #             print "this is not the same suit as the top card. please try again."
        #             #print "here are your cards: {}" .format(play1)
        #             userChoice = raw_input("enter the card you wish to play:")
        #         while userChoice[1] not in play[i] and userchoice[1] != 8:
        #             print "this is not the same number as the top card. please tryagain."
        #            # print "here are your cards: {}" .format(play1)
        #             userChoice = raw_input("enter the card you wish to play:")
         
     
        

def compTurn(play1, comp1, cardPile, mainDeck):
    playWin, compWin = endProgram(play1,comp1)
    while playWin == False and compWin == False:
    
        sameNum, snList, sameSuit, ssList, haveEight, eList = cardValid(topCard, player)
    
        if sameNum == True:
            cardPile.append(snList)
            comp1.remove(snList)
            print(cardPile)
            topCard = snList[snList(len)-1]
            playWin, compWin = programEnd(play1,comp1)
            print(topCard)
            return cardPile
            return topCard
            return comp1
        elif sameSuit == True and sameNum == False:
            suitChoice = random.choice(ssList)
            cardPile.append(suitChoice)
            comp1.remove(ssList)
            print(cardPile)
            topCard = suitChoice
            playWin, compWin = programEnd(play1,comp1)
            print(topCard)
            return cardPile
            return topCard
            return comp1
        elif haveEight == True and sameSuit == False and sameNum == False:
            eightChoice = random.choice(eList)
            cardPile.append(eightChoice)
            comp1.remove(eight)
            print(cardPile)
            topCard = eightChoice
            playWin, compWin = programEnd(play1,comp1)
            print(topCard)
            return cardPile
            return topCard
            return comp1
    
def specialRun(topCard, sameNum, sameSuit, mainDeck, cardPile, comp1, play1):
    if 1 in topCard and sameNum == True or sameSuit == True:
        addOne = random.choice(mainDeck)
        mainDeck.remove(addOne)
        if len(cardPile)-1 % 2 == 0:
            comp1.append(addOne)
        else:
            play1.append(addOne)
                 
    if 2 in topCard and sameNum == True or sameSuit == True:
        for i in range(0,2):
            addTwo = random.choice(mainDeck)
            mainDeck.remove(addTwo)
        if len(cardPile)-1 % 2 == 0:
            comp1.append(addTwo)
        else:
            play1.append(addTwo)
                
    if 'QS' in topCard and sameNum == True or sameSuit ==True:
        for i in range(0,5):
            addFive = random.choice(mainDeck)
            mainDeck.remove(addTwo)
        if len(cardPile)-1 % 2 == 0:
            comp1.append(addTwo)
        else:
            play1.append(addTwo)
            
def drawCard(sameNum, sameSuit, haveEight, player, mainDeck):
    
    if sameNum == False and sameSuit == False and haveEight == False:
        pickCard = random.choice(mainDeck)
        mainDeck.remove(pickCard)
        player.append(pickCard)
    
        

def main():
    
    mainDeck, play1, comp1 = dealCard()
    topCard = firstCard(mainDeck)
    cardPile = []
    cardPile.append(topCard)
    print("The top card is {}").format(topCard)
    print("Your card pile consists of {}").format(cardPile)
    suit, number = cardValid(topcard, play1, comp1)
    print(suit)
    print(number)
    # cardValid(topcard, play1, comp1)

main()

#KARAN STARTS HERE

    
def firstCard(mainDeck):
    
    index = random.randint(0,22)
    topCard = mainDeck.pop(index)
    
    return topCard



def cardValid(topcard, player):
    
    suit = topCard[0]
    number = topCard[1]
    
    ssList = []
    snList = []
    eList = [] 
    # ssList2 = []
    # snList2 = []
    # eList2 = []
  
    sameNumLoc=-1
    for i in range(0,len(player)-1):
          if number in player[i] and sameNumLoc!=-1:
            sameNum == True 
            sameNumLoc = i
            snList.append( player[sameNumLoc])
            
          elif number not in player[i] and sameNumLoc!=-1:
            sameNum == False 
            
            
          elif suit in player[i] and sameNumLoc!=-1:
            sameSuit == True 
            sameNumLoc = i
            ssList.append(player[sameNumLoc])
            
          elif suit not in player[i] and sameNumLoc!=-1:
            sameSuit == False
            
          elif '8' in player[i] and sameNumLoc!=-1:
            haveEight == True
            sameNumLoc = i
            eList.append(player[sameNumLoc])
            
          elif '8' not in player[i] and sameNumLoc!=-1:
                haveEight == False
            
    # for k in range(0,len(comp1)-1):
    #     
    #     if number in comp1[k] and sameNumLoc != -1:
    #         sameNum == True
    #         sameNumLoc = k
    #         snList2.append(comp1[sameNumLoc])
    #         
    #     elif suit in comp1[k] and sameNumLoc!=-1:
    #         sameSuit == True
    #         sameNumLoc = k
    #         ssList2.append(comp1[sameNumLoc])
    #         
    #     elif '8' in comp1[k] and sameNumLoc!=-1:
    #         haveEight == True
    #         sameNumLoc = k
    #         eList2.append(comp1[sameNumLoc])
    if topcard.suit == 
            

        
        
    return sameNum,sameSuit,haveEight,ssList, snList, eList, 



main()

