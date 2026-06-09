from datetime import datetime
import os
import requests

YEAR = 2024

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5f2be56eabd275bf4fe98510938d2bb8fd390e37bc074581532106b0a5d361cb1bcaba5680d640d2dc8dc0be1bd5fd0113d038d3eea9ff7802'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
