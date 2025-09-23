# plot.py
import csv, os
import matplotlib.pyplot as plt

xs, ys = [], []
if os.path.exists("data.csv"):
    with open("data.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            xs.append(float(row["km"]))
            ys.append(float(row["price"]))

if not xs:
    print("data.csv está vacío.")
    raise SystemExit(1)

theta0, theta1 = None, None
if os.path.exists("thetas.csv"):
    with open("thetas.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            theta0 = float(row["theta0"])
            theta1 = float(row["theta1"])
            break
else:
    print("No se encontró thetas.csv. Ejecuta primero train.py.")
    raise SystemExit(1)

xmin, xmax = min(xs), max(xs)
x_line = [xmin, xmax]
y_line = [theta0 + theta1 * xmin, theta0 + theta1 * xmax]

plt.figure()
plt.scatter(xs, ys)
plt.plot(x_line, y_line,  color="tab:red")
plt.xlabel("Mileage (km)")
plt.ylabel("Price (€)")
plt.title("Price vs Mileage")
plt.grid(True)

plt.savefig("fit.png", dpi=120)
print("Gráfica guardada en fit.png")

value = 0.0
m = len(xs)
for i in range(m):
    pred = theta0 + theta1 * xs[i]
    err = abs(pred - ys[i])
    value += err

mae = value / m
print(f"MAE = {mae:.3f}")