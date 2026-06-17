# START 16.06.2026

# Plan invatare pentru 12 săptămâni, dar foarte orientat pe practică. La final trebuie să ai un repository GitHub care să poată fi arătat la interviu.

# Regula principală:
# 70% practică / 30% teorie
# Nu urmări cursuri 8 ore pe zi.

# Formula ideală:
# 2h învățare
# 5-6h practică și cod în fiecare zi.

# Săptămâna 1
# Python Fundamentals
# Ziua 1

# Învață:

# instalare Python
# VS Code
# terminal
# variabile
# print()

# Exerciții:

# afișare nume
# calculator simplu
# Ziua 2

# Învață:

# string
# int
# float
# bool

# Exerciții:

# age = 30
# name = "Alex"

# Construiește:

# calculator vârstă
# convertor temperatură
# Ziua 3

# Învață:

# if
# elif
# else

# Exerciții:

# validator vârstă
# validator parolă
# Ziua 4

# Învață:

# for
# while

# Exerciții:

# tabel înmulțire
# numere pare
# Ziua 5

# Învață:

# funcții
# def suma(a, b):
#     return a + b

# Exerciții:

# calculator modular
# Ziua 6

# Învață:

# liste
# tuple
# set

# Exerciții:

# listă utilizatori
# căutare utilizator
# Ziua 7

# Recapitulare.

# Construiește:

# mini-project
# User Management Console App

# GitHub:

# git init
# git add .
# git commit -m "week1 project"
# Săptămâna 2
# Python pentru Automation
# Ziua 1

# Dicționare

# user = {
#     "username": "alex",
#     "role": "admin"
# }
# Ziua 2

# Fișiere

# open()
# read()
# write()

# Exercițiu:

# scriere raport test
# Ziua 3

# JSON

# Foarte important pentru API Testing.

# import json

# Citește și modifică JSON-uri.

# Ziua 4

# Excepții

# try:
# except:
# Ziua 5

# Module

# import
# from
# Ziua 6

# Virtual Environments

# python -m venv venv
# Ziua 7

# Mini proiect:

# Test Data Generator

# Generează:

# email
# username
# password
# Săptămâna 3
# OOP

# Învață:

# class
# object
# inheritance
# Exemplu
# class User:
#     def __init__(self, name):
#         self.name = name

# class Admin(User):
#     pass

# Proiect:

# Banking App Simulation

# Obiectiv:

# să înțelegi exact cum vor funcționa Page Objects.

# Săptămâna 4
# Git + pytest
# Git

# Învață:

# git clone
# git pull
# git push
# git branch
# git merge
# pytest

# Instalează:

# pip install pytest

# Primul test:

# def test_sum():
#     assert 2 + 2 == 4

# Rulează:

# python -m pytest

# Nu pytest direct dacă PATH-ul încă nu este configurat.

# Obiectiv

# 20 teste pytest.

# Săptămâna 5
# pytest Advanced

# Învață:

# fixtures
# markers
# parametrization
# conftest.py

# Exemplu:

# @pytest.mark.parametrize(
#     "a,b,result",
#     [
#         (1,2,3),
#         (2,3,5)
#     ]
# )
# Săptămâna 6
# Playwright

# Instalare:

# pip install playwright
# playwright install

# Primul test:

# from playwright.sync_api import sync_playwright

# Învață:

# browser
# page
# goto
# click
# fill

# Scenarii:

# login valid
# login invalid
# Săptămâna 7
# Playwright Practic

# Automatizează:

# SauceDemo

# Sauce Demo

# Scenarii:

# login
# logout
# add to cart
# remove from cart

# Obiectiv:

# 10-15 teste UI.

# Săptămâna 8
# Page Object Model

# Structură:

# project/
# │
# ├── pages/
# ├── tests/
# ├── utils/

# Exemplu:

# class LoginPage:
#     pass

# La final:

# toate testele folosesc Page Objects
# Săptămâna 9
# API Testing

# Instalează:

# pip install requests

# Învață:

# GET
# POST
# PUT
# DELETE

# Folosește:

# JSONPlaceholder

# Teste:

# create user
# update user
# delete user
# Săptămâna 10
# API Framework

# Structură:

# api/
# tests/
# utils/

# Adaugă:

# test data
# sessions
# helpers
# Săptămâna 11
# GitHub + CI

# Creează repository.

# Învață:

# git remote
# git push
# pull request
# Săptămâna 12
# GitHub Actions

# Workflow:

# push
# ↓
# run tests
# ↓
# generate report

# La final trebuie să ai:

# qa-automation-framework/
# │
# ├── pages/
# ├── tests/
# ├── api/
# ├── utils/
# ├── reports/
# ├── .github/workflows
# ├── requirements.txt
# └── README.md
# Obiectiv final

# După 12 săptămâni trebuie să poți răspunde la interviu la întrebări precum:

# Ce este Page Object Model?
# De ce folosești pytest?
# Cum gestionezi waits?
# Cum structurezi un framework?
# Cum rulezi testele în CI/CD?
# Care este diferența dintre Playwright și Selenium?

# Dacă urmezi acest plan serios, după primele 6-8 săptămâni vei putea deja să automatizezi scenarii reale și să începi să aplici la roluri de QA Automation Junior/Mid. În paralel, putem folosi conversația asta ca jurnal: îmi spui în fiecare zi ce ai făcut și îți spun exact ce să studiezi în ziua următoare.


#*****************************************************************************************************************
# ------------------------------------------ CAPITOLUL 1 - Primele notiuni ---------------------------------------
#*****************************************************************************************************************

# print("Primul meu program.")

# print("Introdu numele utilizatorului")
# n = input() #numele utilizatorului
# print("Introdu numele utilizatorului")
# p = input() #numele utilizatorului
# #mai jos este afisat numele complet
# print(n + " " + p)

# n = input("n=")
# m = input("m=")
# print(n+m)

# numar = int(4)
# print(numar)
# numar = str
# type(numar)

# v1, v2, v3 = input("v1="), input("v2="), input("v3=")
# print(v1,v2,v3)
# print(type(v1))

# x = 3*(4+2)
# print(x)
# print(type(x))

# print((2+3*(2+1))*2)

# print(7/2)
# print(-7/2)
# print(7.0/2)
# print(-7.0/2)
# print(6/2)
# print(6.2/2)

# print ("Introdu un numar natural!")
# numar_natural = int(input())
# print (numar_natural * 5)

# print ("Introdu un prim numar natural!")
# primul_numar_natural = int(input())
# print ("Introdu al doilea numar natural!")
# al_doilea_numar_natural = int(input())
# print("Catul intreg al celor doua numere naturale introduse este: ", primul_numar_natural//al_doilea_numar_natural)
# print("Restul impartirii celor doua numere naturale introduse este: ", primul_numar_natural%al_doilea_numar_natural)

# print ("Introdu un numar natural pentru care vrei sa inveti tabla inmultirii cu acesta!")
# numar_natural = int(input())
# print("", numar_natural, 'inumltit cu 1 este egal cu ', numar_natural*1, "\n",
#       numar_natural, 'inumltit cu 2 este egal cu ', numar_natural*2, "\n",
#       numar_natural, 'inumltit cu 3 este egal cu ', numar_natural*3, "\n",
#       numar_natural, 'inumltit cu 4 este egal cu ', numar_natural*4, "\n",
#       numar_natural, 'inumltit cu 5 este egal cu ', numar_natural*5, "\n",
#       numar_natural, 'inumltit cu 6 este egal cu ', numar_natural*6, "\n",
#       numar_natural, 'inumltit cu 7 este egal cu ', numar_natural*7, "\n",
#       numar_natural, 'inumltit cu 8 este egal cu ', numar_natural*8, "\n",
#       numar_natural, 'inumltit cu 9 este egal cu ', numar_natural*9)

# print ('Introdu un numar natural pentru care vrei sa afli cu cat este egal acesta la puterea a doua si a treia!')
# n = int(input())
# print(n, 'la puterea a doua este egal cu', n**2)
# print(n, 'la puterea a treia este egal cu', n**3)

# print ("Introdu o prima cifra nenula!")
# n_01 = input()
# print ("Introdu o a doua cifra nenula, diferita de prima introdusa!")
# n_02 = input()
# print ("Cu ", n_01, "si", n_02, "se pot forma urmatorele 2 numere: ", (n_01 + n_02), "si", (n_02 + n_01))

# print('''
#       *********
#       * @   @ *
#       *   *   *
#       *  \_/  *
#       *********
#       ''')


#*****************************************************************************************************************
# -------------------------------------------- CAPITOLUL 2 - Expresii --------------------------------------------
#*****************************************************************************************************************


# numar = int(input("Introduceti un numar: "))
# print("Numarul introdus de tine este:", numar)
# print("Este ", numar, ">=0 ?", numar>=0)

# numar = bool(int(input("Introduceti un numar: ")))
# print("Este numarul introdus de tine diferit de 0 ?", numar)

# v = int(input("Introduceti o cifra: "))
# v += 2
# print(v)
# v -= 2
# print(v)
# v *= 2
# print(v)
# v **= 2
# print(v)
# v //= 2
# print(v)
# v %= 2
# print(v)
# v /= 2
# print(v)

# exp = eval(input())
# print(exp)
# print(type(exp))

# str1 = ""
# str2 = "a"
# str3 = "Salut!"
# print("", len(str1), "\n",
#       len(str2), "\n",
#       len(str3))

# numar = int(input("Introdu un numar din trei cifre: "))
# c1 = numar%10
# print(c1)
# numar = numar // 10
# c2 = numar%10
# print(c2)
# numar= numar//10
# c3 = numar
# print(c3)
# rez = c1*100 + c2*10 + c3
# print("Rezultatul este:", rez)

# t = float(input("timp (secunde)= "))
# v = float(input("viteza (m/s)= "))
# print("Distanta parcursa este: ", t*v,"m",sep="")
# print("Distanta parcursa este: ", t*v,"m")

# lungime = int(input("Introduceti o lungime exprimata in milimetri: "))
# print('lungime[SI] = ', lungime/1000, 'm', sep='')

# n = int(input("Introduceti un numar natural: "))
# print('Suma primelor n numere este: ', n*(n+1)/2)

# E = 1/2 + 1/3 + 1/4
# print(E)
# E = (1/(2*3)) + (1/(3*4)) + (1/(4*5))
# print(E)
# E = ((1+2)/(3+4)) + (5+6)/(7+8) + (9+10)/(11+12)
# print(E)

# x = 7
# x = x+1.5
# print(x)
# print(type(x))

# x = 4
# x = x <= 4
# print(x)
# print(type(x))

# x = 1
# print(x+7 == 8*x)
# print(2*x+3 == 6)

# a = 2
# b = 5
# a += b+1
# print(a)

# numar = int(input("Introdu un numar din 4 cifre: "))
# c4 = numar%10
# numar = numar // 10
# c3 = numar%10
# numar = numar // 10
# c2 = numar%10
# numar = numar // 10
# c1 = numar
# rez = (c4*1000) + (c3*100) + (c2*10) + c1
# print(rez)

# numar = int(input('Introduceti un numar din exact 3 cifre: '))
# c3 = numar%10
# numar = numar // 10
# c2 = numar%10
# numar = numar // 10
# c1 = numar
# print(c2, c1, c3, sep="")

# numar = int(input('Introduceti un numar din exact 2 cifre: '))
# c2 = numar%10
# numar = numar // 10
# c1 = numar
# print(c1**2 + c2**2)

# numar = int(input('Introduceti un numar din 5 cifre: '))
# c5 = numar%10
# numar = numar // 10
# c4 = numar%10
# numar = numar // 10
# c3 = numar%10
# numar = numar // 10
# c2 = numar%10
# numar = numar // 10
# c1 = numar
# s = (c1+c2+c3+c4+c5)
# p = (c1*c2*c3*c4*c5)
# # s = (n*(n+1))/2 // Suma tuturor numerelor pana la 0 la n
# print("", s, '\n', p)

# elev1 = float(input("Introduceti media generala: "))
# elev2 = float(input("Introduceti media generala: "))
# elev3 = float(input("Introduceti media generala: "))
# elev4 = float(input("Introduceti media generala: "))
# elev5 = float(input("Introduceti media generala: "))
# media_generala_elevi = ((elev1 + elev2 + elev3 + elev4 + elev5) / 5)
# print(media_generala_elevi)

# n = int(input('Introduceti un prim numar natural: '))
# m = int(input('Introduceti un al doilea numar natural: '))
# s = 2**(n+m)
# print(s)


#*****************************************************************************************************************
# ----------------------------------- CAPITOLUL 3 - Fara OOP nu putem continua... --------------------------------
#*****************************************************************************************************************

#Definitii
#Prin incapsulare intelegem mecanismul prin care datele (variabilele) si functiile (numite in acest caz si metode)
#sunt plasate impreuna, intr-o unica structura, numita clasa.

#Un obiect este instantierea unei clase efectuata de un constructor.
#Clasa are incapsulate date si metode proprii care sunt structurate abstract.


#*****************************************************************************************************************
# ---------------------------------------- CAPITOLUL 4 - Siruri de caractere -------------------------------------
#*****************************************************************************************************************

# sir1 ='ab'
# print((sir1 + " ")*4)

# s1 ='sir de caractere'
# print(s1[0])
# print(s1[0:5])

# s = input('Introducetei un sir de caractere: ')
# print(len(s))
# # print(s[15],s[14],s[13],s[12],s[11],s[10],s[9],s[8],s[7],s[6],s[5],s[4],s[3],s[2],s[1],s[0],sep="")
# print(s[::-1])
# print(s[::-2])
# print(s[len(s)-1::-1])

# a = 'Imi place programarea'
# print('place programare' in a)

# a = input('Introduceti numele marii preferate: ')
# a = a.lower()
# print(a.capitalize())
# print(a)
# print(a.strip())

#Program numarare si calcul total vocale dintr-o propozitie data.
# propozitie = input("Scrie propozitia ta preferata: ")
# print("Textul introdus este:", propozitie)
# a = propozitie.count("a")
# e = propozitie.count("e")
# i = propozitie.count("i")
# o = propozitie.count("o")
# u = propozitie.count("u")
# print("Vocale:")
# print("a - ", a)
# print("e - ", e)
# print("i - ", i)
# print("o - ", o)
# print("u - ", u)
# vocale = a + e + i + o + u
# print("Total vocale:", vocale)

# sir_de_caractere = input("Scrie citatul tau preferat: ")
# print("Citatul tau preferat are", len(sir_de_caractere), "de caractere!")
# print(sir_de_caractere.count("c"))
# print(sir_de_caractere.find("c"))
# print("Citatul incepe cu C ? -", sir_de_caractere.startswith("C"), "\nCitatul incepe cu c ? -", sir_de_caractere.startswith("c"))
# print("Citatul se termina cu '.' ? -", sir_de_caractere.endswith("."), "\nCitatul se termina cu '!' ? -", sir_de_caractere.endswith("!"))
# print("Citatul introdus are lungimea mai mare sau egal cu 43 de caractere ? -", len(sir_de_caractere) > 20)

# c1 = input('Introduceti o prima cifra nenula: ')
# c2 = input('Introduceti o a doua cifra nenula: ')
# print(c1, c2, sep="")
# print(c2, c1, sep="")

# oras = input("Introduceti un nume de oras: ")
# tara = input("Introduceti un numele unei tari: ")
# cifra = input("Introduceti o cifra: ")
# propozitie = "Super! Si eu am vizitat {}, iar in {} am petrecut minunat {} zile."
# propozitie = "Super! Si eu am vizitat {1}, iar in {0} am petrecut minunat {2} zile."
# print(propozitie.format(oras, tara, cifra))

# nume = input("Introduceti numele dumneavoastra: ")
# prenume = input("Introduceti prenumele dumneavoastra: ")
# nume = nume.lower()
# print(prenume.capitalize(), nume.upper())

# s1 = input("Introduceti un nume de fruct: ")
# s2 = input("Introduceti un al doilea nume de fruct: ")
# s3 = input("Introduceti un al treilea nume de fruct: ")
# print(s1, s2, s3, sep="")

# sir_numere = input("Introduceti un sir de numere: ")
# print(sir_numere.isdecimal()) #Daca intre numere sunt spatii rezultatul va fi false din cauza lor
# sir_numere2 = input("Introduceti un sir de numere si litere: ")
# print(sir_numere2.isdecimal())

# sir_de_caractere = input("Introduceti un sir de caractere: ")
# print(sir_de_caractere[0] == sir_de_caractere[-1])
# sir_de_caractere = sir_de_caractere.capitalize()
# print(sir_de_caractere)
# print(sir_de_caractere[::-1])


#*****************************************************************************************************************
# ---------------------------------------- CAPITOLUL 5 - Colectii de date ----------------------------------------
#*****************************************************************************************************************

#LISTE
# lista1 = ['Audi', 'BMW', 'Ford', 'Opel']
# print(lista1[0])
# print(lista1[-1])
# print(lista1[0:2])
# print(lista1[1:3])
# print(lista1[1:])
# print(lista1[::-1]) #citirea elementelor de la cap la coada folosind index
# lista1[0] = 'Dacia' #inlocuirea unui element din lista cu un altul
# print(lista1)
# print(lista1.pop()) #sterge ultimul element din lista daca nu este dat un argument si il si afiseaza. Cu argument sterge elementul de la indexul specificat.
# print(lista1)
# del lista1[2]
# print(lista1)
# lista1.append('Trabant') #adauga un element la finalul listei
# print(lista1)
# lista1.append(['Citroen', 'Renault']) #adauga un nou obiect, care este o lista
# print(lista1)
# print(lista1[3][0]) #din lista mare se afiseaza de la indexul 3 doar elementul de la index-ul 0 al obiectului(listei mici)
# print(lista1[3])
# nr_elem_lista1 = lista1.__len__()
# print(nr_elem_lista1)
# lista1.insert(4, 1) #adauga la pozitia 4 un nou element
# print(lista1)
# lista1.extend([1, 2, 3, 4]) #adauga la sfarsitul listei mai multe elemente
# lista2 = [5, 6, 7, 8]
# lista1.extend(lista2)
# print(lista1)
# print('Dacia' in lista1) #cauta un element in lista
# print('Dacia' not in lista1)
# print(sum(lista2, 4)) #calculeaza suma elementelor unei liste daca acestea sunt valori numerice si adauga o valoare dorita la suma lor
# del lista1
# print(list1)

#EXERCITII PROPUSE
# prenume = ['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio']
# varsta = [14, 23, 15, 14, 12, 41, 39]

# print(prenume[0] + ' are ' + 'varsta de ' + str(varsta[0]) + " ani.")
# print(prenume[1], 'are', 'varsta de', varsta[1], "ani.")
# print(prenume[2], 'are', 'varsta de', varsta[2], "ani.")
# print(prenume[3], 'are', 'varsta de', varsta[3], "ani.")
# print(prenume[4], 'are', 'varsta de', varsta[4], "ani.")
# print(prenume[5], 'are', 'varsta de', varsta[5], "ani.")
# print(prenume[6], 'are', 'varsta de', varsta[6], "ani.")

# prenume.extend(['Andreea', 'Ioan'])
# varsta.extend([34, 23])
# print(prenume)
# print(varsta)

# prenume.pop(2)
# varsta.pop(2)
# print(prenume)
# print(varsta)

# prenume.sort()
# varsta.sort()
# print(prenume)
# print(varsta)
# prenume.sort(reverse=True)
# varsta.sort(reverse=True)
# print(prenume)
# print(varsta)

# del varsta
# print(varsta)

# print(prenume[0:3])

# print(prenume[-1])

# print(prenume[::-1])

# prenume2 = ['Petru', 'Alin', 'Alex', 'Alina', ' Maria']
# prenume.extend(prenume2)
# print(prenume)

# print(prenume[2])
# print(prenume[4])
# print(prenume[0:5])

#TUPLURI - ca listele, doar ca nu se pot adauga, modifica sau sterge elementele. Un truc pentru a le modifica e conversia explicita la liste, apoi modificare element dorit si apoi conversie la loc in tuple
#        - are doar 2 metode: .count si .index
# pers1 = ('Mihai', 'Stamate', 26, 1.82, 'Oradea', 'Bihor')
# pers2 = ('Dana', 'Petrisor', 22, 1.64, 'Viscri', 'Brasov')

# print(pers1)
# print(pers2)

# print('Mihai' in pers1)

#SETURI
# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set1)

# set2 = {5.5, 4, 2, 7.2, 'text', ('un', 'tuplu')}
# print(set2)

# set1.add(12)
# print(set1)

# set1.update((14, 17, 19))
# print(set1)

#DICTIONARE
# antonime = {'inalt' : 'scund',
#             'frumos' : 'urat',
#             'mare' : 'mic',
#             'rapid' : 'lent',
#             'greu' : 'usor'}

# print(antonime)
# print(antonime['inalt'])


#*****************************************************************************************************************
# -------------------------------- CAPITOLUL 6 - Instructiunile limbajului Python --------------------------------
#*****************************************************************************************************************

#If, if .. else

# n1 = int(input("Introduceti un numar intreg cu semn: "))
# n2 = int(input("Introduceti un al doilea numar intreg cu semn: "))
# if n1 > n2:
#     print('n1 este mai mare ca n2')
# else:
#     print('n2 este mai mare ca n1')

# n_real = float(input('Introduceti un numar real: '))
# print(n_real)
# if n_real > 0:
#     print(n_real)

#If, elif .. else
# n = int(input('Introduceti un numar intreg: '))
# m = int(input('Introduceti un al doilea numar intreg: '))
# if n > m:
#     print('n este mai mare ca m')
# elif n == m:
#     print('n este egal cu m')
# else:
#     print('n este mai mic ca m')

# n = int(input('Introduceti un numar natural: '))
# if n == 0:
#     a = int(input('Introduceti un numar intreg: '))
#     b = int(input('Introduceti un al doilea numar intreg: '))
#     print(a+b)
# else:
#     x = float(input('Introduceti un numar real: '))
#     y = float(input('Introduceti un al doilea numar real: '))
#     print(x*y)

#PROBLEME REZOLVATE
# valoare = int(input('Introduceti un numar intreg: '))
# print(valoare%2)
# if valoare%2==0:
#     print('Am citit un numar par.')
# else:
#     print('Am citit un numar impar.')

# a = float(input('Introduceti un numar:'))
# b = float(input('Introduceti un al doilea numar:'))
# c = float(input('Introduceti un al treilea numar:'))
# d = float(input('Introduceti un al patrulea numar:'))
# if c+d > 0:
#     print(a+b)
# elif c+d == 0:
#     print(a-b)
# else:
#     print(a*b)

#Forma corecta, dar lipsita de eleganta
# x = int(input('Introduceti un numar intreg: '))
# if x < 0:
#     print(x+1)
# else:
#     print(x-1)
#Forma corecta si eleganta
# x = int(input('Introduceti un numar intreg: '))
# if x < 0:
#     E = x+1
# else:
#     E = x-1
# print(E)

# verificare_inmultire = int(input('Cat fac 7x8 ? - '))
# if verificare_inmultire != 56:
#     rezultat_inmultire = 'Gresit!'
# else:
#     rezultat_inmultire = 'Corect!'
# print(rezultat_inmultire)

# x = float(input('Introduceti un numar: '))
# if x < 0:
#     f = x
# elif x < 10:
#     f = 2*x
# elif 10 <= x < 100:
#     f = 3*x
# else:
#     f = 4*x
# print(f)

# a = int(input('Introduceti un numar intreg: '))
# b = int(input('Introduceti un al doilea numar intreg: '))
# c = int(input('Introduceti un al treilea numar intreg: '))
# if a%2 == 0:
#     a = 'a este numar par'
# else:
#     a = 'a este numar impar'
# if b%2 == 0:
#     b = 'b este numar par'
# else:
#     b = 'b este numar impar'
# if c%2 == 0:
#     c = 'c este numar par'
# else:
#     c = 'c este numar impar'
# print(a, "\n",
#       b, '\n',
#       c, sep="")

# a = int(input('Introduceti un numar intreg: '))
# b = int(input('Introduceti un al doilea numar intreg: '))
# c = int(input('Introduceti un al treilea numar intreg: '))
# p = 0
# if a%2==0:
#     p = p+1 #sau p += 1
# if b%2==0:
#     p = p+1 #sau p += 1
# if c%2==0:
#     p = p+1 #sau p += 1
# print('Numere pare: ', p)

# x = int(input('Introduceti un numar intreg: '))
# y = int(input('Introduceti un al doilea numar intreg: '))
# z = int(input('Introduceti un al treilea numar intreg: '))
# r = 0
# c = 0
# rasp = 0
# if x%3==0 and y%3==0 and z%3==0:
#     r += 1
# if x%2==0:
#     c += 1
# if y%2==0:
#     c += 1
# if z%2==0:
#     c += 1
# if c==2:
#     rasp += 1
# if x>10 and y>10 and z>10:
#     rasp += 1
# print('Au fost indeplinite: ', rasp, ' conditii!')

# a = int(input('Introduceti un numar intreg: '))
# b = int(input('Introduceti un al doilea numar intreg: '))
# c = int(input('Introduceti un al treilea numar intreg: '))
# d = int(input('Introduceti un al patrulea numar intreg: '))

# if a != b and a != c and a != d and b != c and b != d and c != d:
#     print('Toate numerele sunt diferite!')
# else:
#     print('Numerele nu sunt diferite!')

# lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = int(input('Introduceti un numar intreg: '))
# print(x in lista1)

# x = int(input('Numarul este: '))
# dict1 = {
#     1:'unu',
#     2:'doi',
#     3:'trei',
#     4:'patru',
#     5:'cinci',
#     6:'sase',
#     7:'sapte',
#     8:'opt',
#     9:'noua',
# }
# if x in dict1:
#     print(dict1[x])
# else:
#     print('Nu este intre 1 si 9!')

# x = int(input('Numarul este: '))
# lista1 = ['unu', 'doi', 'trei', 'patru', 'cinci', 'sase', 'sapte', 'opt', 'noua']
# if x > 0 and x < 10:
#     print(lista1[x-1])
# else:
#     print('Nu este intre 0 si 9')

# n = int(input('Introduceti un numar: '))
# if n < 0:
#     print('Numarul introdus este negativ!')
# else:
#     print('Numarul introdus este pozitiv!')

# a = float(input('Introduceti un prim numar real: '))
# b = float(input('Introduceti un al doilea numar real: '))
# c = float(input('Introduceti un al treilea numar real: '))
# if a <= 0 and b <= 0 and c <= 0:
#     print('Cu numerele reale introduse nu se poate forma un triunghi!')
# if a+b > c and b + c > a and c + a > b:
#     print('Numerele reale introduse pot fi laturile unui triunghi!')
# else:
#     print('Cu numerele reale introduse nu se poate forma un triunghi!')

# e = int (input('Introduceti un numar intreg: '))
# f = int(input('Introduceti un al doilea numar intreg: '))
# g = int(input('Introduceti un al treilea numar intreg: '))

# if e == f + g:
#     print(e, 'este egal cu suma celorlalte 2 numere introduse!')
# elif f == g + e:
#     print(f, 'este egal cu suma celorlalte 2 numere introduse!')
# elif g == e + f:
#     print(g, 'este egal cu suma celorlalte 2 numere introduse!')
# else:
#     print('Niciun numar dintre cele introduse nu este egal cu suma celorlalte 2')

# x = float (input ('Introduceti un numar real: '))
# if x <= 10:
#     F = x**2 + x - 2
# elif 10 < x <= 20:
#     F = 1 / x
# else:
#     F = (x-1)/(x+1)
# print (F)

# l = int (input('Introduceti un prim numar intreg: '))
# m = int (input('Introduceti un al doilea numar intreg: '))
# n = int (input('Introduceti un al treilea numar intreg: '))
# lista1 = [l, m, n]
# lista1.sort(reverse= True)
# print(lista1)

# h = int (input('Introduceti un prim numar natural din 4 cifre: '))
# j = int (input('Introduceti un al doilea numar natural din 4 cifre: '))
# h_c4 = h%10
# j_c4 = j%10
# if h_c4 > j_c4:
#     print(h)
# else:
#     print(j)

# n1 = int(input('Introduceti un prim numar natural: '))
# n2 = int(input('Introduceti un al doilea numar natural: '))
# if n1%n2 == 0:
#     print("Primul numar natural introdus este divizibil cu cel de-al doilea!")
# else:
#     print("Primul numar natural introdus nu este divizibil cu cel de-al doilea!")

# n1 = int(input('Introduceti un numar natural format din doua cifre: '))
# c2 = n1 % 10
# n1 = n1 // 10
# c1 = n1
# suma_cifre  = c1 + c2
# if suma_cifre % 2 == 0:
#     print('Suma cifrelor numarului introdus este para!')
# else:
#     print('Suma cifrelor numarului introdus este impara!')

# vocale = ['a', 'e', 'i', 'o', 'u']
# litera = input('Introduceti o litera: ')
# if litera in vocale:
#     print(litera, 'este o vocala!')
# else:
#     print(litera, 'este o consoana!')
# sir = input('Introduceti un cuvant: ')
# if sir[0] in vocale:
#     print('Prima litera din cuvantul introdus este o vocala')
# else:
#     print('Prima litera din cuvantul introdus este o consoana')
# if sir[-1] in vocale:
#     print('Ultima litera din cuvantul introdus este o vocala')
# else:
#     print('Ultima litera din cuvantul introdus este o consoana')

#----- Instructiunea repetitiva FOR -----#
# lista1 = ['a', 'b', 'c', 'd', 'e']
# lista2 = [1, 2, 3, 4, 5]
# suma = 0
# for x in lista1:
#     print(x)
# for x in lista2:
#     if x%2==0:
#         print(x)
# for x in lista2:
#     if x%2!=0:
#         suma += x
# print(suma)

# sir1 = 'Imi place Python!'
# vocale = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
# lista = []
# for c in sir1:
#     print(c)
# for c in sir1:
#     lista.append(c)
#     if c in vocale:
#         print(c)
# print(lista)

# dict1 = {1:'a', 2:'b', 3:'c'}
# for c in dict1:
#     print(c)
#     print(dict1.get(c))
# for c in dict1:
#     print(dict1.get(c), 'are cheia', c)
# for c in dict1:
#     print(dict1[c], 'are cheia', c)
# print(dict1.values())
# print(dict1.items())

#----- PROBLEME REZOLVATE -----#
# n = int(input('Introduceti un numar natural: '))
# S = 0
# for n in range(n+1):
#     S += n
# print(S)

# n = int(input('Introduceti un numar natural: '))
# p = 1
# s = 0
# for n in range(1, n+1):
#     p = p * n
#     s = s + p
# print(s)

#----- Citirea colectiilor de date de la tastatura -----#
#----- Exercitii propuse -----#

# s = int(input('Suma pe care doriti sa o depuneti: '))
# d = 5
# p = int(input("Pentru ce perioada doriti sa puneti (luni): "))
# d_calculata_pe_luna = d / 100 * s
# suma_totala = s + (p*d_calculata_pe_luna)
# print("Dupa", p, 'luni, suma totala va fi de ', suma_totala, 'lei!')

#----- Instructiunea repetitiva WHILE -----#

# n = int (input('n = '))
# s = (n * (n+1)) / 2
# s = 0
# x = 1
# while x <= n:
#     s = s + x
#     x = x + 1
#     print(s)
# print('Suma este:', s)

#----- Clauzele break si continue -----#
# BREAK
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for x in lista:
#     if x == 'd':
#         break
# print(x)

# CONTINUE
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for x in lista:
#     if x == 'd':
#         continue
#     print(x)

#*****************************************************************************************************************
# --------------------------------------- CAPITOLUL 7 - La voia intamplarii --------------------------------------
#*****************************************************************************************************************

import random

# for x in range(5):
#     print(random.random())

# numar = random.randint(1,100)
# incercari = 0
# ghicit = int(input())
# while numar != ghicit:
#     if ghicit > numar: print("Este mai mic")
#     else: print("Este mai mare!")
#     incercari += 1
#     ghicit = int(input())
# incercari += 1
# print("Felicitari, ai ghicit numarul din ", incercari, "incercari!")

#*****************************************************************************************************************
# --------------------------------------- CAPITOLUL 8 - Functii si module ----------------------------------------
#*****************************************************************************************************************

# n = int(input("Introduceti un numar natural: "))
# def subp(x):
#     s = 0
#     for i in range(x):
#         s += 1/(i+1)
#     return s
# print(subp(n))

# def creare_lista():
#     n = int(input('Numar de elemente: '))
#     lista_locala = []
#     for i in range(n):
#         elem = input('Elementul ' + str(i) + 'este: ')
#         lista_locala.append(elem)
#     return lista_locala

#EXERCITII ChatGPT
# Calculator varsta
# an_nastere = int(input('Introduceti anul nasterii: '))
# calculator_varsta = 2026 - an_nastere
# print("Varsta dumneavoastra este de", calculator_varsta, "de ani!")

#Convertor temperatura
# temperatura_fahrenheit = float(input('Introduceti temperatura afisata pe termometru in grade fahrenheit: '))
# convertor_temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
# print(convertor_temperatura_celsius)
# print("Temperatura in grade celsius este de", round(convertor_temperatura_celsius, 1), "!")

#-Conversie metri -> centimetri
# lungime_m = float(input("Introduceti lungimea in metri: "))
# lungime_cm = lungime_m * 100
# print('Lungimea in centimetri este de', int(lungime_cm), '!')

#-Calculator IMC
# greutate = float(input("Introduceti greutatea dumneavoastra exprimata in kilograme: "))
# inaltime = float(input("Introduceti inaltimea dumneavoastra exprimata in metri: "))
# imc = greutate/inaltime**2
# print("Indicele dumneavoastra de masa corporala este", round(IMC, 1), "!")

#-Calculator salariu anual
# salariu_lunar = int(input("Introduceti salariul dumneavoastra net lunar in lei: "))
# salariu_anual = salariu_lunar*12
# print('Salariul dumneavoastra anual net este de', salariu_anual, 'lei!')

#-Validator varsta
# varsta = int(input('Introduceti varsta dumneavoastra: '))
# if varsta >= 18:
#     print('Acces permis!')
# else:
#     print('Acces interzis!')

#-Validator parola
# parola = 'Alex12!'
# verifica_parola = input('Introduceti parola: ')
# if verifica_parola == parola:
#     print('Autentificare cu succes!')
# else:
#     print('Parola gresita!')

#-Autentificare
# username = 'alexandru'
# password = 'cheieacces'
# user_input = input('Introduceti numele utilizatorului: ')
# pass_input = input('Introduceti parola: ')
# if user_input == username and pass_input == password:
#     print('Login reusit!')
# elif :
#     print('Numele sau parola sunt gresite!')

#-Major/Minor
# varsta = int(input('Introduceti varsta: '))
# if varsta >= 18:
#     print('Esti major!')
# else:
#     print('Esti minor!')

#-Validator parola 2
# parola = input('Introduceti o parola de minim 8 caractere: ')
# if len(parola) > 7:
#     print('Parola setata cu succes!')
# else:
#     print('Parola are mai putin de 8 caractere!')

#-Cel mai mare numar
# n1 = int(input('Introduceti un prim numar: '))
# n2 = int(input('Introduceti un al doilea numar: '))
# if n1 > n2:
#     print("Numarul mai mare este", str(n1) + "!")
# elif n1 == n2:
#     print("Cele 2 numere sunt egale!")
# else:
#     print("Numarul mai mare este", str(n2) + "!")

#-Login simplificat
# username = 'admin'
# password = '1234'
# username_input = input('Introduceti numele utilizatorului: ')
# password_input = input('Introduceti parola: ')
# if username_input == username and password_input == password:
#     print('Login reusit!')
# else:
#     print('Credentiale invalide!')

#-Mini sistem de validare utilizator
# username = 'admin'
# password = '1234'
# age = 18
# username_input = input('Introduceti numele utilizatorului: ')
# password_input = input('Introduceti parola: ')
# age_input = int(input('Introduceti varsta dumneavoastra: '))
# if age_input >= age:
#     if username_input != username:
#         print('Username invalid!')
#     elif password_input != password:
#         print('Parola invalida!')
#     else:
#         print('Acces permis!')
# else:
#     print('Acces interzis - minori!')

def validate_user(username_input, password_input, age_input):
    username = 'admin'
    password = '1234'
    min_age = 18

    if age_input >= min_age:
        if username_input != username:
            return 'Username invalid!'
        elif password_input != password:
            return 'Parola invalida!'
        else:
            return 'Acces permis!'
    else:
        return 'Acces interzis - minori!'