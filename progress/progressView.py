import matplotlib.pyplot as plt
import json

with open('progress.json', 'r') as f:
    progressData = json.loads(f.read())

xValues = []
minValues = []
lowerPercentile = []
meanValues = []
upperPercentile = []
maxValues = []
for n, generation in enumerate(progressData):
    xValues.append(n+1)
    minValues.append(generation['min'])
    lowerPercentile.append(generation['25percentile'])
    meanValues.append(generation['mean'])
    upperPercentile.append(generation['75percentile'])
    maxValues.append(generation['max'])

plt.plot(xValues, minValues, label = "Minimum")
plt.plot(xValues, lowerPercentile, label = "25th Percentile")
plt.plot(xValues, meanValues, label = "Mean")
plt.plot(xValues, upperPercentile, label = "75th Percentile")
plt.plot(xValues, maxValues, label = "Max")

plt.xlabel('Generation')
# Set the y axis label of the current axis.
plt.ylabel('Fitness')
# Set a title of the current axes.
plt.title('Progress of NEAT')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
