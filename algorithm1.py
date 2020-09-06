#!/usr/bin/env python3
import random

track_dur = []
sec_var = []
sec_rep = []
total_sec = []
form_unit = []
sec_ms = []

# generate list of 10 random numbers between 50 and 100 called 'track_dur'
for i in range(10):
    n = random.randint(50, 100)
    track_dur.append(n)
print("track_dur =", end=' ')
print(track_dur)

# for 1-10 generate random number between 3 and 7 called 'sec_var'
for i in range(10):
    n = random.randint(3, 7)
    sec_var.append(n)
print("sec_var = ", end=' ')
print(sec_var)

# for 1-10 generate random 1 and 5 for each sec_var called 'sec_rep'
for i in range(10):
    sec_list = []
    for j in range(0, sec_var[i]):
        n = random.randint(1, 5)
        sec_list.append(n)
# add up each set of sec_rep = 'total_sec'
    total_sec.append(sum(sec_list))
    sec_rep.append(sec_list)
print("sec_rep =")
for s in sec_rep:
    print(*s)
print("total_sec =", end=" ")
print(total_sec)

# track_dur * 1000 / total_sec = 'form_unit'
for i in range(10):
    form_unit.append(int(track_dur[i] * 1000 / total_sec[i]))
print("form_unit = ", end=' ')
print(form_unit)

# for 1-10 multiplay each sec_rep by form_unit (A_ms, B_ms, etc)
for i in range(len(sec_rep)):
    new_list = []
    for j in range(len(sec_rep[i])):
        new_list.append(sec_rep[i][j] * form_unit[i])
    sec_ms.append(new_list)
print("sec_ms =")
for s in sec_ms:
    print(*s)

# for each formal item A_ms attach a random number 'A_thresh' 100-200

# add to each pair in the list 'A_grid' = sum(A_ms / A_thresh)

# for each thresh_ms do 60000 / thresh_ms * 4 = 'tempo'

# for each grid item, generate random number 'riff_cyc' in sliding range
# of  integers < grid

# grid / riff_cyc = riff_rep (truncated)

# grid - riff_rep = tr_riff (each riff sequence is riff_cyc repeated)
