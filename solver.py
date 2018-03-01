import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

lines = [line.rstrip('\n') for line in open('a_example.in')]

data2 = lines[0].split(' ')

R = int(data2[0])
C = int(data2[1])
F = int(data2[2])
N = int(data2[3])
B = int(data2[4])
T = int(data2[5])

data3 = np.zeros([len(lines)-1,6], dtype=int)
for n in range(len(lines)-1):
    temp = lines[n+1].split(' ')
    for m in range(6):
        data3[n,m] = int(temp[m])

rides = data3[data3[:,4].argsort()]

car_rides = []
for n in range(F):
    car_rides.append([])

car_data = np.zeros([F,3],dtype=int)

#calculates the distance
def distance(ride_coord, car_coord):
    return abs(ride_coord[0]-car_coord[0])+abs(ride_coord[1]-car_coord[1])


points = 0
cost = np.zeros([N,F],dtype=int)
for n in range(N):
    for f in range(F):
        #Calculate cost function
        cost[n,f] = (distance(rides[n],car_data[f])
                    -(rides[n,4]-car_data[f,2]))
        
#find smallest elements of cost function
min_cost_entries = np.argwhere(cost==np.min(cost))
#pick random element of smallest cost function
[ride_pick, car_pick] = min_cost_entries[randint(0,len(min_cost_entries))]
#space distance from ride start to car position
dist_to_ride = distance(rides[ride_pick][0:2],car_data[car_pick][0:2])
#if car can make it to start point in time add bonus to points and update car time to ride start
if car_data[car_pick][2] + dist_to_ride <= rides[ride_pick][4]:
    points = points + B
    car_data[car_pick][2] = rides[ride_pick][4]
else:
    # or update car time to when the car will be at the ride start
    car_data[car_pick][2] = (car_data[car_pick][2]+
            dist_to_ride)
#update car position to ride start point
car_data[car_pick][0:2] = rides[ride_pick][0:2]


for n in range(N):
    for f in range(F):
        #Calculate cost function
        cost[n,f] = (distance(rides[n],car_data[f])
                    -(rides[n,4]-car_data[f,2]))

        
#        car_data[current_pick[1]][0:2] = rides[current_pick[0]][0:2]
        
#        car_data[current_pick][1] = rides[current_pick[0]][2,3]
        
#    available_cars = np.
#    for f in range(F):
#        if car_data

#print(data3)

#data = np.loadtxt("a_example.in")
#rows,columns,n_vehicles,n_rides,bonus,steps = data[0,:]
#actual_data = data[1:,:]
##row_start, column_start, row_end, column_end, earliest_start, latest finish
#print(actual_data)    