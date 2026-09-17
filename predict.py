import csv, os, sys

def obtener_numero():
    while True:
        try:
            mileage = float(input("Introduce car mileage: "))
            return mileage
        except KeyboardInterrupt:
            sys.exit(130)
        except EOFError:
            sys.exit(0)
        except ValueError:
            print("Error: Numbers only.")

mileage = obtener_numero()

theta0, theta1 = 0.0, 0.0

if os.path.exists("thetas.csv"):
    with open("thetas.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            theta0 = float(row["theta0"])
            theta1 = float(row["theta1"])
            break
else:
    print("Warning: thetas.csv not found; using theta0=0, theta1=0")

price = theta0 + theta1 * mileage
if price < 0:
    price = 0
    max_km = -theta0 / theta1
    print(f"Max mileage to price 0 is {max_km}")

print(f"Estimated price is {price:.3f}")