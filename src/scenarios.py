from .retention import exponential_retention

def apply_sale(purchase_rate, day, start, end, uplift):
    if start <= day <= end:
        return purchase_rate + uplift
    return purchase_rate


def get_new_source_retention(variant):
    if variant == "A":
        return exponential_retention(0.58, 0.12)
    if variant == "B":
        return exponential_retention(0.52, 0.10)
