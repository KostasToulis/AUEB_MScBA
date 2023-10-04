import numpy as np
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

class Person:
    def __init__(self, ht, wt, gender):
        self.height = ht
        self.weight = wt
        self.gender = gender

def calculate_distance(p1, p2):
    return math.sqrt((p1.weight-p2.weight)**2 + (p1.height-p2.height)**2)

if __name__ == '__main__':
    random.seed(1)

    people = []

    for i in range(100):
        # generate women
        wt = random.gauss(65,12)
        ht = random.gauss(168,8)
        people.append(Person(ht,wt,'woman'))

        #generate men
        wt = random.gauss(75,12)
        ht = random.gauss(176,10)
        people.append(Person(ht,wt,'man'))

    # for i in people:
    #     print(i.height, i.weight, i.gender)

    # temp_people = people
    men = []
    women = []

    for person in people:
        # tempPeople = people
        # del tempPeople[k]
        sortedPeople = []
        for targetPerson in people:
            sortedPeople.append((targetPerson,calculate_distance(person,targetPerson)))
        sortedPeople.sort(key = lambda x: x[1])
        countWomen = 0
        countMen = 0
        for i in range(1,6):
            if sortedPeople[i][0].gender == 'woman': countWomen += 1
            else: countMen += 1
        if countWomen > countMen: women.append(person)
        else: men.append(person)

    print('Men ',len(men),':\n')
    womenInMen = 0
    for i in men:
        if (i.gender == 'woman'): womenInMen += 1
        # print(i.gender,i.height,i.weight,'\n')

    print('Women', len(women), ':\n')
    menInWomen =0
    for i in women:
        if (i.gender == 'man'): menInWomen += 1
        # print(i.gender,i.height,i.weight, '\n')

    print('Percent of wrong men classifications: ', womenInMen/len(men)*100)
    print('Percent of wrong women classifications: ', menInWomen / len(women) * 100)

    menHeightWeight = np.array([[i.height, i.weight] for i in people if i.gender == 'man'])
    womenHeightWeight = np.array([[i.height, i.weight] for i in people if i.gender == 'woman'])

    # print(menHeightWeight[:, 0], menHeightWeight[:, 1])

    plt.subplot(1)
    plt.plot(menHeightWeight[:, 0], menHeightWeight[:, 1], label='Men', marker='*', color='blue', linewidth=0)
    plt.plot(womenHeightWeight[:, 0], womenHeightWeight[:, 1], label='Women', marker='+', color='red', linewidth=0)
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.show()
