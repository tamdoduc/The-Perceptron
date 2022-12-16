# Vẽ̃ đồ thị
import matplotlib.pyplot as plt

# SỐ học
import numpy as np
import random
import pyautogui as pya

testBefore = True
showBestAnswerDefault = False
bestw1 = -5.719999999999967
bestw2 = -4.499999999999962
bestw0 = 0
# bestw1 = -2.64
# bestw2 = -1.81
# bestw0 = 0

xA = 1
xB = -1

ByA = (-bestw1 * xA - bestw0) / bestw2
ByB = (-bestw1 * xB - bestw0) / bestw2

# Input and labels Feature1;Feature2;Label
x = [
    [0.7, 0.8, 0],
    [0.9, -0.6, 0],
    [0.0, 0.9, 0],
    [0.1, 0.2, 0],
    [0.9, 0.4, 0],
    [0., -0.7, 0],
    [0.4, 0.9, 0],
    [0.6, 0.2, 0],
    [0.7, -0.1, 0],
    [0.3, 0.01, 0],
    [-0.1, 0.01, 0],
    [0.3, -0.9, 0],
    [0.0, -0.2, 0],
    [-0.4, -0.6, 0],
    [0.5, -0.9, 0],
    [-0.7, -0.6, 0],
    [-0.2, -0.4, 0],
    [-0.1, -0.9, 0],
    [-0.5, 0.6, 0],
    [-0.7, -0.7, 0],
]

y = 0

# Maximum number allowed of epochs // Số vòng lặp
n = 100

# Turn on the interactive graphics mode
plt.ion()

for i in range(0, len(x)):

    output = x[i][0] * bestw1 + x[i][1] *bestw2 + bestw0

    if output > 0:
        y = 1
    else:
        y = -1

    x[i][2] = y

    # ----------------  Plotting the Graph below -----------
    plt.clf()
    plt.title('Output %s' % str(output))
    plt.grid(False)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    plt.plot([xA, xB], [ByA, ByB], color='r', linestyle='-', linewidth=1)

    for j in range(0, i+1):
        if x[j][2] == -1:
            plt.plot(x[j][0], x[j][1], 'bo')
        if x[j][2] == 1:
            plt.plot(x[j][0], x[j][1], 'ro')

    plt.plot(x[i][0], x[i][1], 'go', markersize=15, alpha=0.5)

    plt.show()

    plt.pause(0.5)

for j in range(0, len(x)):
    if x[j][2] == -1:
        plt.plot(x[j][0], x[j][1], 'bo')
    if x[j][2] == 1:
        plt.plot(x[j][0], x[j][1], 'ro')
    plt.title('Done')
    plt.show()
    plt.pause(0.5)
    while True:
        a = 0
