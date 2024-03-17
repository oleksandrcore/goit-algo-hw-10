import pulp

lemonade = pulp.LpVariable('A', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('B', lowBound=0, cat='Integer')

problem = pulp.LpProblem('Максимізація виробництва', pulp.LpMaximize)

problem += lemonade + fruit_juice
problem += 2 * lemonade + fruit_juice <= 100
problem += lemonade <= 50
problem += lemonade <= 30
problem += fruit_juice <= 30

problem.solve()

print('Лимонад:', pulp.value(lemonade))
print('Фруктовий сік:', pulp.value(fruit_juice))
