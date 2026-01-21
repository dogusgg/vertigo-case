import pandas as pd

def simulate_dau(retention_fn, daily_installs, days):
    dau = []

    for day in range(1, days + 1):
        active = 0
        for install_day in range(1, day + 1):
            age = day - install_day + 1
            active += daily_installs * retention_fn(age)
        dau.append(active)

    return pd.Series(dau, index=range(1, days + 1))
