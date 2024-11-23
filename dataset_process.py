import pandas as pd
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
import shutil
import os

'''
Обработка датасета
Приводит к единому формату дату, время, часовой пояс, разделители
Чтобы не заморачиваться, можно воспользоваться архивом data.zip, который необходимо разархивировать в корневую директорию проекта
@dataset_path - путь к датасету
'''
def clearDataset(dataset_path = 'data/telecom10k'):
    if os.path.exists('processed'):
        shutil.rmtree('processed')

    os.makedirs('processed', exist_ok=True)

    p = Path(dataset_path)

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

            df.to_csv(f'processed/{x.name}', index=False)

'''
Создает csv файлы с трафиком каждого пользователя отдельно
Выполнение может быть заменено архивом data.zip
!!! ПЕРЕД ВЫПОЛНЕНИЕМ ВЫПОЛНИТЬ clearDataset() !!!
'''
def makeUserTraffic():
    if os.path.exists('processed/subs'):
        shutil.rmtree('processed/subs')

    os.makedirs('processed/subs', exist_ok=True)

    for x in Path("processed").rglob("*"):
        if x.name.startswith('psx_62.0') or x.name.startswith('psx_69.0') or x.name.startswith('psx_65.0'):
            df = pd.read_csv(x, sep=',')
            subsIdsList = df['IdSubscriber'].unique()
            for s in subsIdsList:
                sub_file_name = f'processed/subs/{s}.csv'
                sub_df = df.loc[df['IdSubscriber'] == s]

                if os.path.exists(sub_file_name):
                    sub_df.to_csv(sub_file_name, mode='a', header=False, index=False)
                else:
                    sub_df.to_csv(sub_file_name, mode='a', header=True, index=False)


        elif x.name.startswith('psx_66'):
            df = pd.read_csv(x, sep=',')
            subsIdsList = df['IdSubscriber'].unique()
            for s in subsIdsList:
                sub_file_name = f'processed/subs/{s}.csv'
                sub_df = df.loc[df['IdSubscriber'] == s]

                if os.path.exists(sub_file_name):
                    sub_df.to_csv(sub_file_name, mode='a', header=False, index=False)
                else:
                    sub_df.to_csv(sub_file_name, mode='a', header=True, index=False)