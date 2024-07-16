import numpy as np
import random
from algorithm.Particle import Particle
from algorithm.Swarm import create_swarm, Swarm
import os
import matplotlib.pyplot as plt

class Func: # класс при помощи которого хранится и используется функция
    def __init__(self, func: str)->None:
        self.func = func
        
    def value(self, coordinate: np.ndarray)->float:
        x, y = coordinate[0], coordinate[1]
        return eval(self.func)

class Constants: # константные значения
    def __init__(self) -> None:
        self.FUNC = Func("4*(x - 2)**4 + (x - 2*y)**2")
        self.ROI_SIZE = 100 #величина РОЯ
        self.ITERATION = 100 #количество итераций
        self.MAX_SPEED = 10.0 # максимальная скорость частицы
        self.MAX_COORDINATE = 100.0 #максимальная координата для создания частицы
        self.MIN_COORDINATE = -100.0 #минимальная координата для создания частицы
        self.INERTION = 0.5 #коэффециент иннерции 
        self.F_P = 2.001 #коеффициент глобального ускорения
        self.F_G = 2.001 #коеффициент глобального ускорения
        self.FI = self.F_P + self.F_G
        self.K = 0.9 
        self.X = 2*self.K / abs(2 - self.FI - (self.FI**2 - 4*self.FI) ** 0.5)
        self.swarm = create_swarm(self.MIN_COORDINATE, self.MAX_COORDINATE, self.MAX_SPEED, self.INERTION, self.F_P, self.F_G, self.K, self.X, self.ROI_SIZE)
        self.moving = list()
        self.BEST_SOLUTION = 0
        self.BEST_COORDINATE = (0, 0)
    def add_in_moving(self):
        for i in range(len(self.swarm)):
            self.moving.append(self.swarm[i].clone())
            
    def __repr__(self) -> str:
        return f"best solution: {self.BEST_SOLUTION}, best coordinate: {self.BEST_COORDINATE}"
            

DIRECTORY = "images"
def add_image(N: int, particles: Swarm):
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    x = list()
    y = list()
    for particle in particles:
        x.append(particle.x[0])
        y.append(particle.x[1])
    plt.clf()   
    plt.plot(x, y, 'go')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.xlabel("x")
    plt.ylabel("Y")
    plt.savefig(f"{DIRECTORY}/location_{N}.png")