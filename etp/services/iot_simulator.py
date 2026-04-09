import random

def get_live_sensor_data():
    """
    Simulates raw industrial effluent (Textile/Chemical mix)
    """
    return {
        "bod": round(random.uniform(200, 400), 2),
        "cod": round(random.uniform(500, 800), 2),
        "tss": round(random.uniform(300, 600), 2),
        "ph": round(random.uniform(4.0, 10.0), 2),
        "oil_grease": round(random.uniform(10, 50), 2),
        "cyanide": round(random.uniform(0.1, 2.0), 4),
        "ammonical_n": round(random.uniform(30, 70), 2)
    }