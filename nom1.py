import math
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly import tools
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

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

 # проверка на достижение порогового уровня
def threshold_level():
	stock_amount = maximum_desired_amount_of_stock() # 810
	threshold_level = stock_threshold_level() # 810
	daily_consumption = expected_daily_consumption() # 90
	period_of_expenditure = period_of_expenditure_of_the_stock() # 8
	if stock_amount == threshold_level:
		print(stock_amount)	
		print("Величина запаса достигла порогового уровня в " + str(stock_amount) + " единиц")
	else:
		while stock_amount > threshold_level:
			stock_amount = stock_amount - daily_consumption
			print(stock_amount)
		print("Величина запаса достигла порогового уровня в " + str(stock_amount) + " единиц")
	
# достижение страхового уровня
def safe_level():
	stock_amount = maximum_desired_amount_of_stock() # 810
	daily_consumption = expected_daily_consumption() # 90
	stock_safety = safety_stock() # 180
	if stock_amount == stock_safety:
		print(stock_amount)
		print("Величина запаса достигла страхового уровня в " + str(stock_amount) + " единиц")
	else:
		while stock_amount > stock_safety:
			stock_amount = stock_amount - daily_consumption
			print(stock_amount)	
		print("Величина запаса достигла страхового уровня в " + str(stock_amount) + " единиц")

stock_amount = maximum_desired_amount_of_stock() # 810
daily_consumption = expected_daily_consumption() # 90
stock_safety = safety_stock() # 180
TOS = time_of_shipment() # 7

x = np.arange(0, 8, 1)

def f(x):
	stock_amount = maximum_desired_amount_of_stock() # 810
	daily_consumption = expected_daily_consumption() # 90
	stock_safety = safety_stock() # 180	
	return stock_amount - (daily_consumption*x)
	stock_amount = stock_amount - daily_consumption
	print(stock_amount)

# создание поля графика
fig = go.Figure()

# задание размеров поля графика
# параметры надо сделать зависимыми от величины запаса и количества дней расходования запаса
fig.update_yaxes(range=[0, 900], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.update_xaxes(range=[-10, 50], zeroline=True, zerolinewidth=2, zerolinecolor='#008000')

# создание дополнительных линий
fig.add_hline(y=maximum_desired_amount_of_stock(), line_dash="solid", line_color="#4682B4", line_width=7)
fig.add_hline(y=stock_threshold_level(), line_dash="solid", line_color="#1be098", line_width=2)
fig.add_hline(y=safety_stock(), line_dash="dash", line_color="#2547c2", line_width=2)

# добавление "полос" графика
fig.add_trace(go.Scatter(x=[x[0]], y=[f(x[0])], mode="lines+markers")) # trace 0

# добавление точек графика
frames = []
for i in range(1, len(x)):
	frames.append(go.Frame(data=[go.Scatter(x=x[:i+1], y=l(q[:i+1]))]))	# изменение trace 0
fig.frames = frames

# удаление отступов
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

# отображение значений у точек
fig.update_traces(hoverinfo="all", hovertemplate="День: %{x}<br>Величина запаса: %{y}")
plotly.offline.plot(fig)          		

print(f(x))

