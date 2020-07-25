import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def portfolio_mean(w: [float], r: [float]):
    return w.dot(r)


def portfolio_var(w: [float], r: [float]):
    cov = np.cov(r)
    return w.T.dot(cov).dot(w)


xom = pd.read_csv('./data/XOM.csv').sort_values('Date')['Adj Close'].to_numpy()
aapl = pd.read_csv('./data/AAPL.csv').sort_values('Date')['Adj Close'].to_numpy()
ge = pd.read_csv('./data/GE.csv').sort_values('Date')['Adj Close'].to_numpy()
unh = pd.read_csv('./data/UNH.csv').sort_values('Date')['Adj Close'].to_numpy()
ba = pd.read_csv('./data/BA.csv').sort_values('Date')['Adj Close'].to_numpy()

N = 253
stocks = [xom, ba]
stocks = [np.array([x[i+N]/x[i] - 1
          for i in range(0, len(x)-N, N)])
          for x in stocks]
cov = np.cov(stocks)
corr = cov[0][1] / (np.var(stocks[0]) ** 0.5 * np.var(stocks[1]) ** 0.5)
print('cov:\n', cov)
print('corr:\n', corr)
r = [np.mean(i) for i in stocks]
variance = [np.var(i) for i in stocks]
print(r)
print(variance)


all_mus = []
all_vars = []
all_w = []
for i in range(1000):
    w = np.random.rand(len(stocks))
    w = w/sum(w)
    r = [np.mean(i) for i in stocks]
    mu = portfolio_mean(w, r)
    var = portfolio_var(w, r)
    all_w.append(w)
    all_mus.append(mu)
    all_vars.append(var)

idx = all_vars.index(min(all_vars))
print(all_vars[idx])
print(all_w[idx])
plt.scatter(all_vars, all_mus, marker='x', s=10)
plt.show()
