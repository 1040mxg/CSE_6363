import pandas as pd
import math

def sortDist(n):
    return n[0]

def kNN(data):
    vals = data.iloc[:, :].values
    menu = input("Use default datasets? [y/n] ")
    if menu.lower() == "n":
        h2, w2, a2 = [ int(x) for x in input("Input data in format [height,weight,age]: ").split(",")]
    else:
        test_data = [[162, 53, 28],
                 [168, 75, 32],
                 [175, 70, 30],
                 [180, 85, 29]]
        print(" [1]: ", test_data[0], "\n",
               "[2]: ", test_data[1], "\n",
               "[3]: ", test_data[2], "\n",
               "[4]: ", test_data[3], "\n",)
        dataSet = int(input("Select dataset: "))-1
        print("Using dataset: ", test_data[dataSet])
        h2 = test_data[dataSet][0]
        w2 = test_data[dataSet][1]
        a2 = test_data[dataSet][2]
    i = 0
    comp = []
    while i < len(vals):
        temp_list = []
        gender = vals[i][3]
        diffVal = 0
        h1 = vals[i][0]
        w1 = vals[i][1]
        a1 = vals[i][2]
        diffVal = (h1 - h2) ** 2 + (w1 - w2) ** 2 + (a1 - a2) ** 2
        diffVal = math.sqrt(diffVal)
        temp_list.append(diffVal)
        temp_list.append(gender)
        comp.append(temp_list)
        # print("%.2f" %diffVal)
        i += 1

    k = int(input("Enter K value: "))
    comp.sort(key=sortDist)
    print("Cartesian Distances: ", ([x for x in comp[:k]]))
    mCount = ([x[1] for x in comp[:k]]).count("M")
    wCount = ([x[1] for x in comp[:k]]).count("W")
    if mCount > wCount:
        print("Prediction: M")
    else:
        print("Prediction: W")

def main():
    menu = input("Use default training data? [y/n] ")
    if menu.lower() == "y":
        data = pd.read_csv('hw1_data.csv', header=None)
    else:
        customFile = input("Enter data file name with extension: ")
        data = pd.read_csv(customFile, header=None)
    kNN(data)

if __name__ == "__main__":
    main()

# h2, w2, a2 = [ int(x) for x in input("Input data in format [height,weight,age]: ").split(",")]
# i=0
# while i < len(vals):
#     diffVal = 0
#     h1 = vals[i][0]
#     w1 = vals[i][1]
#     a1 = vals[i][2]
#     # print(h1, h2)
#     # print(w1, w2)
#     # print(a1, a2)
#     # print(vals[i][0])
#     diffVal = (h1-h2)**2+(w1-w2)**2+(a1-a2)**2
#     diffVal = math.sqrt(diffVal)
#     print("%.2f" %diffVal)
#     i+=1


# i = 0
# while i < len(distance_columns):
#     j=0
#     while j < len(test_data):
#         print(test_data[j][0] - distance_columns[i][0])
#             # w = test_data[num][1]
#             # a = test_data[num][2]
#         j+=1
#     i+=1

# print(test_data[0][0])
# print(distance_columns[0][0])
# distVal = (test_data[0][0]-distance_columns[0][0])**2
# print(distVal)

# num = 0
# while num < len(test_data):
#     distVal = 0
#     # print("[   ", num+1, "   ]")
#     # print("Height: ", test_data[num][0])
#     # print("Weight: ", test_data[num][1])
#     # print("Age: ", test_data[num][2], "\n")
#     for i in distance_columns:
#         distVal += (distance_columns[i] - test_data[num][i])**2
#     print(distVal)
#     num += 1

# def distance(row):
#     distVal = 0
#     num = 0
#     while num < len(test_data):
#         for i in distance_columns:
#             distVal += (row[i] - test_data[num][i])**2)
#             num+=1
#
# print(test1)
