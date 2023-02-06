def calculate_pay(hours, wage):
    if hours > 40:
        product = wage * 40
        product += 2 * (wage * (hours - 40))
    else:
        product = hours * wage
    return max(product, 0)


def main():
    result = calculate_pay(50, 20)
    print(result)


if __name__ == "__main__":
    main()