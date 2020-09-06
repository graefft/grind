#!/usr/bin/env python3
import random

track_dur = []
sec_var = []
sec_rep = []
total_sec = []
form_unit = []

for i in range(10):
    n = random.randint(50, 100)
    track_dur.append(n)
print("track_dur =", end=' ')
print(track_dur)

for i in range(10):
    n = random.randint(3, 7)
    sec_var.append(n)
print("sec_var = ", end=' ')
print(sec_var)

for i in range(10):
    sec_list = []
    for j in range(0, sec_var[i]):
        n = random.randint(1, 5)
    #    print(n, end = " ")
        sec_list.append(n)
    total_sec.append(sum(sec_list))
    sec_rep.append(sec_list)
    # print()
print("sec_rep =")
for s in sec_rep:
    print(*s)
print("total_sec =", end=" ")
print(total_sec)

form_unit = []
for i in range(10):
    form_unit.append(int(track_dur[i] * 1000 / total_sec[i]))
print("form_unit = ", end=' ')
print(form_unit)

sec_ms = []
for i in range(len(sec_rep)):
    new_list = []
    for j in range(len(sec_rep[i])):
        new_list.append(sec_rep[i][j] * form_unit[i])
    sec_ms.append(new_list)
print("sec_ms =")
for s in sec_ms:
    print(*s)
