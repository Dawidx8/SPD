from generatory import RandomNumberGenerator
import math
import operator
import copy

NUMBER = 10  # ilosc zadan do wykonania
SEED = 1
MAX = 29


class task:
    def __init__(self,i):
        self.id = i

    def add_r(self,r_time):
        self.r = r_time

    def add_p(self,p_time):
        self.p = p_time

    def add_q(self,q_time):
        self.q = q_time


def print_list(list):
    print("nr: ",end=" ")
    for i in list:
        print(i.id, end = " ")
    print()
    print("r: ",end=" ")
    for i in list:
        print(i.r, end = " ")
    print()
    print("p: ",end=" ")
    for i in list:
        print(i.p, end = " ")
    print()
    print("q: ",end=" ")
    for i in list:
        print(i.q, end = " ")
    print()


def sc(list):
    s.append(list[0].r)
    c.append(s[0]+list[0].p)
    Cmax = c[0] + list[0].q
    cq.append(c[0] + list[0].q)
    for i in range(1,len(list)):
        s.append(max(list[i].r,c[i-1]))
        c.append(s[i] + list[i].p)
        cq.append(c[i] + list[i].q)
        Cmax = max(Cmax,(c[i] + list[i].q))
    
    print("pi: ",end=" ")
    for i in list:
        print(i.id, end = " ")
    print()
    print("s: ",end=" ")
    print(s)
    print("c: ",end=" ")
    print(c)
    print("cq: ",end=" ")
    print(cq)
    print("Cmax: ",Cmax)



generator = RandomNumberGenerator.RandomNumberGenerator(SEED)
s = []  # moment rozpoczecia zadania
c = []  # moment zakonczenia zadania
cq = []
Cmax = 0

list = []
A = 0   # suma czasow r

for i in range(NUMBER):
    list.append(task(i+1))
    list[i].add_p(generator.nextInt(1,MAX))
    A += list[i].p

for i in range(NUMBER):
    list[i].add_r(generator.nextInt(1,A))

for i in range(NUMBER):
    list[i].add_q(generator.nextInt(1,A))

print_list(list)
print()
print("Permutacja naturalna:")
sc(list)
print()
print("Kolejnosc po algorytmie Schrage:")


# algorytm Schrage
k = 1
N = copy.copy(list)
G = []
pi = [] # prawidlowa kolejnosc
t = min(N,key=operator.attrgetter("r")).r

while G or N:
    while N and min(N,key=operator.attrgetter("r")).r <= t:
        ob = min(N,key=operator.attrgetter("r"))
        G.append(copy.copy(ob))
        N.remove(ob)
    if G:
        ob = max(G,key=operator.attrgetter("q"))
        G.remove(ob)
        pi.append(copy.copy(ob))
        t += ob.p
        k += 1
    else:
        t = min(N,key=operator.attrgetter("r")).r

s.clear()
c.clear()
cq.clear()
sc(pi)

