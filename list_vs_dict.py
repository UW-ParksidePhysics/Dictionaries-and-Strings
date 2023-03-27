# exercise 6.2

#t1 = {}
#t1[0] = -5
#t1[1] = 10.5

"""The code above works while the code below does not work because of the use of {} vs [] in
the initial definition of t1 and t2 respectively. The line t1 = {} sets up t1 as a dictionary
for which the values of t1[0] and t1[1] are then assigned. The line t2 = [] sets up t2 as an
empty list. Values of empty lists can only be assigned using the append function."""

#t2 = []
#t2[0] = -5
#t2[1] = 10.5

"""The following code will fill the empty list t3"""

t3 = []
t3.append(-5)
t3.append(10.5)
print(t3)
