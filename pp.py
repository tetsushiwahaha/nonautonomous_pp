import sys, json
import numpy as np
from numpy import cos
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

import pptools

def func(t, x, data):
	v =  []
	n = len(data.dict['func'])
	for i in np.arange(n):
		v.append(eval(data.dict['func'][i]))
	return v

def main():
	data = pptools.init()

	state0 = data.dict['x0']
	tick = data.dict['tick']

	fperiod = 2.0 * np.pi
	duration = fperiod * data.dict['period']
	tspan = np.arange(0, duration, tick)
	running = True
	
	while running:
		if pptools.window_closed(data.ax) == True:
			sys.exit()
		state = solve_ivp(func, (0, duration), state0, 
			t_eval=tspan, 
			rtol = 1e-6,
			#method = 'DOP853', 
			method = 'RK45', args=(data, ))
		if data.visual_orbit == 1:
			lines, = plt.plot(state.y[0, :], state.y[1, :], 
				linewidth = 1, color = (0, 0, 0), 
				ls = "-", alpha = data.dict['alpha'])
		plt.plot(state.y[0, -1], state.y[1, -1], 'o', 
			markersize = 2, color="red", alpha = data.dict['alpha'])
		state0 = data.dict['x0'] = state.y[:, -1] 
		plt.pause(0.001) #REQIRED

if __name__ == '__main__':
	main()