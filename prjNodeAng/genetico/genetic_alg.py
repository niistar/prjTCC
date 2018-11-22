from random import randint, random, shuffle, sample, choice
from itertools import permutations
from pprint import pprint
from statistics import mean
import collections
from copy import copy, deepcopy
from flask import Flask, request
from flask_cors import CORS
import sys

app = Flask (__name__)
CORS(app)
machines_global = []
tasks_global = []

@app.route('/', methods=['POST'])
def funcao():
  s=0
  if request.method == 'POST':
    json = request.get_json()
    for i in range(len(json)):
      if s == 0 and json[i] != '//':
        machines_global.append(json[i])
      if s == 0 and json[i] == '//':
        s = 1
      if s == 1 and json[i] != '//':
        tasks_global.append(json[i])


    print(machines_global)
    print('aa')
    print(tasks_global)

  
  #Classes
  class Individual:
    def __init__(self, machines):
      self._machines = machines
      self._fit = 0

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
    def __eq__(self, other):
      return self.__dict__ == other.__dict__
    def __hash__(self):
      return id(self)
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
    machines = []
    for i in range(len(machines_global)):
      task_nova = deepcopy(tasks_global)
      shuffle(task_nova)
      #print(machines_global[i].name)
      print('socorro')
      print(machines_global[i])
      print('nao aguento mais')
      #machine_nova = Machine(machines_global[i].name, task_nova)
      #machines.append(machine_nova)
    #individual = Individual(machines)



      # task1 = Task('T1', 40, 0, 0, 0)
      # task2 = Task('T2', 18, 0, 0, 0)
      # task3 = Task('T3', 31, 2, 1, 0)
      # task4 = Task('T4', 7, 0, 0, 0)
      # task5 = Task('T5', 22, 0, 0, 0)
      # task6 = Task('T6', 4, 0, 0, 0)
      # task7 = Task('T7', 11, 0, 0, 0)
      # task8 = Task('T8', 26, 5, 1, 0)
      # task9 = Task('T9', 50, 0, 0, 0)
      # task10 = Task('T10', 8, 0, 0, 0)


      # tasks1 = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
      # tasks2 = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
      # tasks3 = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
      # tasks4 = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
      # tasks5 = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

      # shuffle(tasks1)
      # machine1 = Machine('Caldeira', tasks1)
      # shuffle(tasks2)
      # machine2 = Machine('Empacotadora', tasks2)
      # shuffle(tasks3)
      # machine3 = Machine('Prensa', tasks3)
      # shuffle(tasks4)
      # machine4 = Machine('Etiquetadora', tasks4)
      # shuffle(tasks5)
      # machine5 = Machine('Esteira', tasks5)
      # machines = [machine1, machine2, machine3, machine4, machine5]
      # individual = Individual(machines)

    return individual

  #Método de cálculo da aptidão do indivíduo
  def fitness (individual):
    total = 0
    total2 = 0
    for i in range(len(individual._machines)):
      for j in range(len(individual._machines[i]._tasks)):
        total += individual._machines[i]._tasks[j]._time
        #print(individual._machines[i]._tasks[j]._time)
        if individual._machines[i]._tasks[j]._order != 0:
          if individual._machines[i]._tasks[j]._forcedorder == 0:
            if j < individual._machines[i]._tasks[j]._order:
              individual._fit += 10000
          else:
            if j != individual._machines[i]._tasks[j]._order:
              individual._fit += 10000
        
        if individual._machines[i]._tasks[j]._nexttask != 0:
          if j < len(individual._machines[i]._tasks)-1:
              if individual._machines[i]._tasks[j+1] != individual._machines[i]._tasks[j]._nexttask:
                  individual._fit += 10000

        for k in range(len(individual._machines)):
          for l in range(len(individual._machines[k]._tasks)):
            total2 += individual._machines[k]._tasks[l]._time
            if k != i:
              if l < j and individual._machines[k]._tasks[l]._time == individual._machines[i]._tasks[j]._time and total2 > total:
                individual._fit += total2 - total

              elif l == j and individual._machines[k]._tasks[l]._time == individual._machines[i]._tasks[j]._time and total2 > total:
                individual._fit += total2 - total

              elif l == j and individual._machines[k]._tasks[l]._time == individual._machines[i]._tasks[j]._time and total2 <= total:
                individual._fit += individual._machines[i]._tasks[j]._time  
              
              elif l > j and individual._machines[k]._tasks[l]._time == individual._machines[i]._tasks[j]._time and total + individual._machines[i]._tasks[j]._time > total2:
                individual._fit += (total + individual._machines[i]._tasks[j]._time) - total2
          total2 = 0
                
      individual._fit += total
      #print(individual._fit)
      total = 0

  #Método para o cruzamento entre indivíduos
  def permutation(individuals):
    new_individuals = []
    menor = 1000000000000
    new_list = []
    for j in range(1000):
      new_individual = []
      new_individuals = []
      menor = 1000000000000
      individuals_random = sample(individuals, 3)
      #minor_1 = [ l for l in individuals_random if l[-1] == min([ fit[-1] for fit in individuals_random._fit ]) ][0]
      for i in range(3):
          if(individuals_random[i]._fit < menor):
              minor_1a = individuals_random[i]
              menor = individuals_random[i]._fit
      individuals_random = sample(individuals, 3)
      menor = 1000000000000
      for i in range(3):
          if(individuals_random[i]._fit < menor):
              minor_2a = individuals_random[i]
              menor = individuals_random[i]._fit
      individuals_random = sample(individuals, 3)
      menor = 1000000000000
      for i in range(3):
          if(individuals_random[i]._fit < menor):
              minor_3a = individuals_random[i]
              menor = individuals_random[i]._fit

      lista = [minor_1a, minor_2a, minor_3a]
      menor = 1000000000000
      for i in range(3):
          if(lista[i]._fit < menor):
              minor_1 = lista[i]
              menor = lista[i]._fit

      #---------------------------------------------
      for i in range(3):
        if(individuals_random[i]._fit < menor):
            minor_1a = individuals_random[i]
            menor = individuals_random[i]._fit
      individuals_random = sample(individuals, 3)
      menor = 1000000000000
      for i in range(3):
        if(individuals_random[i]._fit < menor):
            minor_2a = individuals_random[i]
            menor = individuals_random[i]._fit
      individuals_random = sample(individuals, 3)
      menor = 1000000000000
      for i in range(3):
          if(individuals_random[i]._fit < menor):
              minor_3a = individuals_random[i]
              menor = individuals_random[i]._fit

      lista = [minor_1a, minor_2a, minor_3a]
      menor = 1000000000000
      for i in range(3):
          if(lista[i]._fit < menor):
              minor_2 = lista[i]
              menor = lista[i]._fit


      # for i in range(len(minor_1._machines)):
      #   if i == 0:
      #     quant = round((len(minor_1._machines))*0.6)
      #     ran = sample(range(1, len(minor_1._machines)-1), quant)
      #     new_individuals.append(minor_2._machines[i])
      #     for j in range(len(ran)):
      #       index = ran[j]
      #       new_individuals[i]._tasks[index] = deepcopy(minor_1._machines[i]._tasks[index])

      #     dif = []
      #     eq = []

      #     for j in range(len(new_individuals[i]._tasks)):
      #       for k in range(len(new_individuals[i]._tasks)):
      #         if minor_1._machines[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time:
      #           break
      #         elif k == len(new_individuals[i]._tasks)-1:
      #           dif.append(j)

      #     for j in range(len(new_individuals[i]._tasks)):
      #       for k in range(len(new_individuals[i]._tasks)):
      #         if new_individuals[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time and j != k and j < k and k not in eq:
      #           eq.append(k)
      #     for j in range(len(dif)):
      #       ind = eq[j]
      #       ind2 = dif[j]
      #       new_individuals[i]._tasks[ind] = minor_1._machines[i]._tasks[ind2]



      #   elif i % 2 == 1:
      #     if i == 0:
      #       quant = round((len(minor_1._machines))*0.6)
      #       ran = sample(range(len(minor_2._machines)-1), quant)
      #       new_individuals.append(minor_1._machines[i])
      #       for j in range(len(ran)):
      #         index = ran[j]
      #         new_individuals[i]._tasks[index] = deepcopy(minor_2._machines[i]._tasks[index])

      #       dif = []
      #       eq = []

      #       for j in range(len(new_individuals[i]._tasks)):
      #         for k in range(len(new_individuals[i]._tasks)):
      #           if minor_1._machines[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time:
      #             break
      #           elif k == len(new_individuals[i]._tasks)-1:
      #             dif.append(j)

      #       for j in range(len(new_individuals[i]._tasks)):
      #         for k in range(len(new_individuals[i]._tasks)):
      #           if new_individuals[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time and j != k and j < k and k not in eq:
      #             eq.append(k)
      #       for j in range(len(dif)):
      #         ind = eq[j]
      #         ind2 = dif[j]
      #         new_individuals[i]._tasks[ind] = minor_2._machines[i]._tasks[ind2]

      #   else:
      #     if i == 0:
      #       quant = round((len(minor_1._machines))*0.6)
      #       ran = sample(range(len(minor_1._machines)-1), quant)
      #       new_individuals.append(minor_2._machines[i])
      #       for j in range(len(ran)):
      #         index = ran[j]
      #         new_individuals[i]._tasks[index] = deepcopy(minor_1._machines[i]._tasks[index])

      #       dif = []
      #       eq = []

      #       for j in range(len(new_individuals[i]._tasks)):
      #         for k in range(len(new_individuals[i]._tasks)):
      #           if minor_1._machines[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time:
      #             break
      #           elif k == len(new_individuals[i]._tasks)-1:
      #             dif.append(j)

      #       for j in range(len(new_individuals[i]._tasks)):
      #         for k in range(len(new_individuals[i]._tasks)):
      #           if new_individuals[i]._tasks[j]._time == new_individuals[i]._tasks[k]._time and j != k and j < k and k not in eq:
      #             eq.append(k)
      #       for j in range(len(dif)):
      #         ind = eq[j]
      #         ind2 = dif[j]
      #         new_individuals[i]._tasks[ind] = minor_1._machines[i]._tasks[ind2]


      for i in range(len(minor_1._machines)):
        if i == 0:
          for j in range(len(minor_1._machines[i]._tasks)):
            if minor_1._machines[i]._tasks[j]._forcedorder == 1:
              if i != minor_1._machines[i]._tasks[j]._order:
                index = minor_1._machines[i]._tasks[j]._order
                taskAux = minor_1._machines[i]._tasks[j]
                minor_1._machines[i]._tasks[j] = minor_1._machines[i]._tasks[index]
                minor_1._machines[i]._tasks[index] = taskAux
          new_individuals.append(minor_1._machines[i])
        elif i % 2 == 1:
          for j in range(len(minor_2._machines[i]._tasks)):
            if minor_2._machines[i]._tasks[j]._forcedorder == 1:
              if i != minor_2._machines[i]._tasks[j]._order:
                index = minor_2._machines[i]._tasks[j]._order
                taskAux = minor_2._machines[i]._tasks[j]
                minor_2._machines[i]._tasks[j] = minor_2._machines[i]._tasks[index]
                minor_2._machines[i]._tasks[index] = taskAux
          new_individuals.append(minor_2._machines[i])
        else:
          for j in range(len(minor_1._machines[i]._tasks)):
            if minor_1._machines[i]._tasks[j]._forcedorder == 1:
              if i != minor_1._machines[i]._tasks[j]._order:
                index = minor_1._machines[i]._tasks[j]._order
                taskAux = minor_1._machines[i]._tasks[j]
                minor_1._machines[i]._tasks[j] = minor_1._machines[i]._tasks[index]
                minor_1._machines[i]._tasks[index] = taskAux
          new_individuals.append(minor_1._machines[i])

      new_individual = Individual(new_individuals)

      x = randint(0, 1000)
      if x < 10:
          while True:
              maq1 = randint(0, len(new_individual._machines)-1)
              maq2 = randint(0, len(new_individual._machines)-1)
              if(maq1 != maq2):
                  break

          aux = new_individual._machines[maq1]._tasks
          
          shuffle(aux)
          for i in range(len(aux)):
            if aux[i]._forcedorder == 1:
              if i != aux[i]._order:
                index = aux[i]._order
                taskAux = aux[i]
                aux[i] = aux[index]
                aux[index] = taskAux
          new_individual._machines[maq1]._tasks = new_individual._machines[maq2]._tasks
          new_individual._machines[maq2]._tasks = aux
      # for o in range(len(new_individual._machines)):
      #   for p in range(len(new_individual._machines[o]._tasks)):
      #     tasksss = new_individual._machines[o]._tasks[p]
      #     print(tasksss)
      new_list.append(new_individual)

    return new_list

  #Lista de indivíduos - População
  individuals = []
  controle = 10000000
  counter = 0
  menor = 0
  ciclos = 0
  resposta = []
  s = 0
  #print('chegou')
  for i in range (1000):
    x = population()
    individuals.append(x)

  while True:
    for i in range(1000):
        fitness(individuals[i])
    response = max(individuals, key = lambda x: x._fit)
    response2 = min(individuals, key = lambda x: x._fit)
    media = []

    for j in range(len(individuals)):
      media.append(individuals[j]._fit)


    menor = response._fit
    if(menor < controle):
      controle = menor
      counter += 1
      ciclos = 0
    ciclos += 1
    individuals = permutation(individuals)
    s = 1


    resposta = [mean(media), response._fit, response2._fit]
    pprint(resposta)

    if response._fit == response2._fit:
      for i in range(len(response._machines[0]._tasks)):
        print('Maquina 1: ')
        print(response2._machines[0]._tasks[i])
        print('\n')
      for i in range(len(response._machines[0]._tasks)):
        print('Maquina 2: ')
        print(response2._machines[1]._tasks[i])
        print('\n')
      for i in range(len(response._machines[0]._tasks)):
        print('Maquina 3: ')
        print(response2._machines[2]._tasks[i])
        print('\n')
      for i in range(len(response._machines[0]._tasks)):
        print('Maquina 4: ')
        print(response2._machines[3]._tasks[i])
        print('\n')
      for i in range(len(response._machines[0]._tasks)):
        print('Maquina 5: ')
        print(response2._machines[4]._tasks[i])
        print('\n')
      break

    # print('media: ' + str(mean(media)))
    # print('maior: ' + str(response._fit))
    # print('menor: ' + str(response2._fit))

  # for i in range(len(response._machines)):
  #     for j in range(len(response._machines[i]._tasks)):
  #             print('Maquina: ' + str(j))
              
  #             print(response._machines[i]._tasks[j])
  #             print('\n')

  for i in range(len(response._machines[0]._tasks)):
    print('Maquina 1: ')
    print(response._machines[0]._tasks[i])
    print('\n')
  for i in range(len(response._machines[0]._tasks)):
    print('Maquina 2: ')
    print(response._machines[1]._tasks[i])
    print('\n')
  for i in range(len(response._machines[0]._tasks)):
    print('Maquina 3: ')
    print(response._machines[2]._tasks[i])
    print('\n')
  for i in range(len(response._machines[0]._tasks)):
    print('Maquina 4: ')
    print(response._machines[3]._tasks[i])
    print('\n')
  for i in range(len(response._machines[0]._tasks)):
    print('Maquina 5: ')
    print(response._machines[4]._tasks[i])
    print('\n')

  return 'qqq'
  #voltar o código aqui