import pandas as pd
import mplfinance as mpf
import ccxt

binance = ccxt.binance()
ohlcv = binance.fetch_ohlcv("BTC/USDT", timeframe = '5m', limit = 100)

df = pd.DataFrame(ohlcv, columns = ["Date", "Open", "High", "Low", "Close", "Volume"])
df["Date"] = pd.to_datetime(df["Date"], unit = 'ms')
df.set_index("Date", inplace=True)

df["EMA5"] = df["Close"].ewm(span = 5).mean()

df['prev_Close'] = df['Close'].shift(1)
df['prev_EMA5'] = df['EMA5'].shift(1)
df['cross_up'] = (df['prev_Close'] < df['prev_EMA5']) & (df['Close'] > df['EMA5'])


cross_points = df[df['cross_up']]

if not cross_points.empty:
    cross_index = cross_points.index[0]  # 첫 번째 돌파 시점
    idx = df.index.get_loc(cross_index)  # 전체 df에서의 인덱스 위치
    df_focus = df.iloc[max(idx-10, 0):idx+10]  # 돌파 전후 10개 캔들 잘라냄

mpf.plot(df_focus, type='candle', mav=(5), volume=True, style='yahoo',
         savefig='ema5_example_focus.png')
