import pandas as pd
from pathlib import Path
from datetime import datetime
import os

os.makedirs('processed', exist_ok=True)

p = Path("data/telecom10k")

for x in p.rglob("*"):
    if (x.suffix == '.csv' or x.suffix == '.txt') and x.name.startswith('psx_'):
        if x.name.startswith('psx_62.0') or x.name.startswith('psx_69.0') or x.name.startswith('psx_65.0'):
            df = pd.read_csv(x, sep=',')
            df['StartSession'] = df['StartSession'].apply(
                lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M:%S'))
            df['StartSession'] = df['StartSession'] + pd.Timedelta(hours=5)

            df['UpTx'] = df['UpTx'].apply(
                lambda x: x*8)
            df['DownTx'] = df['DownTx'].apply(
                lambda x: x*8)

        elif x.name.startswith('psx_66'):
            df = pd.read_table(x, sep='|')
            df['StartSession'] = df['StartSession'].apply(
                lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))
            df['StartSession'] = df['StartSession'] + pd.Timedelta(hours=6)

        df = df.loc[df['UpTx'] > 0]
        df = df.loc[df['DownTx'] > 0]

        df.to_csv(f'processed/{x.name}')

