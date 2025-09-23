import csv

mileages = []
prices = []

with open("data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)  # lee cada fila como un diccionario
    for row in reader:
        mileages.append(float(row["km"]))
        prices.append(float(row["price"]))

if not mileages:
    raise ValueError("CSV empty.")
scale = max(mileages)
if scale == 0:
    raise ValueError("All km are zero")
xs = [x / scale for x in mileages]

learning_rate = 0.1
iterations = 5000
m = len(xs)
theta0 = 0.0
theta1 = 0.0

for _ in range(iterations):
    predictions = [theta0 + theta1 * x for x in xs]
    errors = [predictions[i] - prices[i] for i in range(m)]

    d_theta0 = (1/m) * sum(errors)
    d_theta1 = (1/m) * sum(errors[i] * xs[i] for i in range(m))

    theta0 -= learning_rate * d_theta0
    theta1 -= learning_rate * d_theta1

theta1 = theta1 / scale
with open("thetas.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["theta0", "theta1"])
    writer.writerow([theta0, theta1])


print(f"theta0: {theta0:.3f}, theta1: {theta1:.3f}")
print("Parámetros guardados en thetas.csv")

