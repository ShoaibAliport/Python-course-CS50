def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_wihtout_dollar_sign = d.replace('$','')
    return float(d_wihtout_dollar_sign)


def percent_to_float(p):
    percent_without_percent_sign = p.replace('%','')
    return float(percent_without_percent_sign) / 100


main()
