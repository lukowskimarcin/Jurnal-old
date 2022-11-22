#https://blog.teclado.com/api-key-authentication-with-flask/
from service import MetaTraderService
import pprint
import pandas as pd
from datetime import datetime

service = MetaTraderService()

#pprint.pprint(service.get_symbols())
#pprint.pprint(service.symbol_info('DJI30'))
# pprint.pprint(service.symbol_info_tick('DJI30'))

# Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
#rates = service.copy_rates_from('DJI30', 'H1', datetime.utcnow(), 10)
# pprint.pprint(rates)

#rates = service.copy_rates_from_pos('DJI30', 'M30')
#pprint.pprint(rates[-1])
#print(datetime.utcfromtimestamp(rates[-1][0]))

#print("Margin needed: ", service.order_calc_margin('DJI30', 'SELL', 0.1), " USD" )
#print("SELL 33500->33400 profit: ", service.order_calc_profit('DJI30', 'SELL', 0.1, 33500, 33400))
#pprint.pprint(f'orders: {service.orders_get()}'  )


#print(service.positions_get())


print("====================================================")

res = service.history_orders(datetime(2022,11,22), datetime(2022,11,24))
#print(f'history_orders: {res}'  )
 
sum = 0
for order in res:
    print(order)
    print("\n")
    sum = sum + order['profit']


print(f"total profit: {sum} ")