# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:27:32 2020

@author: Steven Sachio
"""

import random as rd
from collections import Counter as ctr

"""
numdeck = 0
while numdeck == 0:
    numdeckinp = int(input ("How many decks do you want to play with? (Max 100) "))
    if (numdeckinp > 0 and numdeckinp <= 100):
        numdeck = numdeckinp
        Deck = numdeck*StoreDeck
        break
    print("")
    print ("Please input a number larger than 0 and smaller than 100")


numshuff = 0
while numshuff == 0:
    numshuffinp = int(input ("How many times do you want to shuffle this deck? "))
    if (numshuffinp > 0 and numshuffinp <= 1000):
        numshuff = numshuffinp
        for i in range(numshuffinp):
            rd.shuffle(Deck)
        break
    print("")
    print ("Please input a number larger than 0 and smaller than 1000")
"""

def getValue(hand,DeckDict):
    """
    Calculates the value of the person's hand
    Input: list of cards on hand
    Output: Int value of hand
    """
    hv = []
    if ("AH" in hand) or ("AC" in hand) or ("AS" in hand) or ("AD" in hand):
        counted = ctr(hand)
        NoAces = counted["AH"] + counted["AC"] + counted["AS"] + counted["AD"]
        for i in hand:
            hv.append(DeckDict[i])
        Value1 = sum(hv)
        Value2 = Value1
        for z in range(NoAces-1):
            Value2 -= 10
        Value3 = Value2-10
        if Value1 == 21:
            return Value1
        elif Value2 == 21:
            return Value2
        elif Value3 == 21:
            return Value3
        elif Value1 < 21:
            return Value1
        elif Value2 > 21:
            return Value3
        elif Value1 > 21:
            return Value2
    else:
        for i in hand:
            hv.append(DeckDict[i])
        Value = sum(hv)
        return Value


def PlayerAction(action, PlayerHand, DealerHand, Deck, DeckDict):
    if (action == "Hit") or (action == "hit") or (action == "H") or (action == "h"):
        PlayerHand.append(Deck.pop(0))
        print("")
        print("")
        print("BLACK JACK!")
        print("--------------------")
        print("")
        print("Dealer's Hand:", DealerHand)
        print("Value:", getValue(DealerHand, DeckDict))
        print("")
        print("")
        print("Player's Hand:", PlayerHand)
        print("Value:", getValue(PlayerHand, DeckDict))
        print("")
        print("")
        if getValue(PlayerHand, DeckDict) > 21:
            return "PB", PlayerHand, getValue(PlayerHand, DeckDict)
        return PlayerAction(input("Do you want to Hit or Stand? "), PlayerHand, DealerHand, Deck, DeckDict)
    elif (action == "Stand") or (action == "stand") or (action == "S") or (action == "s"):
        return "NORM", PlayerHand, getValue(PlayerHand, DeckDict)

def DealerAction(DealerHand,Deck, DeckDict):
    DealerHand.append(Deck.pop(0))
    if getValue(DealerHand, DeckDict) == 21:
        return "DBJ", DealerHand, getValue(DealerHand, DeckDict)
    while getValue(DealerHand, DeckDict) < 17 and getValue(DealerHand, DeckDict) != 21:
        DealerHand.append(Deck.pop(0))
        getValue(DealerHand, DeckDict)
    if getValue(DealerHand, DeckDict) > 21:
        return "DB", DealerHand, getValue(DealerHand, DeckDict)
    return "NORM", DealerHand, getValue(DealerHand, DeckDict)
    
def PlayBlackJack():
    DeckDict= {'AC': 11, '2C': 2, '3C': 3, '4C': 4, '5C': 5, '6C': 6, '7C': 7, '8C': 8, '9C': 9, 
       '10C': 10, 'JC': 10, 'QC': 10, 'KC': 10, 'AH': 11, '2H': 2, '3H': 3, '4H': 4, 
       '5H': 5, '6H': 6, '7H': 7, '8H': 8, '9H': 9, '10H': 10, 'JH': 10, 'QH': 10, 
       'KH': 10, 'AD': 11, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7, '8D': 8, 
       '9D': 9, '10D': 10, 'JD': 10, 'QD': 10, 'KD': 10, 'AS': 11, '2S': 2, '3S': 3, '4S': 4, 
       '5S': 5, '6S': 6, '7S': 7, '8S': 8, '9S': 9, '10S': 10, 'JS': 10, 'QS': 10, 'KS': 10}
    StoreDeck = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 
               'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 
               '10H', 'JH', 'QH', 'KH', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', 
               '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AS', '2S', '3S', '4S', '5S', 
               '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']
    Deck = []
    numdeck = rd.randrange(0,50)
    Deck = numdeck*StoreDeck
    numshuff = rd.randrange(0,50)
    for i in range(numshuff):
        rd.shuffle(Deck)
    PlayerHand = []
    DealerHand = []
    PlayerHand.append(Deck.pop(0))
    DealerHand.append(Deck.pop(0))
    PlayerHand.append(Deck.pop(0))
    PV = getValue(PlayerHand, DeckDict)
    DV = getValue(DealerHand, DeckDict)
    print("")
    print("")
    print("BLACK JACK!")
    print("GOOD LUCK!")
    print("")
    print("Dealer's Hand:", DealerHand)
    print("Value:", DV)
    print("")
    print("")
    print("Player's Hand:", PlayerHand)
    print("Value:", PV)
    print("")
    print("")
    if PV == 21:
        Flag, DealerHand, DV = DealerAction(DealerHand, Deck, DeckDict)
        if Flag == "DBJ":
            return print("")
            print("")
            print("BLACK JACK!")
            print("--------------------")
            print("")
            print("Dealer's Hand:", DealerHand)
            print("Value:", DV)
            print("")
            print("")
            print("Player's Hand:", PlayerHand)
            print("Value:", PV)
            print("")
            print("DEALER ALSO GOT BLACK JACK! ITS A TIE!")
        print("")
        print("")
        print("BLACK JACK!")
        print("--------------------")
        print("")
        print("Dealer's Hand:", DealerHand)
        print("Value:", DV)
        print("")
        print("")
        print("Player's Hand:", PlayerHand)
        print("Value:", PV)
        print("")
        print("YOU GOT BLACK JACK! CONGRATULATIONS YOU WON!")
        return 
    Flag, PlayerHand, PV = PlayerAction(input("Do you want to Hit or Stand? "), PlayerHand, DealerHand, Deck, DeckDict)
    if Flag == "PB":
        print("")
        print("")
        print("BLACK JACK!")
        print("--------------------")
        print("")
        print("Dealer's Hand:", DealerHand)
        print("Value:", DV)
        print("")
        print("")
        print("Player's Hand:", PlayerHand)
        print("Value:", PV)
        print("")
        print("BUSTED! GAME OVER!")
        return
    Flag, DealerHand, DV = DealerAction(DealerHand, Deck, DeckDict)
    if Flag == "DBJ":
        print("")
        print("")
        print("BLACK JACK!")
        print("--------------------")
        print("")
        print("Dealer's Hand:", DealerHand)
        print("Value:", DV)
        print("")
        print("")
        print("Player's Hand:", PlayerHand)
        print("Value:", PV)
        print("")
        print("DEALER GOT BLACK JACK! GAME OVER!")
        return
    elif Flag == "DB":
        print("")
        print("")
        print("BLACK JACK!")
        print("--------------------")
        print("")
        print("Dealer's Hand:", DealerHand)
        print("Value:", DV)
        print("")
        print("")
        print("Player's Hand:", PlayerHand)
        print("Value:", PV)
        print("")
        print("DEALER GOT BUSTED! YOU WON!")
        return
    elif Flag == "NORM":
        if PV > DV:
            print("")
            print("")
            print("BLACK JACK!")
            print("--------------------")
            print("")
            print("Dealer's Hand:", DealerHand)
            print("Value:", DV)
            print("")
            print("")
            print("Player's Hand:", PlayerHand)
            print("Value:", PV)
            print("")
            print("CONGRATULATIONS! YOU WON!")
            return
        elif PV == DV:
            print("")
            print("")
            print("BLACK JACK!")
            print("--------------------")
            print("")
            print("Dealer's Hand:", DealerHand)
            print("Value:", DV)
            print("")
            print("")
            print("Player's Hand:", PlayerHand)
            print("Value:", PV)
            print("")
            print("SAME HAND VALUES! ITS A TIE!")
            return
        else:
            print("")
            print("")
            print("BLACK JACK!")
            print("--------------------")
            print("")
            print("Dealer's Hand:", DealerHand)
            print("Value:", DV)
            print("")
            print("")
            print("Player's Hand:", PlayerHand)
            print("Value:", PV)
            print("")
            print("GAME OVER! YOU LOST!")
            return 

PlayBlackJack()