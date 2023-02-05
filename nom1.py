from prettytable import PrettyTable
import math

days = []
values = []

# задание параметров
def requirement(): #1
	param1 = 20000
	return param1

def EOQ(): #2
	param2 = 630
	return param2

def time_of_shipment(): #3
	param3 = 7
	return param3

def possible_time_of_delivery_delay(): #4
	param4 = 2
	return param4

def expected_daily_consumption(): #5
	param5 = math.ceil(requirement() / 226)
	if param5 % 10 != 0 and EOQ() % 10 == 0:
		param5 = param5 / 10
		param5 = math.ceil(param5)
		param5 = 10*param5
		return param5
	return param5

def period_of_expenditure_of_the_stock(): #6
	param6 = math.ceil(EOQ() / expected_daily_consumption())
	return param6

def expected_consumption_during_delivery(): #7
	param7 = math.ceil(time_of_shipment() * expected_daily_consumption())
	return param7

def maximum_consumption_during_delivery(): #8
	param8 = ((time_of_shipment() + possible_time_of_delivery_delay()) * expected_daily_consumption())
	return param8

def safety_stock(): #9
	param9 = maximum_consumption_during_delivery() - expected_consumption_during_delivery()
	return param9

def stock_threshold_level(): #10
	param10 = safety_stock() + expected_consumption_during_delivery()
	return param10

def maximum_desired_amount_of_stock(): #11
	param11 = safety_stock() + EOQ()
	return param11

def period_of_consumption_of_the_stock_up_to_the_threshold_level(): #12
	param12 = math.ceil((maximum_desired_amount_of_stock() - stock_threshold_level()) / expected_daily_consumption())
	return param12
	
# достижение страхового уровня, пополнение запаса
def safe_level():
	stock_amount = maximum_desired_amount_of_stock() # 810
	threshold_level = stock_threshold_level() # 810
	daily_consumption = expected_daily_consumption() # 90
	stock_safety = safety_stock() # 180

	for i in range(1, (time_of_shipment()+1)):
		days.append(i)

	# разобраться с циклами
	if stock_amount == threshold_level:
		print("Величина запаса достигла порогового уровня в " + str(stock_amount) + " единиц")
		print("\n")
	else:
		while stock_amount > threshold_level:
			stock_amount = stock_amount - daily_consumption
		print("Величина запаса достигла порогового уровня в " + str(stock_amount) + " единиц")
		print("\n")

	if stock_amount == stock_safety:
		print("Величина запаса достигла страхового уровня в " + str(stock_amount) + " единиц")
		print("\n")
	else:
		while stock_amount > stock_safety:
			stock_amount = stock_amount - daily_consumption
			values.append(stock_amount)
		print("Величина запаса достигла страхового уровня в " + str(stock_amount) + " единиц")
		print("\n")

	print(days, values)

safe_level()
