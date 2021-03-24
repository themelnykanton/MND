import random
import math as mt
import numpy as np


class Main:
    def __init__(self, count):
        self.n = count
        self.var = 316
        self.D = 0

        self.xn = [[-1, -1], [-1, 1], [1, -1]]

        self.y_mass, self.y_avg_mass, self.dis_mass, self.fuv_mass, self.quv_mass, self.ruv_mass, self.koef_mass = [], [], [], [], [], [], []

        self.x1_min, self.x1_max, self.x2_min, self.x2_max = -10, 50, -20, 60

        self.y_min, self.y_max = (20 - self.var) * 10, (30 - self.var) * 10

        self.mx1, self.mx2, self.my, self.a1, self.a2, self.a3, self.a11, self.a22 = 0, 0, 0, 0, 0, 0, 0, 0

        self.y_mass_func()
        self.y_avg_mass_func()
        self.dis_mass_func()
        self.fuv_quv_ruv_lists_func()
        self.koef()
        self.other()

    def y_mass_func(self):
        print("Матриця планування для n єкспериментів")

        for i in range(3):
            self.y_mass.append([])
            for j in range(self.n):
                self.y_mass[i].append(random.randint(self.y_min, self.y_max))
            print(self.y_mass[i])

    def y_avg_mass_func(self):
        print("Середні значення матриці планування")

        for i in range(3):
            self.y_avg_mass.append(sum(self.y_mass[i]) / self.n)
            print(self.y_avg_mass[i])

    def dis_mass_func(self):
        print("Дисперсія")

        for i in range(3):
            d = 0
            for j in range(self.n):
                d += (self.y_mass[i][j] - self.y_avg_mass[i]) ** 2
            self.dis_mass.append(d / self.n)
            print(d / self.n)
        self.D = mt.sqrt((2 * (2 * self.n - 2) / (self.n * (self.n - 4))))
        print("Основне відхилення - ", self.D)

    def fuv_quv_ruv_lists_func(self):
        fuv1, fuv2, fuv3 = self.dis_mass[0] / self.dis_mass[1], self.dis_mass[2] / self.dis_mass[0], self.dis_mass[2] / \
                           self.dis_mass[1]

        quv1, quv2, quv3 = ((self.n - 2) / self.n), ((self.n - 2) / self.n) * fuv2, ((self.n - 2) / self.n) * fuv3

        ruv1, ruv2, ruv3 = (quv1 - 1) / self.D, (quv2 - 1) / self.D, (quv3 - 1) / self.D

        self.fuv_mass.append(fuv1)
        self.fuv_mass.append(fuv2)
        self.fuv_mass.append(fuv3)

        self.quv_mass.append(quv1)
        self.quv_mass.append(quv2)
        self.quv_mass.append(quv3)

        self.ruv_mass.append(ruv1)
        self.ruv_mass.append(ruv2)
        self.ruv_mass.append(ruv3)
        for i in range(3):
            print("Fuv - ", self.fuv_mass[i])
        for i in range(3):
            print("Quv - ", self.quv_mass[i])
        for i in range(3):
            print("Ruv - ", self.ruv_mass[i])
            
         #перевірка на однорідність
        for i in range(3):
            if self.ruv_mass[i]<2:
                self.ruv_mass[i]=2
        if sum(self.ruv_mass)==6:
            print("Диссперсія однорідна")
        else:
            print("Дисперссія неоднорідна")
        # -------------------------

    def koef(self):
        for i in range(3):
            self.mx1 += self.xn[i][0]
            self.mx2 += self.xn[i][1]
            self.my += self.y_avg_mass[i]
            self.a1 += self.xn[i][0] ** 2
            self.a2 = self.xn[i][0] * self.xn[i][1]
            self.a3 += self.xn[i][1] ** 2
            self.a11 += self.xn[i][0] * self.y_avg_mass[i]
            self.a22 += self.xn[i][1] * self.y_avg_mass[i]

        self.mx1, self.mx2, self.my, self.a1, self.a2, self.a3, self.a11, self.a22 = self.mx1 / 3, self.mx2 / 3, self.my / 3, self.a1 / 3, self.a2 / 3, self.a3 / 3, self.a11 / 3, self.a22 / 3

        self.b0 = np.linalg.det([[self.my, self.mx1, self.mx2], [self.a11, self.a1, self.a2],
                                 [self.a22, self.a2, self.a3]]) / np.linalg.det(
            [[1, self.mx1, self.mx2], [self.mx1, self.a1, self.a2], [self.mx2, self.a2, self.a3]])

        self.b1 = np.linalg.det(
            [[1, self.my, self.mx2], [self.mx1, self.a11, self.a2], [self.mx2, self.a22, self.a3]]) / np.linalg.det(
            [[1, self.mx1, self.mx2], [self.mx1, self.a1, self.a2], [self.mx2, self.a2, self.a3]])

        self.b2 = np.linalg.det(
            [[1, self.mx1, self.my], [self.mx1, self.a1, self.a11], [self.mx2, self.a2, self.a22]]) / np.linalg.det(
            [[1, self.mx1, self.mx2], [self.mx1, self.a1, self.a2], [self.mx2, self.a2, self.a3]])

        self.koef_mass.append(self.b0)
        self.koef_mass.append(self.b1)
        self.koef_mass.append(self.b2)

        for i in range(3):
            print("Нормований коефіцієнт - ", self.koef_mass[i])
        print("Нормоване рівняння регресії")
        print(str(self.b0) + " " + str(self.b1) + "*x1" + " " + str(self.b2) + "*x2")
        print("Перевірка")
        print(self.b0 + self.b1 * (-1) + self.b2 * (-1), " = ", self.y_avg_mass[0])
        print(self.b0 + self.b1 * (-1) + self.b2 * (1), " = ", self.y_avg_mass[1])
        print(self.b0 + self.b1 * (1) + self.b2 * (-1), " = ", self.y_avg_mass[2])
       

    def other(self):
        delta_x1 = (self.x1_max - self.x1_min) / 2
        delta_x2 = (self.x2_max - self.x2_min) / 2
        x10 = (self.x1_min + self.x1_max) / 2
        x20 = (self.x2_min + self.x2_max) / 2
        a_0 = self.b0 - self.b1 * (x10 / delta_x1) - self.b2 * (x20 / delta_x2)
        a_1 = self.b1 / delta_x1
        a_2 = self.b2 / delta_x2

        print("Натуралізовані коефіцієнти - ", a_0, a_1, a_2)
        print("Натуралізоване рівняння")
        print(str(a_0) + " " + str(a_1) + " * x1" + " " + str(a_2) + " * x2")
        print("Перевірка по рядках")
        print(a_0 + a_1 * (-10) + a_2 * (-20), "=", self.y_avg_mass[0])
        print(a_0 + a_1 * (-10) + a_2 * (60), "=", self.y_avg_mass[1])
        print(a_0 + a_1 * (50) + a_2 * (-20), "=", self.y_avg_mass[2])


if __name__ == "__main__":
    new_class = Main(6)
