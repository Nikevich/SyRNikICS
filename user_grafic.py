import pandas as pd
import matplotlib.pyplot as plt
import math

def getUpTx(path_subs):
    data = pd.read_csv('processed/subs/' + path_subs)  # Замените на путь к вашему файлу
    # Рассчитываем время начала каждой строки с учетом продолжительности
    data['Timestamp'] = pd.to_datetime(data['StartSession']) + pd.to_timedelta(data['Duartion'], unit='s')

    count = data.shape[0]

    for i in range(count - 1, 0, -1):  # Обратный цикл
        if pd.isna(data.loc[i, 'EndSession']):
            data.loc[i, 'UpTx'] = data.loc[i, 'UpTx'] - data.loc[i - 1, 'UpTx']
        if data.loc[i, 'UpTx'] < 0:
            data.loc[i, 'UpTx'] = data.loc[i, 'UpTx'] * (-1) 


    # Строим график
    plt.figure(figsize=(12, 6))

    # Линия для UpTx
    plt.plot(data['Timestamp'], data['UpTx'], 'r.')

    # Настройки графика
    plt.title('UpTx', fontsize=14)
    plt.xlabel('Время', fontsize=12)
    plt.ylabel('Трафик (bytes)', fontsize=12)
    plt.grid(True)

    plt.savefig("data/traffic_plot_UpTx.png")  # Сохраняем график в файл
    return 'data/traffic_plot_UpTx.png'

def getDownTx(path_subs):
    data = pd.read_csv('processed/subs/' + path_subs)  # Замените на путь к вашему файлу
    # Рассчитываем время начала каждой строки с учетом продолжительности
    data['Timestamp'] = pd.to_datetime(data['StartSession']) + pd.to_timedelta(data['Duartion'], unit='s')

    count = data.shape[0]

    for i in range(count - 1, 0, -1):  # Обратный цикл
        if pd.isna(data.loc[i, 'EndSession']):
            data.loc[i, 'DownTx'] = data.loc[i, 'DownTx'] - data.loc[i - 1, 'DownTx']
        if data.loc[i, 'DownTx'] < 0:
            data.loc[i, 'DownTx'] = data.loc[i, 'DownTx'] * (-1) 


    # Строим график
    plt.figure(figsize=(12, 6))

    # Линия для DownTx
    plt.plot(data['Timestamp'], data['DownTx'], 'r.')

    # Настройки графика
    plt.title('DownTx', fontsize=14)
    plt.xlabel('Время', fontsize=12)
    plt.ylabel('Трафик (bytes)', fontsize=12)
    plt.grid(True)

    plt.savefig("data/traffic_plot_DownTx.png")  # Сохраняем график в файл
    return 'data/traffic_plot_DownTx.png'
print("График сохранён как 'traffic_plot.png'")