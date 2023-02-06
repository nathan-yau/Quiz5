def calculate_pay(hours, wage):
    if hours > 40:
        weekly_pay = wage * 40
        weekly_pay += 2 * (wage * (hours - 40))
    else:
        weekly_pay = hours * wage
    if hours < 0 or wage < 0:
        weekly_pay = 0

    return weekly_pay


def main():
    result = calculate_pay(40, 20)
    print(result)


if __name__ == "__main__":
    main()