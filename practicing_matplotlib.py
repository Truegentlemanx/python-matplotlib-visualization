import matplotlib.pyplot as plt

from die import Die

# Create two D6 Dice.
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list using list comprehension.
results = [die_1.roll() + die_2.roll() for results in range(5000)]

# Analize the results.
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
# Using a list comprehension to create a list
freqeuncies = [results.count(value) for value in poss_results]

# Visualize the results using matplotlib.
plt.style.use("grayscale")
fig, ax = plt.subplots()

# Making it a bar chart.
ax.bar(poss_results, freqeuncies)

# Set chart title and label axes.
ax.set_title("Frequencies of numbers when rollin a two D6 Dice", fontsize=24)
ax.set_xlabel("Rolls", fontsize=20)
ax.set_ylabel("Frequencies of a thrown number", fontsize=20)

plt.show()