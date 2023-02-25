# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:08:54 2023

@author: Bahodir
"""
import random

def section1(x=10):
    tson = random.randint(1, x)
    taxminlar = 0
    print("Keling o`yin o`ynaymiz. Men 1-10 oralig`idagi bir sonni o`yladim. Aytingchi men qaysi sonni o`yladim")
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if taxmin > tson:
            print("Xato, Men kichikroq son o`yladim yana harakat qilib ko`ring")
        elif taxmin < tson:
            print("Xato, Men kattaroq son o`yladim yana harakat qilib ko`ring ")
        else:
            break
    print("Tabriklayman! Siz men o`ylagan sonni topdingiz!")
    print("Men o`ylagan son: ", tson)
    print(f"Urinishlar soni: {taxminlar}")      
    return taxminlar
 
def section2(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.\n>>>")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)\n>>>".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar




def play_area(x=10):
    savol = True
    while savol:
        taxminlar_user = section1(x)
        taxminlar_pc = section2(x)
        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} ta urinishda sonni topdim. Siz esa {taxminlar_user} ta urinishda topdingiz, Demak men yutdim!")
        elif taxminlar_pc == taxminlar_user:
            print(f"Durrang! ikkimiz ham sonni {taxminlar_pc} ta urnishda topdik")
        else:
            print(f"Qoyil! siz g`olibsiz, siz {taxminlar_user} ta urinishda, men esa {taxminlar_pc} ta urnishda topdim")
            savol = True
    
        savol = int(input("Yana o`ynaymizmi? Ha(1) yo`q(0) \n>>>"))

play_area()













