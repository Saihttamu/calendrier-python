# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:48:16 2014

@author: Matthias

Ce programme définit une fonction jour_date() qui donne le jour de la semaine de la date rentrée.

On considère pour cela que:

    - la fonction jour_date() prend la date dans l'ordre et sous forme de trois arguments jour, mois, année de type int

    - l'année 0 n'existe pas: on passe de l'an -1 à l'an 1
    
    - une année a supérieure à 0 est bissextille si a est multiple de 4 et non multiple de 100 ou mutliple de 400
    
    - une année a inférieure à 0 est bissextille si (a+1) est multiple de 4 et non multiple de 100 ou multiple de 400
"""


def bissextile(a):
    assert a != 0, "L'année zéro n'existe pas!"
    assert type(a)==int, "Format d'année invalide"
    if a>0:
        return a%4==0 and a%100!=0 or a%400==0
    else:
        return (a+1)%4==0 and a%100!=0 or a%400==0


def get_year(a): # crée un dictionnaire représentant les mois de l'année a et leur nombre de jours correspondant
    assert a != 0, "L'année zéro n'existe pas!"
    assert type(a)==int, "Format d'année invalide: l'année doit être un entier"
    
    months = {}
    for month in range(1,13):
        if month < 8 and month%2==1 or month > 7 and month%2==0:
            months[month] = 31
            
        elif month==2:
            if bissextile(a):
                months[month] = 29
            else:
                months[month] = 28
        
        else:
            months[month] = 30
    return months



def jour_date(j,m,a):
    annee = get_year(a)
    assert m in annee and j in range(1,annee[m]+1), "La date rentrée est incorrecte"

    J,M,A = 21,8,1995 # date de référence: lundi
    ANNEE = get_year(A)
    jours = ("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")    
    ecart = 0 # écart en jours entre la date d'entrée et la date de référence
    annees = 0 # écart en années entre la date d'entréee et la date de référence
    nbrbiss = 0 
    
    for year in range(min(A,a)+1,max(A,a)): # on compte le nombre d'années bissextiles entre les deux dates
        if year!=0:
            annees+=1
            if bissextile(year):
                nbrbiss+=1
    
    ecart += annees*365 + nbrbiss
    
    if A < a:
        for mois in ANNEE:
            if mois > M:
                ecart += ANNEE[mois]
                
        for mois in annee:
            if mois < m:
                ecart += annee[mois]
        
        ecart += (ANNEE[M]-J) + j
    
    elif a < A:
        for mois in annee:
            if mois > m:
                ecart += annee[mois]
                
        for mois in ANNEE:
            if mois < M:
                ecart += ANNEE[mois]
                
        ecart += (annee[m]-j) + J
        ecart *= -1
    
    else: # A == a
        for mois in range(min(m,M),max(m,M)):
            ecart += annee[mois]
        if M<=m:
            ecart += j-J
        else:
            ecart += J-j
            ecart *= -1
    
    return jours[ecart%7]