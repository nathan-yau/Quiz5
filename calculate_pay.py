def calculate_pay(hours, wage):
    """
    Calculate the employee's weekly salary

    :param hours: floating point number or an integer
    :param wage: floating point number or an integer
    :precondition: hours must be a float point number or an integer
    :precondition: wage must be a float point number or an integer
    :postcondition: calculate the weekly pay
    :return: employee's weekly salary as a floating point number

    >>> calculate_pay(10.5, 20.0)
    210.0
    >>> calculate_pay(13.5, 20.3)
    274.05
    >>> calculate_pay(58, 30)
    2280.0
    """
    if hours > 40:
        weekly_pay = wage * 40
        weekly_pay += 2 * (wage * (hours - 40))
    else:
        weekly_pay = hours * wage
    if hours < 0 or wage < 0:
        weekly_pay = 0
    return float(weekly_pay)


def main():
    result = calculate_pay(40, 20)
    print(result)


if __name__ == "__main__":
    main()
