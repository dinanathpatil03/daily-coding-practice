import matplotlib.pyplot as plt

# customized line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Basic line plot")
plt.plot(x, y, color="r", linestyle="-.", marker="o", linewidth=4, markersize=9)
plt.grid(True)
print(plt.show())

# Multiple plots
# sample data
x = [1 ,2 ,3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.subplot(2, 2, 1)
plt.plot(x, y1, color = "green")
plt.title("PLot1")

plt.subplot(2, 2, 2)
plt.plot(y1, x, color = "red")
plt.title("PLot2")

plt.subplot(2, 2, 3)
plt.plot(x, y2, color = "blue")
plt.title("PLot3")

plt.subplot(2, 2, 4)
plt.plot(y2, x, color = "yellow")
plt.title("PLot4")

print(plt.show())

# BAR PLOT

catagory = ["A", "B", "C", "D", "E"]
value = [5, 6, 8, 4, 2]

plt.bar(catagory, value, color = "purple")
plt.xlabel("catagories")
plt.ylabel("values")
plt.title("Bar Plot")
print(plt.show())

# Histogram

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, color="orange", edgecolor = "black")
print(plt.show())

# Create a scatter plot

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.scatter(x, y, color="blue", marker="x")
print(plt.show())


# create an pipe charts
labels = ["A", "B", "C", "D"]
sizes = [30, 20, 40, 10]
colors = ["yellow", "green", "orange", "blue"]
explode = (0.2, 0, 0 ,0)


plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True)
print(plt.show())






