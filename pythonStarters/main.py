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


def GeneratePopulation(womenWeightMean, womenWeightSigma, womenHeightMean, womenHeightSigma, menWeightMean, menWeightSigma, menHeightMean, menHeightSigma):
    # global i
    people = []
    for i in range(100):
        # generate women
        wt = random.gauss(womenWeightMean, womenWeightSigma)
        ht = random.gauss(womenHeightMean, womenHeightSigma)
        people.append(Person(ht, wt, 'woman'))

        # generate men
        wt = random.gauss(menWeightMean, menWeightSigma)
        ht = random.gauss(menHeightMean, menHeightSigma)
        people.append(Person(ht, wt, 'man'))
    return people


def GeneratePredictedPopulation(people):
    men = []
    women = []
    for targetPerson in people:
        sortedPeople = []
        for person in people:
            # for each targetPerson generate a list containing the population and each of their respective distance to targetPerson
            sortedPeople.append((person, calculate_distance(person, targetPerson)))
        # sort said list on the calculated distance
        sortedPeople.sort(key=lambda x: x[1])
        countWomen = 0
        countMen = 0
        # iterate over the first 5 people excluding the first because it is the targetPerson (its distance to itself is 0)
        for i in range(1, 6):
            if sortedPeople[i][0].gender == 'woman':
                countWomen += 1
            else:
                countMen += 1
        if countWomen > countMen:
            women.append(targetPerson)
        else:
            men.append(targetPerson)
    return men, women


def PlotFindings(people, men, women):
    menHeightWeight = np.array([[i.height, i.weight] for i in people if i.gender == 'man'])
    womenHeightWeight = np.array([[i.height, i.weight] for i in people if i.gender == 'woman'])
    predictedMenTrue = np.array([[i.height, i.weight] for i in men if i.gender == 'man'])
    predictedWomenTrue = np.array([[i.height, i.weight] for i in women if i.gender == 'woman'])
    predictedMenFalse = np.array([[i.height, i.weight] for i in men if i.gender == 'woman'])
    predictedWomenFalse = np.array([[i.height, i.weight] for i in women if i.gender == 'man'])
    # print(menHeightWeight[:, 0], menHeightWeight[:, 1])
    plt.subplot(121)
    plt.title('Men & Women Height/Weight')
    plt.plot(menHeightWeight[:, 0], menHeightWeight[:, 1], label='Men', marker='*', color='blue', linewidth=0)
    plt.plot(womenHeightWeight[:, 0], womenHeightWeight[:, 1], label='Women', marker='+', color='red', linewidth=0)
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.subplot(122)
    plt.title('Predicted Men & Women Height/Weight')
    plt.plot(predictedMenTrue[:, 0], predictedMenTrue[:, 1], label='Men', marker='*', color='blue', linewidth=0)
    plt.plot(predictedWomenTrue[:, 0], predictedWomenTrue[:, 1], label='Women', marker='+', color='red', linewidth=0)
    plt.plot(predictedMenFalse[:, 0], predictedMenFalse[:, 1], label='Men', marker='*', color='green', linewidth=0)
    plt.plot(predictedWomenFalse[:, 0], predictedWomenFalse[:, 1], label='Women', marker='+', color='green',
             linewidth=0)
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.show()


if __name__ == '__main__':
    random.seed(1)

    people = GeneratePopulation(65, 12, 168, 8, 75, 12, 176, 10)

    men, women = GeneratePredictedPopulation(people)

    #Print percent of wrong predictions
    womenInMen = 0
    for i in men:
        if (i.gender == 'woman'): womenInMen += 1

    menInWomen =0
    for i in women:
        if (i.gender == 'man'): menInWomen += 1

    print('Percent of wrong men classifications: ', womenInMen/len(men)*100)
    print('Percent of wrong women classifications: ', menInWomen / len(women) * 100)

    PlotFindings(people, men, women)
