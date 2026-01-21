# General config & assumptions

DAYS = 30
DAILY_INSTALLS = 20_000

ARPPU = 5.0   # educated guess for microtransaction heavy games

VARIANTS = {
    "A": {
        "purchase_rate": 0.0305,
        "ecpm": 9.80,
        "ads_per_dau": 2.3,
        "retention_points": {
            1: 0.53,
            3: 0.27,
            7: 0.17,
            14: 0.06
        }
    },
    "B": {
        "purchase_rate": 0.0315,
        "ecpm": 10.80,
        "ads_per_dau": 1.6,
        "retention_points": {
            1: 0.48,
            3: 0.25,
            7: 0.19,
            14: 0.09
        }
    }
}

SALE_START = 15
SALE_END = 25
SALE_UPLIFT = 0.01

NEW_SOURCE_START = 20
OLD_SOURCE_INSTALLS = 12_000
NEW_SOURCE_INSTALLS = 8_000
