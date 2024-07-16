import random
import numpy as np

class Particle: # класс частицы
    def __init__(self, MIN_COORDINATE, MAX_COORDINATE, MAX_SPEED, INERTION, F_P, F_G, K, X) -> None:
        self.v = np.array([
            random.random() * MAX_SPEED, #вектор скорости
            random.random() * MAX_SPEED
        ])
        self.x = np.array([
            random.random() * (MAX_COORDINATE - MIN_COORDINATE) + MIN_COORDINATE,# координата точки частицы
            random.random() * (MAX_COORDINATE - MIN_COORDINATE) + MIN_COORDINATE
        ])
        self.local_solution = self.x
        
        self.MAX_SPEED = MAX_SPEED # константные параметры для расчетта вектора скорости
        self.INERTION = INERTION
        self.F_P = F_P
        self.F_G = F_G
        self.K = K
        self.X = X
        
        
    def update_v(self, global_solution): # функция расчета вектора скорости
        self.v = self.X * (self.INERTION * self.v + self.F_P * random.random() * (global_solution - self.x) + self.F_G * random.random() * (self.local_solution - self.x))
        
        if self.v[0] > self.MAX_SPEED:
            self.v[0] = self.MAX_SPEED
            
        if self.v[1] > self.MAX_SPEED:
            self.v[1] = self.MAX_SPEED

    def update_x(self): # функция расчета координат частицы.
        self.x = self.x + self.v

    def update_local_solution(self, func): # расчет наилучшего локального решения и сохранение координаты точки в которой решение достигается
        if func.value(self.local_solution) - func.value(self.x):
            self.local_solution = self.x
            
    def clone(self): # клонирование 
        clone = Particle(self.x[0], self.x[1], self.MAX_SPEED, self.INERTION, self.F_P, self.F_G, self.K, self.X)
        clone.x = self.x
        clone.v = self.v
        clone.local_solution = self.local_solution
        return clone