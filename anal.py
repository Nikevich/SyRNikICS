
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def analyze_session_traffic(data):
    # Читаем данные из CSV файла
    data = pd.read_csv("data/telecom10k")

    # Проверяем, что данные содержат необходимые столбцы
    if 'session_time' not in data.columns or 'traffic' not in data.columns:
        raise ValueError("Данные должны содержать столбцы 'session_time' и 'traffic'.")

    # Выводим зависимость между временем сессии и отданным трафиком
    plt.figure(figsize=(10, 6))
    plt.plot(data['session_time'], data['traffic'], marker='o')
    plt.title('Зависимость отданного трафика от времени сессии')
    plt.xlabel('Время сессии ')
    plt.ylabel('Отданный трафик ')
    plt.grid()
    plt.show()

    # Создаем словарь для соответствия времени сессии и отданного трафика
    session_traffic_dict = dict(zip(data['session_time'], data['traffic']))

    return session_traffic_dict

def analyze_traffic_fft(session_traffic_dict):
    traffic = np.array(session_traffic_dict['traffic'])
    time = np.array(session_traffic_dict['session_time'])

    # Выполнение преобразования Фурье
    fft_result = np.fft.fft(traffic)
    fft_freq = np.fft.fftfreq(len(traffic), d=(time[1] - time[0]))  # Частоты

    # Визуализация результата
    plt.figure(figsize=(12, 6))

    # График амплитуды
    plt.subplot(2, 1, 1)
    plt.plot(fft_freq, np.abs(fft_result), marker='o')
    plt.title('Преобразование Фурье: амплитуда')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.grid()

    # График фазы
    plt.subplot(2, 1, 2)
    plt.plot(fft_freq, np.angle(fft_result), marker='o', color='orange')
    plt.title('Преобразование Фурье: фаза')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Фаза (рад)')
    plt.grid()
    analyze_traffic_fft(session_traffic_dict)