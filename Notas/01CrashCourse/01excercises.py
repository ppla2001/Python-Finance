#Task 1
price = 300
square_root = price ** 0.5
square_root

#Task 2
stock_index = "SP500"
stock_index[2:]

#Task 3 
stock_index = "SP500"
price = 300
'The {} is at {} today.'.format(stock_index,price)

#Task 4
stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
'''Yesterdays 250'''
stock_info['sp500']['yesterday']
''' number 365 '''
stock_info['info'][1][2]

#Task 5
def source_finder(s):
    return s.split('--')[-1]

source_finder('PRICE:345.324:SOURCE--QUANDL')

#Task 6
def price_finder(s):
    if 'price' in s.lower():
        return True

price_finder("What is the price?")
price_finder("DUDE, WHAT IS PRICE!!!")

#Task 7
s = 'Wow that is a nice price, very nice Price! I said price 3 times.'
def count_price(s):
    price_counter = 0
    for word in s.lower().split():
        if 'price' in word:
            price_counter += 1
    return price_counter

count_price(s)

#Task 8
def avg_price(n):
    for num in n:
        return sum(n)/len(n)

avg_price([3,4,5])