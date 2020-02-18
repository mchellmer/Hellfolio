import risk_kit as erk
import matplotlib.pyplot as pyp
import pandas as pd

## Get and annualise historic returns
ind = pd.read_csv("data/ind30_m_vw_rets.csv", header=0, index_col=0)/100
ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period('M')
ind.columns = ind.columns.str.strip()
er = erk.annualize_rets(ind["1996":"2000"], 12)
cov = ind["1996":"2000"].cov()

## Define columns of returns and plot ef
l = ["Games", "Fin"]
erk.plot_ef(50, er[l], cov.loc[l,l])
pyp.show()

## Set a return to get weights for
ret = .15
weights_15 = erk.minimize_vol(ret, er[l], cov.loc[l,l])
print(weights_15)