from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas as pd
import json

WarframesResponse = urlopen("https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Warframes.json")
WDF = pd.read_json(WarframesResponse)

print(WDF)
WDF['masteryPoints'] = 6000
WDF.to_excel('frames.xlsx', engine='xlsxwriter')

