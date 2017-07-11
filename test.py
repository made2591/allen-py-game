#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Matteo'

import random
from model.model import Person, AllenAlgebra


NAME = ["Maryanne",
"Shemika",
"Deann",
"Myles",
"Avril",
"Twanda",
"Meaghan",
"Malinda",
"Courtney",
"Laine",
"Lucilla",
"Argentina",
"Georgene",
"Ellena",
"Bridgette",
"Arletta",
"Zofia",
"Wan",
"Wilbur",
"Romana",
"Tonita",
"Charlott",
"Mao",
"Takisha",
"Christen",
"Garfield",
"Flora",
"Mirella",
"Letty",
"Bunny",
"Jeniffer",
"Alice",
"Irving",
"Natalia",
"Joleen",
"Hortense",
"Florine",
"Salvador",
"Livia",
"Chantell",
"Errol",
"Toccara",
"Jutta",
"Vera",
"Dollie",
"Lucinda",
"Anna",
"Shon",
"Johana",
"Jacquelyn"]


ag = AllenAlgebra()

NUMBER_OF_PERSONS = 4

persons = []
index_of_name_choosen = []
for i in range(0, NUMBER_OF_PERSONS, 1):
    index = random.randrange(0, len(NAME))
    while index in index_of_name_choosen:
        index = random.randrange(0, len(NAME))
    index_of_name_choosen.append(index)
    p = Person(NAME[index], 1900, 2015)
    p.set_random(1900, 2015)
    persons.append(p)

for i in range(0, NUMBER_OF_PERSONS, 1):
    temp = persons[0:i-1]+persons[i+1:len(persons)]
    persons[i].toString(a = persons[i], level = random.randrange(1, 3), rnd = random.randrange(0, 3), persons = temp)

comparision = {}
for i in range(0, NUMBER_OF_PERSONS, 1):
    comparision[i] = []

for f, v in comparision.iteritems():
    for i, k in comparision.iteritems():
        comparision[f].append(ag.tests(persons[f], persons[i]))

first = 0
second = 0
for i, l in comparision.iteritems():
    for k in l:
        if first != second:
            if random.randrange(0, 10) > 6:
                ag.toString(persons[first], persons[second], k)
        second += 1
    first += 1
    second = 0

print "\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"

# print "\n%%%%%%%%%%%%%%%%%\n"
# for i in comparision:
#     print comparision[i]

# print "\n%%%%%%%%%%%%%%%%%\n"
# first = 0
# second = 0
# for i, l in comparision.iteritems():
#     for k in l:
#         if first != second:
#             ag.toString(persons[first], persons[second], k)
#         second += 1
#     first += 1
#     second = 0

q, a = ag.generateQuestion(0, persons)

print q, a

# persons = []
# a = Person("Person 1", 1900, 1910)
# b = Person("Person 2", 1908, 1920)
# c = Person("Person 3", 1915, 1923)
#
# persons.append(a)
# persons.append(b)
# persons.append(c)
#
# a.toString(1, 1)
# b.toString(1, 1)
# c.toString(1, 1)
#
# q, a = ag.generateQuestion(0, persons)
#
# print q, a

# a, b = b, a

# comp[0] = 1 or comp[0] = -1 ==> comp[6] = -1

# comp[1] = 1 or comp[1] = -1 ==> comp[0] = 0 and comp[6] = -1

# comp[2] = 1 or comp[2] = -1 ==> comp[0] = 0 and comp[1] = 0 and comp[6] = -1

# comp[3] = 1 or comp[3] = -1 ==> comp[0] = 0 and comp[1] = 0 and comp[2] = 0 and comp[6] = -1

# comp[4] = 1 or comp[4] = -1 ==> comp[0] = 0 and comp[1] = 0 and comp[2] = 0 and comp[3] = 0 and comp[6] = -1

# comp[5] = 1 or comp[5] = -1 ==>
#                comp[0] = 0 and comp[1] = 0 and comp[2] = 0 and comp[3] = 0 and comp[4] = 0 and comp[6] = -1

# comp[6] = 1 ==> comp[0] = 0 and comp[1] = 0 and comp[2] = 0 and comp[3] = 0 and comp[4] = 0 and comp[5] = 0

# ag.toString(a, b, ag.tests(a, b))



# persons = []
# comparision = {}
# for i in range(0, NUMBER_OF_PERSONS, 1):
# persons.append(Person("Persona "+str(i), 1900, 2000, 1))
#     print persons[-1].name, persons[-1].downlimit, persons[-1].uplimit
#     comparision[i] = []
#
# for f, v in comparision.iteritems():
#     for i, k in comparision.iteritems():
#         comparision[f].append(ag.tests(persons[f], persons[i]))
#
# print "\n%%%%%%%%%%%%%%%%%\n"
# for i in comparision:
#     print comparision[i]
#
# print "\n%%%%%%%%%%%%%%%%%\n"
# first = 0
# second = 0
# for i, l in comparision.iteritems():
#     for k in l:
#         if first != second:
#             ag.toString(persons[first], persons[second], k)
#         second += 1
#     first += 1
#     second = 0






# luca = Person("Luca", 1987, 2015)
#
# alice = Person("Alice", 1987, 2015)
#
# matteo = Person("Matteo", 1991, 2015)
#
# mamma = Person("Mamma", 1961, 2015)
#
# papa = Person("Papa", 1957, 2015)

# print ag.tests(alice, luca)
# ag.toString(alice, luca, ag.tests(alice, luca))

# print ag.tests(alice, matteo)
# ag.toString(alice, matteo, ag.tests(alice, matteo))
#
# print ag.tests(mamma, matteo)
# ag.toString(mamma, matteo, ag.tests(mamma, matteo))

# marco = Person("Marco", 1987, 2000)
# giovanni = Person("Giovanni", 2012, 2098)
# comp = ag.random_comparision(marco, giovanni)
# comp = ag.random_comparision()
# print comp
# print ag.toString(marco, giovanni, comp)