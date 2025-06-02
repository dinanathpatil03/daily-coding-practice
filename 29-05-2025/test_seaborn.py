import seaborn as sns

### Basic Plotting with seaborn

tips = sns.load_dataset("tips")
print(tips)

## create the scatter plot
import matplotlib.pyplot as plt

# sns.scatterplot(x="total_bill", y="tip", data=tips)
# plt.title("Scatter plot total bill vs tip")
# print(plt.show())

## Line Plot

# sns.lineplot(x="size", y="total_bill", data=tips)
# plt.title("Line plot of size and total bill")
# print(plt.show())

## catagorical bill
## bar plot

# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title("Bar plot for catagorical days")
# print(plt.show())


## Box plot

# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.title("Box plot")
# print(plt.show())

# Violin plot

sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin plot")
print(plt.show())