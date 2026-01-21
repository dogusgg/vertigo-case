import numpy as np
from scipy.interpolate import interp1d

def build_log_linear_retention(retention_points):
    days = np.array(list(retention_points.keys()))
    rates = np.array(list(retention_points.values()))

    log_rates = np.log(rates)
    interpolator = interp1d(days, log_rates, fill_value="extrapolate")

    def retention(day):
        if day < 1:
            return 1.0
        return float(np.exp(interpolator(day)))

    return retention


def exponential_retention(a, b):
    def retention(day):
        if day < 1:
            return 1.0
        return a * np.exp(-b * (day - 1))
    return retention
