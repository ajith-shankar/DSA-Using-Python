N, M, D = [int(x) for x in input("Enter Fuel capacity, Milage and Distance between each fuel stations \n").split(",")]

count = 1
temp = N * M

if temp < D:
    print("No")
else:
    while temp < 1000:
        count += 1
        temp = temp + N * M
    print("Yes", count)
