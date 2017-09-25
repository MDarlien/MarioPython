import gym
import numpy
import gym_pull
import random
from random import randint
def move(x):
	r = random.randrange(2)
	if r == 0:
                return  [0, 0, 0, 1, 0, 1]  # Right + B
	
	if r == 1:
                return  [0, 0, 0, 0, 1, 0]  # Up
	if r == 2:
		return  [0,0,0,1,1,0]
	if r == 3:
		return  [0,0,0,1,0,0]
	if r == 4:
		return  [0,0,0,1,0,0]
a = numpy.append([[0,0,0,0,1,0],[0,0,0,1,0,1]],[[0,0,0,0,1,0]], axis = 0 )
intera = 0
for i_episode in range(1000):
	env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
	observation = env.reset()
	distance=0
	i = 0
	contador = 0
	while True:
            env.render()
	    contador = contador + 1

	    if contador >= intera:
		action = move(random.randint(0, 3))
	    	#action = numpy.random.randint(2, size=6)
		a = numpy.insert(a,contador,action,axis = 0)
	    else:
		action = a[contador]
               
            print action
	    print i
            old_observation = observation
            observation, reward, done, info = env.step(action)
	    if info['distance'] <= distance:
	    	i = i + 1
	    else:
		i = 0
            if info['distance'] > distance:
		#print old_observation
                print '---------------------------------------------------------'
		print contador
		print intera
		print info['distance']
		print i
		#spamwriter.writerow(action)
		#aqui tiene que  llnar la variable 
                distance = info['distance']
	    if i >= 100:
		intera = contador
		intera = intera - 150 
		break
            if done:
                break
