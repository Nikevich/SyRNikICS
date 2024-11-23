import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных
data = pd.read_csv('processed/subs/3904.csv')  # Замените на путь к вашему файлу

# Рассчитываем время начала каждой строки с учетом продолжительности
data['Timestamp'] = pd.to_datetime(data['StartSession']) + pd.to_timedelta(data['Duartion'], unit='s')

x = []

for i in range(data.shape[0]):
    x.append(i)

# Строим график
plt.figure(figsize=(12, 6))

# Линия для UpTx
plt.plot(x, data['UpTx'], 'b')
plt.plot(x, data['DownTx'], 'r')

# Настройки графика
plt.title('Использование трафика по времени', fontsize=14)
plt.xlabel('Время', fontsize=12)
plt.ylabel('Трафик (bytes)', fontsize=12)
plt.grid(True)

plt.savefig("traffic_plot.png")  # Сохраняем график в файл
print("График сохранён как 'traffic_plot.png'")