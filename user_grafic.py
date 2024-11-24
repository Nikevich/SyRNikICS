import pandas as pd
import matplotlib.pyplot as plt
import math

# Чтение данных
data = pd.read_csv('processed/subs/4187.csv')  # Замените на путь к вашему файлу

# Рассчитываем время начала каждой строки с учетом продолжительности
data['Timestamp'] = pd.to_datetime(data['StartSession']) + pd.to_timedelta(data['Duartion'], unit='s')

count = data.shape[0]

for i in range(count - 1, 0, -1):  # Обратный цикл
    if pd.isna(data.loc[i, 'EndSession']):
        data.loc[i, 'UpTx'] = data.loc[i, 'UpTx'] - data.loc[i - 1, 'UpTx']


# Строим график
plt.figure(figsize=(12, 6))

# Линия для UpTx
plt.plot(data['Timestamp'], data['UpTx'], 'b')
# plt.plot(data['Timestamp'], data['DownTx'], 'r')

# Настройки графика
plt.title('Использование трафика по времени', fontsize=14)
plt.xlabel('Время', fontsize=12)
plt.ylabel('Трафик (bytes)', fontsize=12)
plt.grid(True)

plt.savefig("traffic_plot.png")  # Сохраняем график в файл
print("График сохранён как 'traffic_plot.png'")