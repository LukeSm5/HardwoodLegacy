# NilEngine.py
# handles NIL negotiations and offers within the game

NIL_VALUES={
    "5_star": {
        "high": 10000000,
        "market_value": 5000000,
        "low": 2000000,
    },
    "4_star": {
        "high": 2000000,
        "market_value": 800000,
        "low": 400000,
    },
    "3_star": {
        "high": 400000,
        "market_value": 200000,
        "low": 100000
    },
    "2_star": {
        "high": 150000,
        "market_value": 75000,
        "low": 25000
    },
    "unranked": {
        "high": 100000,
        "market_value": 25000,
        "low": 0
    }
}
# The max each prestige level of a program can offer
PRESTIGE_OFFERS= {
    "blue_blood": {
        "max_offer": 10000000,
        "total_budget": 20000000
    },
    "high_major": {
        "max_offer": 5000000,
        "total_budget": 12500000
    },
    "mid_major": {
        "max_offer": 1000000,
        "total_budget": 2500000
    },
    "low_major": {
        "max_offer": 500000,
        "total_budget": 750000
    },
}

NEGOTIATION_OUTCOMES ={
    "accepted",
    "countered",
    "declined"
}

NIL_FACTORS={

}

def calculate_nil_market_value(ranking: str):
    if ranking not in NIL_VALUES:
        raise ValueError(f"Invalid ranking: {ranking}")
    return NIL_VALUES[ranking]["market_value"]

def calculate_nil_budget(prestige_tier: str):
    if prestige_tier not in PRESTIGE_OFFERS:
        raise ValueError(f"Invalid Prestige: {prestige_tier}")
    return PRESTIGE_OFFERS[prestige_tier]["total_budget"]

def generate_initial_nil_offer():
    pass

def process_negotiation():
    pass

def calculate_nil_influence():
    pass

def update_nil_budget(remaining_budget: int, nil_offer: int):
    if remaining_budget - nil_offer < 0:
        raise ValueError(f"Too large of an NIL offer")
    return remaining_budget - nil_offer