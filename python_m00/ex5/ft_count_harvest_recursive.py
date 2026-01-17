
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def loop(current_day, days):
        print(f"Day {current_day}")
        if current_day == days:
            return
        loop(current_day + 1, days)
    loop(1, days)
    print("Harvest time!")
