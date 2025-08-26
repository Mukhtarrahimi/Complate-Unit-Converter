import sys

#
LENGTH_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254,
}

WEIGHT_FACTORS = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,
    "oz": 0.028349523125,
    "ton": 1000.0,
}

VOLUME_FACTORS = {
    "l": 1.0,
    "ml": 0.001,
    "m3": 1000.0,
    "cm3": 0.001,
    "cup": 0.2365882365,
    "pt": 0.473176473,
    "qt": 0.946352946,
    "gal": 3.785411784,
}


SPEED_FACTORS = {
    "m/s": 1.0,
    "km/h": 1000.0 / 3600.0,
    "mph": 0.44704,
    "knot": 0.5144444444444445,
}


AREA_FACTORS = {
    "m2": 1.0,
    "km2": 1e6,
    "cm2": 0.0001,
    "mm2": 1e-6,
    "acre": 4046.8564224,
    "hectare": 10000.0,
}

CATEGORIES = {
    "Length": LENGTH_FACTORS,
    "Weight": WEIGHT_FACTORS,
    "Volume": VOLUME_FACTORS,
    "Speed": SPEED_FACTORS,
    "Area": AREA_FACTORS,
    "Temperature": None,
}


def convert_linear(value, from_unit, to_unit, factors):
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Invalid unit.")
    value_in_base = value * factors[from_unit]
    result = value_in_base / factors[to_unit]
    return result


def convert_temperature(value, from_unit, to_unit):
    f = from_unit.upper()
    t = to_unit.upper()
    if f == "C":
        c = value
    elif f == "F":
        c = (value - 32) * 5.0 / 9.0
    elif f == "K":
        c = value - 273.15
    if t == "C":
        return c
    elif t == "F":
        return c * 9.0 / 5.0 + 32
    elif t == "K":
        return c + 273.15


def list_units(factors):
    return ", ".join(sorted(factors.keys()))


def get_category_choice():
    print("\nCategories:")
    for i, name in enumerate(CATEGORIES.keys(), 1):
        print(f"{i}. {name}")
    choice = input("Choose category number: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(CATEGORIES):
            return list(CATEGORIES.keys())[idx]
    except ValueError:
        pass
    print("Invalid choice.")
    return None


def safe_float_input(prompt):
    s = input(prompt).strip()
    try:
        s = s.replace(",", ".")
        return float(s)
    except ValueError:
        raise ValueError("Invalid number.")


def main():
    print("Welcome to Unit Converter")
    while True:
        cat = None
        while cat is None:
            cat = get_category_choice()
        if cat not in CATEGORIES:
            print("Invalid category.")
            continue
         try:
            if cat == "Temperature":
                print("Units: C, F, K")
                value = safe_float_input("Enter value: ")
                from_u = input("From unit (C/F/K): ").strip().upper()
                to_u = input("To unit (C/F/K): ").strip().upper()
                result = convert_temperature(value, from_u, to_u)
                print(f"Result: {value} {from_u} = {round(result, 6)} {to_u}")
            else:
                factors = CATEGORIES[cat]
                value = safe_float_input("Enter value: ")
                print(f"Available units: {list_units(factors)}")
                from_u = input("From unit: ").strip()
                to_u = input("To unit: ").strip()
                if from_u not in factors or to_u not in factors:
                    print("Invalid unit.")
                    continue
                result = convert_linear(value, from_u, to_u, factors)
                print(f"Result: {value} {from_u} = {round(result, 6)} {to_u}")