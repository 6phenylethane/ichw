#!/usr/bin/env python3  
  
"""tile.py: put bricks in the whole wall, and draw them by turtle  
  
__author__ = "Shen Chenxi"  
__pkuid__  = "1800011777"  
__email__  = "zzscx@pku.edu.cn"  
"""  
import turtle  
m = int(input('The length of the wall:'))  
n = int(input('The height of the wall:'))  
a = int(input('The length of the brick:'))  
b = int(input('The width of the brick:'))  
'''输入墙和瓷砖的两边长  
'''  
   
def brick(e, m, n, a, b):  
    '''由瓷砖的左下角一维坐标，给出整个瓷砖铺满的所有一维坐标元组  
    '''  
    if e % m + a <= m and e // m + b <= n:  
        b_rick = []  
        for i in range(a):  
            for j in range(b):  
                b_rick.append(e + i + m * j)  
        return tuple(b_rick)  
    else:  
        return False  
  
def set_in(start, tu_ple, total, results):  
    '''开始铺瓷砖，每铺一块瓷砖记录一次，并从墙中删掉瓷砖的所有覆盖坐标，然后进行递归  
    '''  
    a, b, m, n, i = tu_ple  
    t = brick(i, m, n, a, b)  
    if t:  
        now0 = start+[t]  
        walllst = []  
        for k in now0:  
            walllst.extend(k)  
        walldict = set(walllst)  
        s = len(walldict)  
        if s == total:  
            results.append(now0)  
        elif len(walllst) == s:  
            wallleft = set(range(total))-walldict  
            i = min(wallleft)  
            set_in(now0, (a, b, m, n, i), total, results)  
            set_in(now0, (b, a, m, n, i), total, results)  
    return results  
  
def draw(lst, m):  
    '''用turtle画出来  
    '''  
    para = 200/m  
    bob = turtle.Turtle()  
    bob.speed(0)  
    bob.penup()  
    bob.goto(-200, 100)  
    for i in lst:  
        lu, rd = i[0], i[-1]  
        y, x = divmod(lu, m)  
        bob.goto(para*x-200, 100-para*y)  
        dy, dx = divmod(rd-lu, m)  
        dy += 1  
        dx += 1  
        bob.pendown()  
        for k in range(2):  
            bob.fd(para*dx)  
            bob.rt(90)  
            bob.fd(para*dy)  
            bob.rt(90)  
        bob.penup()  
  
def main():  
    total = n * m  
    if a != b:  
        if m * n % (a * b) == 0:  
            results = (  
            set_in([], (a, b, m, n, 0), total, []) +   
            set_in([], (b, a, m, n, 0), total, [])  
            )  
            for i in range(len(results)):  
                print(i + 1, results[i])  
            need = int(input('Which one do you want to draw?'))-1  
            draw(results[need], m)  
        else:  
            print(None)  
    if a == b:  
        if m % a == 0 and n % a == 0:  
            wallput = []  
            for i in range(n // a):  
                for j in range(m // a):  
                    wallput.append(brick(j * a + i * a * m, m, n, a, a))  
                    results = [wallput]  
            print(results[0])  
            print(input('Do you wan to draw it?'))  
            draw(results[0], m)  
        else:  
            print(None)  
  
if __name__ == '__main__':  
    main()  
