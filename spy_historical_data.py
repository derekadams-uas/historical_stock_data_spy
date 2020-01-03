import requests
import json

res = requests.get(
    'https://api.worldtradingdata.com/api/v1/history?symbol=SPY&sort=newest&api_token=1PuMQqtLgDksslLmJMFOmxhpkybV4otV3zjyCkFyw7Oy6z1MhbFZwE0G1dKY&date_from=2018-01-02&date_to=2018-01-03',)

data = res.json()
print(data)

dates = data['history'].items()
day_deltas_raw = {}
day_deltas_pct = {}
day_ranges_raw = {}
day_ranges_pct = {}
day_volumes = {}

for k, v in dates:
    date_metrics = dict(v.items())
    day_open = float(date_metrics['open'])
    day_close = float(date_metrics['close'])
    day_high = float(date_metrics['high'])
    day_low = float(date_metrics['low'])
    day_volume = int(date_metrics['volume'])

    day_delta_raw = day_close - day_open
    day_delta_pct = day_delta_raw / day_open * 100
    day_range_raw = day_high - day_low
    day_range_pct = day_range_raw / day_open * 100

    day_deltas_raw[k] = day_delta_raw
    day_deltas_pct[k] = day_delta_pct
    day_ranges_raw[k] = day_range_raw
    day_ranges_pct[k] = day_range_pct
    day_volumes[k] = day_volume


print(day_deltas_raw)
print(day_deltas_pct)
print(day_ranges_raw)
print(day_ranges_pct)
print(day_volumes)
