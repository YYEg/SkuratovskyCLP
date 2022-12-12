from pulp import LpMinimize, LpProblem, LpStatus, LpVariable


def Zero():
    model0 = LpProblem(name="LP0", sense=LpMinimize)

    x01 = LpVariable(name="x01", lowBound=0)
    x02 = LpVariable(name="x02", lowBound=0)
    x03 = LpVariable(name="x03", lowBound=0)
    x04 = LpVariable(name="x04", lowBound=0)
    x05 = LpVariable(name="x05", lowBound=0)

    model0 += 1 * x01 + 1 * x02 + 1 * x03 + 1 * x04 + 1 * x05  # Целевая функция ЛП0
    model0 += 1 * x01 + 3 * x02 + 5 * x03 + 7 * x04 + 9 * x05 >= 85  # Ограничение 1
    model0 += 4 * x01 + 3 * x02 + 2 * x03 + 1 * x04 + 0 * x05 >= 60  # Ограничение 2

    model0.solve()

    print(f"status: {model0.status}, {LpStatus[model0.status]}")
    print(f"objective: {model0.objective.value()}")

    for var in model0.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model0.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    #objective: 22.7777778
    #x01: 0.0
    #x02: 20.0
    #x03: 0.0
    #x04: 0.0
    #x05: 2.7777778


def First():
    model1 = LpProblem(name="LP1", sense=LpMinimize)

    x11 = LpVariable(name="x11", lowBound=0)
    x12 = LpVariable(name="x12", lowBound=0)
    x13 = LpVariable(name="x13", lowBound=0)
    x14 = LpVariable(name="x14", lowBound=0)
    x15 = LpVariable(name="x15", lowBound=0)

    model1 += 1 * x11 + 1 * x12 + 1 * x13 + 1 * x14 + 1 * x15  # Целевая функция ЛП0
    model1 += 1 * x11 + 3 * x12 + 5 * x13 + 7 * x14 + 9 * x15 >= 85  # Ограничение 1
    model1 += 4 * x11 + 3 * x12 + 2 * x13 + 1 * x14 + 0 * x15 >= 60  # Ограничение 2
    model1 += x12 <= 20 #ограничение для метода ветвей и границ
    model1 += x15 <= 2 #ограничение для метода ветвей и границ

    model1.solve()

    print(f"status: {model1.status}, {LpStatus[model1.status]}")
    print(f"objective: {model1.objective.value()}")

    for var in model1.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model1.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    #objective: 22.7777773
    #x11: 0.0
    #x12: 18.444444
    #x13: 2.3333333
    #x14: 0.0
    #x15: 2.0


def Second():
    model2 = LpProblem(name="LP2", sense=LpMinimize)

    x21 = LpVariable(name="x21", lowBound=0)
    x22 = LpVariable(name="x22", lowBound=0)
    x23 = LpVariable(name="x23", lowBound=0)
    x24 = LpVariable(name="x24", lowBound=0)
    x25 = LpVariable(name="x25", lowBound=0)

    model2 += 1 * x21 + 1 * x22 + 1 * x23 + 1 * x24 + 1 * x25  # Целевая функция ЛП2
    model2 += 1 * x21 + 3 * x22 + 5 * x23 + 7 * x24 + 9 * x25 >= 85  # Ограничение 1
    model2 += 4 * x21 + 3 * x22 + 2 * x23 + 1 * x24 + 0 * x25 >= 60  # Ограничение 2
    model2 += x22 >= 20 #ограничение для метода ветвей и границ
    model2 += x25 <= 2 #ограничение для метода ветвей и границ

    model2.solve()

    print(f"status: {model2.status}, {LpStatus[model2.status]}")
    print(f"objective: {model2.objective.value()}")

    for var in model2.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model2.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    #objective: 23.0
    #x21: 0.0
    #x22: 20.0
    #x23: 0.0
    #x24: 1.0
    #x25: 2.0

Zero()

First()
Second()