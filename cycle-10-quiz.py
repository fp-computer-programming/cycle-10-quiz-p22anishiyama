# Author: ATN 2/2/22

# values to start off with (note: im not sure if the values should carry over from problem to problem)
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# 1st

def price_avg(prices):
    # im going to be storing this information via in int
    average = 0
    
    # adding the current value to our average variable
    for x in prices:
        average += x

    # dividing this average value by the total number of entries to give our final result
    average /= len(prices)
    return average


print(price_avg(prices))

# 2nd

def discount(prices):
    # using enumerate because the question says "return the same list as prices..."
    for i, v in enumerate(prices):
        prices[i] -= 5
    return prices

print(discount(prices))

# 3rd

def revenue(prices, sales):
    # the total revenue is what i will be using for the output
    revenue = 0
    # i am setting quantity to be the total sales so i can delete from the original list later on
    quantity = len(sales)

    # for each entry in the prices, i am adding the price times the amount of that item sold to the total revenue
    for x in prices:
        revenue += (x * sales[0])
        del(sales[0])

    # i made two seperate outputs whether or not only one item is being sold
    if quantity != 1:
            return "{0} items were sold for ${1}".format(quantity, revenue)
    else:
            return "{0} item was sold for ${1}".format(quantity, revenue)


print(revenue(prices, sales))

# 4th

def bulk_discount(prices):
    # using enumerate since i am changing the list in place
    for i, v in enumerate(prices):
        # if the price meets the conditions, it is being lowered
        if prices[i] > 40:
            # i debated having three arguments for the function in order to determine the price threshold and the amount to lower/raise by
            prices[i] -= 10
    return prices

print(bulk_discount(prices))

# 5th

def item_format(prices, items):
    # i created a seperate list for these items so i am able to delete them when necessary
    mod_items = items
    mod_prices = prices
    # using a nested for loop
    for x in mod_items:
        for i, v in enumerate(x):
            # when printing each value, i titled the entry of the list to make it seem more appealing to the user
            print("{0} ${1}".format(x[i].title(), mod_prices[0]))
            # i am then able to delete this entry in the prices because of my initial cloning of the list
            del(mod_prices[0])


item_format(prices, items)

# 6th (will i get extra credit for completing this additionally?)

def counter(n, mult):
    # setting the counter variable because it is a while loop
    x = 0
    # setting the restrictions of this counter
    while x < n:
        # adding the counter variable by this multiple and printing this value
        x += mult
        print(x)


counter(100, 3)
