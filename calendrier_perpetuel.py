# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:48:16 2014

@author: Matthias
"""

def date(j,m,a):
    J,M,A=23,2,2013 # jour: samedi
    ka=0 # écart d'années
    km=0 # écart de mois
    
    for i in range(abs(a-A)): # pour chaque année on compte 365 ou 366 jours
        if (min(a,A)+i)%4==0 and (min(a,A)+i)%100!=0 or (min(a,A)+i)%400==0:
            ka+=366
        else:
            ka+=365
    
    for i in range(min(m,M),max(m,M)):
        if i<=7:
            if i%2==1: # mois impair: janvier, mars, mai, juillet
                km+=31
            elif i==2: # pour février
                if max(A,a)%4==0 and max(A,a)%100!=0 or max(A,a)%400==0: # on vérifie si c'est une année bissextile
                    km+=29
                else: # si ce n'est pas une année bissextile
                    km+=28
            else: # mois pair différent de février: avril, juin
                km+=30
        elif i%2==1: # i>=8
            km+=30
        else:
            km+=31
    
    if A<=a: # si l'année de référence est supérieure à la date entrée
        if M<=m: # si le mois de référence est supérieur au mois entré
            if J<=j:
                ka+=km+abs(J-j)
            else: 
                ka+=km-abs(J-j)
        elif J<=j: # avec M>m
            ka=ka-km+abs(J-j)
        else:
            ka=ka-km-abs(J-j)
            
    else: # A>a
        if M>m:
            if J<=j:
                ka=ka+km-abs(J-j)
            else:
                ka=ka+km+abs(J-j)
        elif J<=j: # M<=m
            ka=ka-km-abs(J-j)
        else:
            ka=ka-km+abs(J-j)
    
    if A<a or A==a and M<m or A==a and M==m and J<=j:
        if (ka)%7==0:
            return 'samedi'
        if (ka)%7==1:
            return 'dimanche'
        if (ka)%7==2:
            return 'lundi'
        if (ka)%7==3:
            return 'mardi'
        if (ka)%7==4:
            return 'mercredi'
        if (ka)%7==5:
            return 'jeudi'
        if (ka)%7==6:
            return 'vendredi'
    else:
        if (ka)%7==0:
            return 'samedi'
        if (ka)%7==1:
            return 'vendredi'
        if (ka)%7==2:
            return 'jeudi'
        if (ka)%7==3:
            return 'mercredi'
        if (ka)%7==4:
            return 'mardi'
        if (ka)%7==5:
            return 'lundi'
        if (ka)%7==6:
            return 'dimanche'