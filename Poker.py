#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:57:37 2020

@author: chrisgaughan
"""


from cards import Cards
import random



class Play(Cards):
    
    def __init__(self, players=1):
        self.players = players
        super().__init__()
        
    def deal(self,players=1, cards=1):
        #initial = self.deck
        random.shuffle(self.deck)
        self.hands = [self.deck[i:players *cards:players]
                      for i in range (players)]
        return self.hands
        
