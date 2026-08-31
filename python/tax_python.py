def buy_item(cost_of_item):
    return cost_of_item + tax_included(cost_of_item)

def tax_included(cost_of_item):
    tax_rate=0.05
    return cost_of_item * tax_rate

final_cost= buy_item(50)
print(final_cost)