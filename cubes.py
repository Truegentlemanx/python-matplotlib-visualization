import matplotlib.pyplot as plt

input_values = range(1, 5001)
cubes = [i**3 for i in input_values]

plt.style.use('grayscale')
fig, ax = plt.subplots()

ax.plot(input_values, cubes, linewidth=3)

# Set chart titles and label axes
ax.set_title('Cubes all around', fontsize=24)
ax.set_xlabel('Values', fontsize=20)
ax.set_ylabel('Cubes of values', fontsize=20)

# Set size of tick labels. 
ax.tick_params(labelsize=24)

plt.show()