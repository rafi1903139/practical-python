# bounce.py
#
# Exercise 1.5
'''
Problem statement:
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.
'''

ball_current_height = 100
n_bounce = 10
for i in range(n_bounce):
    ball_current_height *= 3 / 5 
    #print(i+1, ball_current_height) # without rounding value
    print(i + 1, round(ball_current_height, ndigits=4))

