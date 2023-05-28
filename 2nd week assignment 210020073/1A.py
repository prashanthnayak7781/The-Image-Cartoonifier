import matplotlib.pyplot as plt

years_experience = [1, 3, 5]
salary = [300, 480, 570]

plt.scatter(years_experience, salary)
plt.xlabel('No. of Years Experience')
plt.ylabel('Salary')
plt.title('Years of Experience vs. Salary')

plt.show()
