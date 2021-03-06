from random import randint, random, shuffle, sample, choice
from itertools import permutations, combinations, combinations_with_replacement
from pprint import pprint
from copy import copy, deepcopy
#Classes
class Individual:
    def __init__(self, machines):
        self._machines = machines
        self._fit = 0
    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self._machines, memo))
            memo[id_self] = _copy 
        return _copy

class Machine:
  def __init__(self, name, tasks):
    self._name = name
    self._tasks = tasks

  
  def get_tasks(self):
    return self._tasks

  def set_tasks(self,tasks):
      self._tasks = tasks

  def add_task(self, task):
      self._tasks.append(task)

class Task:
    def __init__(self, name, time, order, forcedorder, nexttask):
        self._name = name
        self._time = time
        self._order = order
        self._forcedorder = forcedorder
        self._nexttask = nexttask
    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self._name, self._time, self._order, self._forcedorder, self._nexttask)
    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self._name, memo), 
                deepcopy(self._time, memo),
                deepcopy(self._order, memo),
                deepcopy(self._forcedorder, memo),
                deepcopy(self._nexttask, memo))
            memo[id_self] = _copy 
        return _copy

#Métodos

#Método de criação de indivíduo
def population():
    task1 = Task('T1', 40, 0, 0, 0)
    task2 = Task('T2', 18, 0, 0, 0)
    task3 = Task('T3', 31, 0, 0, 0)
    task4 = Task('T4', 7, 0, 0, 0)
    task5 = Task('T5', 22, 0, 0, 0)

    # task6 = Task('T6', 3, 6, 0, 0)
    # task7 = Task('T7', 17, 0, 0, 0)
    # task8 = Task('T8', 32, 0, 0, 0)
    # task9 = Task('T9', 40, 0, 0, 0)
    # task10 = Task('T10', 6, 0, 0, 0)

    tasks1 = [task1, task2, task3, task4, task5]
    tasks2 = [task1, task2, task3, task4, task5]
    tasks3 = [task1, task2, task3, task4, task5]
    tasks4 = [task1, task2, task3, task4, task5]
    tasks5 = [task1, task2, task3, task4, task5]
    shuffle(tasks1)
    machine1 = Machine('Caldeira', tasks1)
    shuffle(tasks2)
    machine2 = Machine('Empacotadora', tasks2)
    shuffle(tasks3)
    machine3 = Machine('Prensa', tasks3)
    shuffle(tasks4)
    machine4 = Machine('Etiquetadora', tasks4)
    shuffle(tasks5)
    machine5 = Machine('Esteira', tasks5)
    machines = [machine1, machine2, machine3, machine4, machine5]
    individual = Individual(machines)

    return individual



def calcula(individual):
    tasks = []
    new_individual = deepcopy(individual)
    testind = deepcopy(individual)
    menor_maq = []
    machine = []
    for subset in permutations(individual._machines[0]._tasks, 5):
        tasks.append(subset)
    total = 0
    total2 = 0
    fit = 0
    menor = 1000000
    testind._fit = 0
    controle = deepcopy(individual)
    controle._fit = 0
    # for i in range (len(testind._machines)):
    #     for j in range(len(testind._machines[i]._tasks)):
    #         testind._fit += testind._machines[i]._tasks[j]._time

    for i in range(len(individual._machines)):
        for j in range(len(tasks)):
            if j == 0:
                menor = 1000000
            testind._machines[i]._tasks = tasks[j]
            testind._fit = controle._fit
            for k in range(len(testind._machines[i]._tasks)):
                total += testind._machines[i]._tasks[k]._time
                if i != 0:
                    for l in range(len(testind._machines)):
                        for m in range(len(testind._machines[l]._tasks)):
                            total2 += testind._machines[l]._tasks[m]._time
                            if testind._machines[l]._tasks[m] == testind._machines[i]._tasks[k]:
                                if total2 > total and l < i:
                                    testind._fit += total2 - total
                                elif (total + testind._machines[i]._tasks[k]._time) > total2 and l < i:
                                    testind._fit += (total + testind._machines[i]._tasks[k]._time) - total2
                                if m == k and l < i:
                                    testind._fit += testind._machines[i]._tasks[k]._time
                        total2 = 0
                else:
                    testind._fit = total

            if testind._fit < menor:
                menor = testind._fit
                new_individual._machines[i]._tasks = deepcopy(testind._machines[i]._tasks)
                new_individual._fit = testind._fit
                ite = j
                if i != 0 and k == 4:
                    new_individual._fit += total
            total = 0
            testind._fit = controle._fit
        if i == 0:
            controle._fit = new_individual._fit
        else:
            controle._fit += new_individual._fit
        controle._machines[i]._tasks = new_individual._machines[i]._tasks

    return controle








    # for m in range(len(tasks)):
    #     for i in range (len(individual._machines)):
    #         machine = individual._machines[i]
    #         for j in range (len(individual._machines[i]._tasks)):
    #             total += individual._machines[i]._tasks[j]._time
    #             fit += individual._machines[i]._tasks[j]
    #             for l in range (len(individual._machines)):
    #                 if l < i:
    #                     for k in range (len(individual._machines[l]._tasks)):
    #                         total2 += individual._machines[l]._tasks[k]._time
    #                         if individual._machines[i]._tasks[j] == individual._machines[l].tasks[k]:
    #                             if total2 > total:
    #                                 fit += total2-total
    #                             if j == k:
    #                                 fit += individual._machines[l].tasks[k]
    #         if fit < menor:
    #             menor_maq = individual._machines[i]
    #             fit = menor
        
        
        





individual = population()
new_ind = calcula (individual)
print(new_ind._fit)
print ('\n')
for i in range (len(new_ind._machines)):
    for j in range(len(new_ind._machines[i]._tasks)):
        print(new_ind._machines[i]._tasks[j])