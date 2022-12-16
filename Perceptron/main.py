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



# Input and labels Feature1;Feature2;Label
x = [
    [0.72, 0.82, -1],
    [0.91, -0.69, -1],
    [0.03, 0.93, -1],
    [0.12, 0.25, -1],
    [0.96, 0.47, -1],
    [0.8, -0.75, -1],
    [0.46, 0.98, -1],
    [0.66, 0.24, -1],
    [0.72, -0.15, -1],
    [0.35, 0.01, -1],
    [-0.11, 0.01, -1],  #test
    [0.31, -0.96, 1],
    [0.0, -0.26, 1],
    [-0.43, -0.65, 1],
    [0.57, -0.97, 1],
    [-0.72, -0.64, 1],
    [-0.25, -0.43, 1],
    [-0.12, -0.9, 1],
    [-0.50, 0.62, 1],
    [-0.77, -0.76, 1],
]

# Output
y = 0

# Best Fit Line for the given problem. This is used for plotting
BEST_X = 0.77
BEST_Y = -0.55

# Color - Red or Blue, 1 and -1, respectively
color = ""
# Answer = Correct or Error
answer = ""

# --- Parameters ---;

## Step 1

# Weights
w1 = 0
w2 = 0
w0 = 1

# Best Weights
bw1 = 0
bw2 = 0
bw0 = 1
minError = 999999;

# Maximum number allowed of epochs // Số vòng lặp
n = 100

# Best Learn Point
blxA = 0
blxB = 0
blyA = 0
blyB = 0

# -----------------------------------

# Turn on the interactive graphics mode
plt.ion()

# Step 2: Loop
for k in range(1, n):
    hits = 0
    print("\n------------------- Loop number: " + str(k) + "------------------");

    # Send all data points into the learning algorithm
    for i in range(0, len(x)):

        output = x[i][0] * w1 + x[i][1] *w2 + w0

        if abs(output) < minError:
            minError = output
            bw1 = w1
            bw2 = w2
            bw0 = w0

        if output > 0:
            y = 1
        else:
            y = -1

        # if the output does not match with the Desired output, then update.
        if y == x[i][2]:
            hits += 1
            answer = "No Weight Change."
        else:
            w1 += x[i][2] * x[i][0]
            w2 += x[i][2] * x[i][1]
            w0 += x[i][2]

        print("\n" + answer)


        # ----------------  Plotting the Graph below -----------
        plt.clf()
        if (testBefore == False):
            plt.title('Loop number %s\n' % (str(k)) + 'W1: %s  ' % (str(w1)) + 'W2: %s   ' % (w2) + 'W0: %s' % (str(w0)))
        else:
            plt.title('Best Answer Before W1: %s  ' % (str(w1)) + 'W2: %s   ' % (w2) + 'W0: %s' % (str(w0)))
        plt.grid(False)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        xA = 1
        xB = -1

        if w2 != 0:
            yA = (-w1 * xA - w0) / w2
            yB = (-w1 * xB - w0) / w2
            ByA = (-bestw1 * xA - bestw0) / bestw2
            ByB = (-bestw1 * xB - bestw0) / bestw2
        else:
            xA = -w0 / w1
            xB = -w0 / w2

            yA = 1
            yB = -1

        if (testBefore == False):
            # Draw Best Line Before
            plt.plot([xA, xB], [yA, yB], color='g', linestyle='-', linewidth=2)
        else:
            # Draw BestLine Caculated
            plt.plot([xA, xB], [ByA, ByB], color='r', linestyle='-', linewidth=1)

        if showBestAnswerDefault:
            # Draw best line (black)
            plt.plot([BEST_X, BEST_Y], [-1, 1], color='k', linestyle='-', linewidth=1)

        # Draw blue points
        # x_coords, y_coords = get_points(data_dictionary, '-1')
        for p in range(0, len(x)):
            x_coords = x[p][0]
            y_coords = x[p][1]
            if x[p][2] == -1:
                plt.plot(x_coords, y_coords, 'bo')
            else:
                plt.plot(x_coords, y_coords, 'ro')
            ...

        # Highlights the current point
        if answer == 'Correct!':
            plt.plot(x[i][0], x[i][1], 'go', markersize=15, alpha=0.5)
        else:
            plt.plot(x[i][0], x[i][1], 'mo', markersize=30, alpha=0.5)

        plt.show()

        plt.pause(0.05)

        if (testBefore == True):
            while True:
                a=0

    if hits == len(x):
        print("\n------------------------------------------")
        print("\nAlgorithm has learn with" + str(k) + " iterations!")
        minError = 0
        bw1 += w1
        bw2 += w2
        bw0 += w0
        break
    else:
        print("\n------------------------------------------")
        print("\nAlgorithm has learn with" + str(k) + " iterations!")
    ...
...

print("\nDone!\n")
print("Best W: w1"+str(w1)+" ,w2"+str(w2)+" ,w0"+str(w0)+" ,\n Output: "+str(minError))
