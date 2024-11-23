import pyarrow.parquet as pq

client_file_path = "data/client.parquet"

'''
Выводит данные о пользователях
@filter - фильтрация клиентов перед отображением
'''
def getClients(filter = None):

    if (filter is not None):
        count_rows = filter["records_per_page"]
        range_start = (filter["range"] - 1) * count_rows
        range_end = filter["range"] * count_rows
    else:
        range_start = 0
        range_end = 10


    try:
        client_data = pq.read_table(client_file_path).to_pandas()
        count_clients = client_data.shape[0]
        filtered_data = client_data.iloc[range_start:range_end]

        return [
            True, 
            filtered_data, 
            count_clients
        ]
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return [
            False, 
            None,
            0
        ]