import requests
#url = "https://cloud.git-corp.ru"
url = "https://speedtest.ru"
timeout1 = 5
# Выводим контент страницы
try:
    response1 = requests.get(url, timeout = timeout1)
    statusget1 = response1.status_code
    print(f"Ответ запроса {statusget1} к адрессу {url}")

    content_type = response1.headers.get('Content-Type', '')

    if statusget1 == 200 and 'application/json' in content_type:
        data = response1.json()
        print("Заголовок Content-Type:", data)
        print("Первые 100 символов JSON:", str(data)[:100])

    elif statusget1 != 200:
        error_messages = {
            400: "Ошибка клиента: неверный запрос",
            403: "Ошибка доступа: запрещено",
            404: "Ресурс не найден",
            500: "Внутренняя ошибка сервера",
            
        }
        print(f"Ошибка: {error_messages.get(statusget1, 'Неизвестная ошибка')}")

    else:
        # Для HTML-страницы выводим первые 300 символов
        print("Первые 300 символов ответа:", response1.text[:300])

except requests.exceptions.Timeout:
    print(f"Тайм-аут запроса > {timeout1} сек : сервер {url} не ответил вовремя")

except requests.exceptions.ConnectionError:
    print(f"Нет соединения: ошибка сети (DNS, недоступность хоста {url} и т.п.)")