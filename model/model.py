#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Matteo'

import random

class Person(object):

    uplimit = 1900
    downlimit = 2015
    name = "Person"

    def __init__(self, n, d, u):
        self.name = n
        self.downlimit = d
        self.uplimit = u

    def set_random(self, start, end):
        self.downlimit = random.randrange(start, end-1)
        self.uplimit = random.randrange(self.downlimit+1, end)

    def toString(self, a, level = 0, rnd = 0, persons = []):

        if rnd == 0:
            if level == 0:
                print a.name+" was born in "+str(a.downlimit)+" and died in "+str(a.uplimit)
            elif level == 1:
                print a.name+" was born in "+str(a.downlimit)
            elif level == 2:
                print a.name+" died in "+str(a.uplimit)
        elif rnd == 1:
            if level == 0:
                hint_down = random.randrange(1, a.uplimit-a.downlimit+1)
                hint_up = random.randrange(1, a.uplimit-a.downlimit)
                print a.name+" was born before "+str(a.downlimit+hint_down)+ " and died after "+str(a.uplimit-hint_up)
            elif level == 1:
                hint_down = random.randrange(1, a.uplimit-a.downlimit+1)
                print a.name+" was born before "+str(a.downlimit+hint_down)
            elif level == 2:
                hint_up = random.randrange(1, a.uplimit-a.downlimit+1)
                print a.name+" died after "+str(a.uplimit-hint_up)
        elif rnd == 2:
            level = random.randrange(1, 3)
            b = random.randrange(0, len(persons))
            if level == 1:
                hint_down = random.randrange(1, a.uplimit-a.downlimit+1)
                hint_time = "before"
                if a.uplimit > persons[b].downlimit:
                    hint_time = "after"
                elif a.uplimit == persons[b].downlimit:
                    hint_time = "in the same year"
                print a.name+" was born before "+str(a.downlimit+hint_down)+" and died "+hint_time+" "+persons[b].name+" was born"
            elif level == 2:
                hint_up = random.randrange(1, a.uplimit-a.downlimit+1)
                hint_time = "before"
                if a.downlimit > persons[b].uplimit:
                    hint_time = "after"
                elif a.downlimit == persons[b].uplimit:
                    hint_time = "in the same year"
                print a.name+" died after "+str(a.uplimit-hint_up)
                print a.name+" was born "+hint_time+" "+persons[b].name+" was died"

class AllenAlgebra(object):

    NUMBER_OF_PROPERTIES = 7

    # def random_comparision(self, a, b):
    #     comparision = []
    #     for i in range(0, self.NUMBER_OF_PROPERTIES, 1):
    #         comparision.append(random.randrange(-1, 2))
    #     while self.valid(a, b, comparision) == True:
    #         return self.random_comparision
    #     return comparision
    #
    # def valid(self, a = Person, b = Person, comparision = []):
    #
    #     for i in range(0, self.NUMBER_OF_PROPERTIES, 1):
    #         test, actual, comparision = self.tests_exclude(a, b, comparision, i)
    #         print test
    #         print actual
    #         print comparision
    #         raw_input("Next compare...")
    #

    # def tests_exclude(self, a = Person, b = Person, actual = [], index = -1):
    #     comparision = []
    #     if index != 0: comparision.append(self.before(a, b))
    #     if index != 1: comparision.append(self.meets(a, b))
    #     if index != 2: comparision.append(self.overlaps(a, b))
    #     if index != 3: comparision.append(self.starts(a, b))
    #     if index != 4: comparision.append(self.during(a, b))
    #     if index != 5: comparision.append(self.finishes(a, b))
    #     if index != 6: comparision.append(self.equals(a, b))
    #     for i in range(0, self.NUMBER_OF_PROPERTIES, 1):
    #         if comparision[i] != actual[i]: return False, actual, comparision
    #     return True

    def generateQuestion(self, level, persons):
        a = random.randrange(0, len(persons))
        if a > len(persons) / 2:
            b = random.randrange(0, a)
        else:
            b = random.randrange(a+1, len(persons))
        if level == 0:
            return "Is that possible that "+persons[a].name+" was born after "+persons[b].name+"?", persons[a].downlimit > persons[b].downlimit
        elif level == 1:
            return "Is that possible that "+persons[a].name+" died before "+persons[b].name+" was born ?", persons[a].uplimit < persons[b].downlimit


    def tests(self, a = Person, b = Person):
        comparision = []
        comparision.append(self.before(a, b))
        comparision.append(self.meets(a, b))
        comparision.append(self.overlaps(a, b))
        comparision.append(self.starts(a, b))
        comparision.append(self.during(a, b))
        comparision.append(self.finishes(a, b))
        comparision.append(self.equals(a, b))
        return comparision

    def toString(self, a = Person, b = Person, comparision = []):
        if comparision[0] == 1: print a.name+" was born and died before "+b.name
        if comparision[0] == -1: print a.name+" was born and died after "+b.name
        if comparision[0] == 0: pass

        if comparision[1] == 1: print a.name+" died when "+b.name+" was born"
        if comparision[1] == -1: print b.name+" died when "+a.name+" was born"
        if comparision[1] == 0: pass

        if comparision[2] == 1: print a.name+" was born before "+b.name+" was born, died after "+b.name+" was born and "+b.name+" died after "+a.name+" was dead"
        if comparision[2] == -1: print b.name+" was born before "+a.name+" was born, died after "+a.name+" was born and "+a.name+" died after "+b.name+" was dead"
        if comparision[2] == 0: pass

        if comparision[3] == 1: print a.name+" was born in the same year and died before "+b.name
        if comparision[3] == -1: print b.name+" was born in the same year and died before "+a.name
        if comparision[3] == 0: pass

        if comparision[4] == 1: print a.name+" was born after and died before "+b.name
        if comparision[4] == -1: print b.name+" was born after and died before "+a.name
        if comparision[4] == 0: pass

        if comparision[5] == 1: print a.name+" died in the same year and born after "+b.name
        if comparision[5] == -1: print b.name+" died in the same year and born after "+a.name
        if comparision[5] == 0: pass

        if comparision[6] == 1: print a.name+" was born and died in the same year of "+b.name
        if comparision[6] == -1: print a.name+" was born, died, or both, in different year of "+b.name

    def before(self, a = Person, b = Person):
        if a.downlimit < b.downlimit and a.uplimit < b.uplimit and a.uplimit < b.downlimit: return 1
        if a.downlimit > b.downlimit and a.uplimit > b.uplimit and b.uplimit < a.downlimit: return -1
        return 0

    def meets(self, a = Person, b = Person):
        if a.uplimit == b.downlimit and a.downlimit < b.downlimit: return 1
        if b.uplimit == a.downlimit and b.downlimit < a.downlimit: return -1
        return 0

    def overlaps(self, a = Person, b = Person):
        if a.downlimit < b.downlimit and a.uplimit > b.downlimit and b.uplimit > a.uplimit: return 1
        if b.downlimit < a.downlimit and b.uplimit > a.downlimit and a.uplimit > b.uplimit: return -1
        return 0

    def starts(self, a = Person, b = Person):
        if a.downlimit == b.downlimit and a.uplimit < b.uplimit: return 1
        if b.downlimit == a.downlimit and b.uplimit < a.uplimit: return -1
        return 0

    def during(self, a = Person, b = Person):
        if a.downlimit > b.downlimit and a.uplimit < b.uplimit: return 1
        if b.downlimit > a.downlimit and b.uplimit < a.uplimit: return -1
        return 0

    def finishes(self, a = Person, b = Person):
        if a.uplimit == b.uplimit and a.downlimit > b.downlimit: return 1
        if b.uplimit == a.uplimit and b.downlimit > a.downlimit: return -1
        return 0

    def equals(self, a = Person, b = Person):
        if a.uplimit == b.uplimit and a.downlimit == b.downlimit: return 1
        return -1