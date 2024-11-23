import pandas as pd
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
import os

users_path = Path('processed/users')
users_path.mkdir(parents=True, exist_ok=True)

p1 = Path('data/telecom10k/psx_62.0_2024-01-01 00_10_00.csv')
p2 = Path('data/telecom10k/psx_62.0_2024-01-01 00_20_00.csv')

def save_user_traffic(file_path, save_dir):
    df = pd.read_csv(file_path)

    user_list = df['IdSubscriber'].unique()

    for user_id in user_list:
        user_traffic = df[df['IdSubscriber'] == user_id]
        user_file_path = save_dir / f"{user_id}.csv"
        user_traffic.to_csv(user_file_path, mode='a', index=False)

save_user_traffic(p1, users_path)
save_user_traffic(p2, users_path)


# for x in Path("data/telecom10k").rglob("*"):
#     if x.name.startswith('psx_62.0') or x.name.startswith('psx_69.0') or x.name.startswith('psx_65.0'):
#         df = pd.read_csv(x, sep=',')
#         subsIdsList = df['IdSubscriber'].unique()
#         for s in subsIdsList:
#             sub_df = df.loc[df['IdSubscriber'] == s]
#             sub_df.to_csv(f'processed/subs/{s}.csv')

#     elif x.name.startswith('psx_66'):
#         df = pd.read_csv(x, sep='|')
#         subsIdsList = df['IdSubscriber'].unique()
#         for s in subsIdsList:
#             sub_df = df.loc[df['IdSubscriber'] == s]
#             sub_df.to_csv(f'processed/subs/{s}.csv')