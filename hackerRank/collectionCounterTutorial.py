from collections import Counter

if __name__ == "__main__":
    print("how many sizes are available?")
    no_of_shoes = int(input())
    print("Mention the available sizes")
    available_shoe_sizes = map(int, input().split(" "))
    available_shoe_sizes_dict = Counter(available_shoe_sizes)
    print("How many customers are interested to buy the shoes?")
    number_of_customers = int(input())
    print("Mention the size and offered price")
    total_income = 0
    for i in range(number_of_customers):
        shoe_size, offered_price = map(int, input().split(" "))
        is_size_available = available_shoe_sizes_dict.get(shoe_size, 0)
        if (is_size_available > 0):
            total_income += offered_price
            available_shoe_sizes_dict[shoe_size] = is_size_available - 1
    print("total income is->", total_income)
