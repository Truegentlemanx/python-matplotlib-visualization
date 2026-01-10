import matplotlib.pyplot as plt

input_values = range(1, 5001)
cubes = [i**3 for i in input_values]

fig, ax = plt.subplots()

ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=20)

# Set chart titles and label axes
ax.set_title('Cubes all around', fontsize=24)
ax.set_xlabel('Values', fontsize=20)
ax.set_ylabel('Cubes of values', fontsize=20)

# Set size of tick labels. 
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 5500, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()