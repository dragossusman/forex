import websocket
import http.client
import time
import statistics

def on_message(ws, message):
    print(message)
	test_price(message)
	
def test_price(message):
	
	# validate a price update: symbol name is correct
	if message.data.s != "APPL" or message.data.s != "AMZN" or message.data.s != "BINANCE:BTCUSDT" or message.data.s != "IC MARKETS:1":
		print("The symbol name is NOT correct")
		
	# validate a price update: last price bigger than 0
	if (message.data.p <= 0)
		print("The last price is NOT bigger than 0")
	# validate a price update: volume is bigger than 0
	if (message.data.volume <= 0)
		print("The volume is NOT bigger than 0")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

def validate_symbols(ws):
	#create the HTTP client
	con = http.client.HTTPConnection("finnhub.io/forex/symbols?exchange=oanda")
	con.request("GET", token="ccs2su2ad3i8m876bjrgccs2su2ad3i8m876bjs0")
	# list of responses
	resp = con.getresponse()
	# create a list
	expected_list = 
	[
		{
			"description": "IC MARKETS Euro vs US Dollar EURUSD",
			"displaySymbol": "EUR/USD",
			"symbol": "IC MARKETS:1"
		},
	{
			"description": "IC MARKETS Australian vs US Dollar AUDUSD",
			"displaySymbol": "AUD/USD",
			"symbol": "IC MARKETS:5"
	},
	{
			"description": "IC MARKETS British Pound vs US Dollar GBPUSD",
			"displaySymbol": "GBP/USD",
			"symbol": "IC MARKETS:2"
	}]
	if(resp.sort() != expected_list.sort()):
		print("The list of symbols in response is different than the expect list")

def performance_tests(ws):
	#create the HTTP client
	con = http.client.HTTPConnection("finnhub.io/forex/symbols?exchange=oanda")
	list_of_request_time = []
	for x in range(30):
		start = time.perf_counter()
		con.request("GET", token="ccs2su2ad3i8m876bjrgccs2su2ad3i8m876bjs0")
		request_time = time.perf_counter() - start
		list_of_request_time.append(request_time)
	
	#print mean of request time
	print("Mean of request time is: " + statistics.fmean(list_of_request_time))
	# print standard deviation of request time
	print("standard deviation of request time is: " + statistics.stdev(list_of_request_time))
	
if __name__ == "__main__":
    websocket.enableTrace(True)
	# I've added here the token for authentication
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=ccs2su2ad3i8m876bjrgccs2su2ad3i8m876bjs0",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
	ws.validate_symbols
	ws.performance_tests
    ws.run_forever()
