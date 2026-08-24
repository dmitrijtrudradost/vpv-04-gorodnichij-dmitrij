# HTTP-запросы на Python (`requests`)

Учебный проект курса **Zerocoder** (задания 1–2): скрипт выполняет HTTP GET-запрос к удалённому серверу, анализирует ответ и корректно обрабатывает ошибки сети и тайм-аута.

Репозиторий: [dmitrijtrudradost/vpv-04-gorodnichij-dmitrij](https://github.com/dmitrijtrudradost/vpv-04-gorodnichij-dmitrij.git)

## Возможности

- GET-запрос к заданному URL с ограничением по времени (`timeout`)
- Вывод HTTP-статуса ответа
- Разбор ответа по `Content-Type`:
  - `application/json` — парсинг JSON и вывод первых 100 символов
  - иначе (например, HTML) — вывод первых 300 символов тела ответа
- Понятные сообщения для типичных статусов: `400`, `403`, `404`, `500`
- Обработка исключений:
  - `requests.exceptions.Timeout` — сервер не ответил вовремя
  - `requests.exceptions.ConnectionError` — нет сети / DNS / хост недоступен

## Структура проекта

```text
.
|── src/
│   └── main.py              # Скрипт HTTP-запроса
├── examples/
│   └── Screenshot ...png    # Пример вывода в терминале
├── .gitignore
└── README.md
```

## Требования

- Python **3.8+**
- Библиотека **requests**

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/dmitrijtrudradost/vpv-04-gorodnichij-dmitrij.git
cd zerocoder_lesson2
```

2. Создайте и активируйте виртуальное окружение:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:

```bash
pip install requests
```

## Запуск

```bash
python src/main.py
```

По умолчанию запрос идёт на `https://speedtest.ru` с таймаутом **5 секунд**.

## Пример вывода

![Пример запуска в терминале](examples/Screenshot%202026-08-21%20141224.png)

**Успешный ответ (HTML, статус 200):**

```text
Ответ запроса 200 к адрессу https://speedtest.ru
Первые 300 символов ответа: <!DOCTYPE html><html lang="ru">...
```

**Тайм-аут:**

```text
Тайм-аут запроса > 5 сек : сервер https://speedtest.ru не ответил вовремя
```

**Ошибка соединения:**

```text
Нет соединения: ошибка сети (DNS, недоступность хоста https://example.ru и т.п.)
```

## Как это работает

1. Выполняется `requests.get(url, timeout=timeout1)`.
2. Печатается код ответа и URL.
3. По заголовку `Content-Type` выбирается ветка:
   - JSON при статусе `200`
   - сообщение об ошибке при статусе ≠ `200`
   - фрагмент HTML/текста в остальных случаях
4. При сетевых сбоях срабатывают блоки `except`.

## Настройка

В начале файла `src/main.py` измените переменные:

```python
url = "https://speedtest.ru"  # целевой адрес
timeout1 = 5                  # таймаут в секундах
```

Для проверки обработки ошибок можно временно указать несуществующий хост или очень маленький `timeout` (например, `0.1`).

## Зависимости

| Пакет      | Назначение                   |
|------------|------------------------------|
| `requests` | HTTP-клиент для GET-запросов |

## Лицензия

Учебный проект. Свободное использование в рамках обучения.

## Автор

Дмитрий — курс Zerocoder, урок 2 / задание 1–2.
