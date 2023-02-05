# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:06:55 2023

@author: Daniel Hulse
"""
from prog_models.models import Powertrain, ESC, DCMotor

esc = ESC()
motor = DCMotor()
powertrain = Powertrain(esc, motor)

# Define future loading function - 100% duty all the time
def future_loading(t, x=None):
    return powertrain.InputContainer({
        'duty': 1,
        'v': 23
    })

# Simulate to threshold
print('\n\n------------------------------------------------')
print('Simulating to threshold\n\n')
simulated_results = powertrain.simulate_to(2, future_loading, dt=2e-5, save_freq=0.1, print=True)


# time
time = simulated_results[0]
# input
ins = simulated_results[1]
# states
states = simulated_results[2]
#outs
outs = simulated_results[3]
# ???
# simulated_results[4]

#if __name__ == '__main__':
    