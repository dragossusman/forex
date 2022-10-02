# forex
1) WebSocket tests.
a) subscribe for any stock, forex symbol or crypto to get price updates
(https://XXXXXXX.io/docs/api/websocket-trades).
b) validate a price update: symbol name is correct, last price bigger
than 0,
volume is bigger than 0.
2) REST API tests:
a) prepares the test environment (initialize network session etc.)
b) validate the list of symbols for the specific forex exchange.
Compare with some static list.
(https://XXXXXXXX.io/docs/api/forex-exchanges)
Task #2: Performance test suite
3) Create a performance test suite that:
a) accesses one of the end-points continuously for a certain number of
times e.g. 30 times
(sequential access is fine)
b) for each access keeps track of the response time on the client side
e) prints out mean &amp; standard deviation of the response time for the
end-point.
