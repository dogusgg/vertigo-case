def calculate_revenue(dau, purchase_rate, arppu, ads_per_dau, ecpm):
    iap = dau * purchase_rate * arppu
    ads = dau * ads_per_dau * ecpm / 1000
    return iap + ads
