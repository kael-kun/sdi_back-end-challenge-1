def calculate_optimized_cost(seats, seat_options):
    sorted_options = sorted(seat_options.items(), key=lambda x: x[1][1] / x[1][0])
    min_cost = float('inf')
    best_distribution = None
    def find_best_distribution(remaining_seats, current_cost, current_distribution):
        nonlocal min_cost, best_distribution
        if remaining_seats <= 0:
            if current_cost < min_cost:
                min_cost = current_cost
                best_distribution = current_distribution.copy()
            return

        for option, (capacity, cost) in sorted_options:
            current_distribution[option] += 1
            find_best_distribution(remaining_seats - capacity, current_cost + cost, current_distribution)
            current_distribution[option] -= 1
    initial_distribution = {option: 0 for option in seat_options}
    find_best_distribution(seats, 0, initial_distribution)
    if best_distribution:
        for option, count in best_distribution.items():
            if count > 0:
                print(f"{option} x {count}")
        print(f"Total = PHP {min_cost}")

seat_options = {
    'S': (5, 5000),
    'M': (9, 8000),  
    'L': (15, 11000)  
}
seats = int(input("Please input number (seat): "))
calculate_optimized_cost(seats, seat_options)
