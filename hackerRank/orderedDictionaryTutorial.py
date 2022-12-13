from collections import Counter
if __name__=="__main__":
    print("enter number of items?")
    no_of_items=int(input())
    item_detail_counter=Counter([])
    print("Enter item name and price, separated by a comma")
    for i in range(no_of_items):
        item_details = {}
        *items,item_price=input().split(" ")
        item=' '.join(items)
        item_details[item]=int(item_price)
        item_detail_counter.update(item_details)
    for counter_item,counter_item_price in item_detail_counter.items():
        print(counter_item,counter_item_price)
