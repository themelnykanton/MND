import numpy as np
import random


def fill_random(x1, x2):
    tmp_mass = []
    for i in range(4):
        tmp_mass.append(random.randint(x1, x2 + 1))
    return tmp_mass


def sum_riv(x1, x2, x3, b0, b1, b2, b3):
    y = b0 + b1 * x1 + b2 * x2 + b3 * x3
    return y


class Lab3:
    def __init__(self, m, x1_min, x1_max, x2_min, x2_max, x3_min, x3_max, y_min, y_max):
        self.m = m

        self.x1_min, self.x1_max = x1_min, x1_max,
        self.x2_min, self.x2_max = x2_min, x2_max
        self.x3_min, self.x3_max = x3_min, x3_max
        self.y_min, self.y_max = y_min, y_max

        self.x1_plan = fill_random(self.x1_min, self.x1_max)
        self.x2_plan = fill_random(self.x2_min, self.x2_max)
        self.x3_plan = fill_random(self.x3_min, self.x3_max)
        self.y1_plan = fill_random(self.y_min, self.y_max)
        self.y2_plan = fill_random(self.y_min, self.y_max)
        self.y3_plan = fill_random(self.y_min, self.y_max)

        self.main_mass = []
        self.plan_matrix = [[1, -1, -1, -1],
                            [1, -1, 1, 1],
                            [1, 1, -1, 1],
                            [1, 1, 1, -1]]

        self.y_avg, self.mx, self.a, self.a_1 = [[] for i in range(4)]
        self.my = 0

        self.s_mass = []

        self.main()

    def main(self):
        self.main_mass.append(self.x1_plan)
        self.main_mass.append(self.x2_plan)
        self.main_mass.append(self.x3_plan)
        self.main_mass.append(self.y1_plan)
        self.main_mass.append(self.y2_plan)
        self.main_mass.append(self.y3_plan)

        self.first_step()
        self.second_step()
        self.prt()

    def first_step(self):
        for i in range(self.m):
            tmp = 0
            for j in range(3):
                tmp += self.main_mass[j + 3][i]
            self.y_avg.append(tmp / 3)

        for i in range(3):
            tmp = 0
            for j in range(self.m):
                tmp += self.main_mass[i][j]
            self.mx.append(tmp / self.m)

        for i in range(4):
            self.my += self.y_avg[i]
        self.my = self.my / 4

        for i in range(3):
            t = 0
            for j in range(4):
                t += self.main_mass[i][j] * self.y_avg[j]
            self.a.append(t / 4)

        for i in range(3):
            t = 0
            for j in range(4):
                t += self.main_mass[i][j] * self.main_mass[i][j]
            self.a_1.append(t / 4)

        a12  = (self.x1_plan[0] * self.x2_plan[0] + self.x1_plan[1] * self.x2_plan[1] + self.x1_plan[2] *
                     self.x2_plan[2] + self.x1_plan[3] * self.x2_plan[
                         3]) / 4
        a13  = (self.x1_plan[0] * self.x3_plan[0] + self.x1_plan[1] * self.x3_plan[1] + self.x1_plan[2] *
                     self.x3_plan[2] + self.x1_plan[3] * self.x3_plan[
                         3]) / 4
        a23 = a32 = (self.x2_plan[0] * self.x3_plan[0] + self.x2_plan[1] * self.x3_plan[1] + self.x2_plan[2] *
                     self.x3_plan[2] + self.x2_plan[3] * self.x3_plan[
                         3]) / 4

        self.ya1, self.ya2, self.ya3, self.ya4 = self.y_avg[0], self.y_avg[1], self.y_avg[2], self.y_avg[3]
        a1, a2, a3 = self.a[0], self.a[1], self.a[2]
        mx1, mx2, mx3 = self.mx[0], self.mx[1], self.mx[2]
        a11, a22, a33 = self.a_1[0], self.a_1[1], self.a_1[2]

        self.b0 = np.linalg.det([[self.my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a32],
                                 [a3, a13, a23, a33]]) / np.linalg.det(
            [[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])

        self.b1 = np.linalg.det([[1, self.my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a32],
                                 [mx3, a3, a23, a33]]) / np.linalg.det(
            [[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])

        self.b2 = np.linalg.det([[1, mx1, self.my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a32],
                                 [mx3, a13, a3, a33]]) / np.linalg.det(
            [[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])

        self.b3 = np.linalg.det([[1, mx1, mx2, self.my], [mx1, a11, a12, a1], [mx2, a12, a22, a2],
                                 [mx3, a13, a23, a3]]) / np.linalg.det(
            [[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])

        self.a12 = self.a21 = (self.x1_plan[0] * self.x2_plan[0] + self.x1_plan[1] * self.x2_plan[1] + self.x1_plan[2] *
                               self.x2_plan[2] + self.x1_plan[3] * self.x2_plan[
                                   3]) / 4
        self.a13 = self.a31 = (self.x1_plan[0] * self.x3_plan[0] + self.x1_plan[1] * self.x3_plan[1] + self.x1_plan[2] *
                               self.x3_plan[2] + self.x1_plan[3] * self.x3_plan[
                                   3]) / 4
        self.a23 = self.a32 = (self.x2_plan[0] * self.x3_plan[0] + self.x2_plan[1] * self.x3_plan[1] + self.x2_plan[2] *
                               self.x3_plan[2] + self.x2_plan[3] * self.x3_plan[
                                   3]) / 4

    def second_step(self):
        b = []
        b.append(self.b0)
        b.append(self.b1)
        b.append(self.b2)
        b.append(self.b3)

        self.Gt = 0.7679
        self.koef_T = []
        self.new_T = []
        self.Sad = 0

        for i in range(4):
            t = 0
            for j in range(3):
                t += (self.main_mass[j + 3][i] - self.y_avg[i]) ** 2
            self.s_mass.append(t / 3)

        self.Gp = max(self.s_mass) / sum(self.s_mass)
        self.S_B = sum(self.s_mass) / 4
        self.S_Bs = self.S_B / 12
        self.SBs = np.sqrt(self.S_Bs)
        self.B = []
        self.T = []

        for i in range(4):
            t = 0
            for j in range(4):
                t += self.y_avg[j] * self.plan_matrix[j][i]
            self.B.append(t / 4)

        for i in range(4):
            self.T.append(abs(self.B[i]) / self.SBs)

        for i in range(len(self.T)):
            if self.T[i] > 2.306:
                self.koef_T.append(i)

        for i in range(4):
            t = 0
            for j in self.koef_T:
                t += b[i] * self.main_mass[j][i]
            self.new_T.append(t)

        for i in range(4):
            self.Sad += (self.new_T[i] - self.y_avg[i]) ** 2

        self.S_ad = self.Sad * 1.5
        self.Fp = self.S_ad / self.S_Bs
        self.Ft = 4.5

    def prt(self):
        print("Матриця планування", "-", self.plan_matrix)
        for i in range(6):
            print(self.main_mass[i])
        print("Середні значення у - ", self.y_avg)
        print("mx1, mx2, mx3 - ", self.mx)
        print("my - ", self.my)
        print("a1, a2, a3 - ", self.a)
        print("a11, a22, a33 - ", self.a_1)
        print("a12, a13, a23, a21, a31, a32 - ", self.a12, self.a13, self.a23, self.a21, self.a31, self.a32)
        print("b0, b1, b2, b3 - ", self.b0, self.b1, self.b2, self.b3)
        print("Отримане рівняння регресії: ", self.b0, "+", self.b1, "*", "x1", "+", self.b2, "*", "x2", "+", self.b3,
              "*", "x3", )
        print(sum_riv(self.x1_plan[0], self.x2_plan[0], self.x3_plan[0], self.b0, self.b1, self.b2, self.b3), "=",
              self.ya1)
        print(sum_riv(self.x1_plan[1], self.x2_plan[1], self.x3_plan[1], self.b0, self.b1, self.b2, self.b3), "=",
              self.ya2)
        print(sum_riv(self.x1_plan[2], self.x2_plan[2], self.x3_plan[2], self.b0, self.b1, self.b2, self.b3), "=",
              self.ya3)
        print(sum_riv(self.x1_plan[3], self.x2_plan[3], self.x3_plan[3], self.b0, self.b1, self.b2, self.b3), "=",
              self.ya4)
        print("Дисперсія - ", self.s_mass)
        print("Gp - ", self.Gp)
        if self.Gp < 0.7679:
            print("Дисперсія однорідна")
        else:
            print("Дисперсія неоднорідна")
        print("S^2b - ", self.S_B)
        print("S^2bs - ", self.S_Bs)
        print("Sbs - ", self.SBs)
        print("B0, B1, B2, B3 - ", self.B)
        for i in range(len(self.T)):
            if self.T[i] > 2.306:
                print(self.T[i], "Входить в рівняння")
            else:
                print(self.T[i], "Виключається з рівнняня")
        print("Рівнняня")
        for i in self.koef_T:
            print("b" + str(i), "*", "x" + str(i), end=" ")
            print("+", end=" ")
        print(0)
        print("y1^, y2^, y3^, y4^ - ", self.new_T)
        print("Ft - ", self.Ft)
        print("Fp - ", self.Fp)
        print("Sad - ", self.Sad)
        if self.Fp > self.Ft:
            print("Fp>Fт.Отже, рівняння регресії неадекватно оригіналу при рівні значимості 0.05")


if __name__ == "__main__":
    c = Lab3(4, -10, 50, -20, 60, 50, 55, int(200 + (-20 + -10 + 50) / 3), int(200 + (55 + 50 + 66) / 3))
