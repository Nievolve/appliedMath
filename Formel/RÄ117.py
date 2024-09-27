import numpy as np
import matplotlib as plt

def Um(Ue,Ie,L,A,rå):
    Um = Ue-(2*rå*L/A)*Ie
    return Um
Ue = 230
Ie = 5.00



material_resistance = [
    {"material": "Silver", "resistivity_ohm_meter": 1.59e-8},
    {"material": "Copper", "resistivity_ohm_meter": 1.68e-8},
    {"material": "Gold", "resistivity_ohm_meter": 2.44e-8},
    {"material": "Aluminum", "resistivity_ohm_meter": 2.82e-8},
    {"material": "Tungsten", "resistivity_ohm_meter": 5.60e-8},
    {"material": "Iron", "resistivity_ohm_meter": 9.71e-8},
    {"material": "Platinum", "resistivity_ohm_meter": 1.06e-7},
    {"material": "Nickel", "resistivity_ohm_meter": 6.99e-8}
]
cable_cross_sections = [
    1.5,   # mm²
    2.5,   # mm²
    4.0,   # mm²
    6.0,   # mm²
    10.0   # mm²
]
cable_lengths = [
    50.0,  # meter
    75.0,  # meter
    100.0, # meter
    125.0, # meter
    150.0  # meter
]
