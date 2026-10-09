# MongoDB Aggregation CLI

Я разработал консольный инструмент для загрузки JSON в MongoDB и выполнения aggregation pipeline.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Устройство проекта

Требуется локальная MongoDB на `localhost:27017`. Пункт импорта очищает выбранную коллекцию перед загрузкой — используйте отдельную учебную базу. JSON-данные и pipeline указываются через меню.

Я публикую исходный код без локальных паролей, окружений, баз и журналов. Для воспроизведения анализа я указываю необходимые данные и зависимости.

## Автор

Антон Никитин — [anton-nikitin21](https://github.com/anton-nikitin21).
