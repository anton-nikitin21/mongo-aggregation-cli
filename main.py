import json
import os
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["postgres_project_mongo"]


def get_collection_name(file_path):
    file_name = os.path.basename(file_path)
    collection_name = os.path.splitext(file_name)[0]
    return collection_name


def load_json_to_collection():
    file_path = input("Введите путь к JSON-файлу с данными: ").strip('"')

    collection_name = get_collection_name(file_path)
    collection = db[collection_name]

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    collection.delete_many({})

    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print(f"Данные загружены в коллекцию: {collection_name}")


def run_aggregation():
    collection_file_path = input("Введите путь к JSON-файлу коллекции: ").strip('"')
    pipeline_file_path = input("Введите путь к JSON-файлу с этапами агрегации: ").strip('"')

    collection_name = get_collection_name(collection_file_path)
    collection = db[collection_name]

    with open(pipeline_file_path, "r", encoding="utf-8") as file:
        pipeline = json.load(file)

    result = collection.aggregate(pipeline)

    print("\nРезультат агрегации:")
    for document in result:
        print(document)


def main():
    while True:
        print("\nМеню:")
        print("1 — Загрузить JSON в коллекцию")
        print("2 — Выполнить агрегацию")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            load_json_to_collection()
        elif choice == "2":
            run_aggregation()
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню")


main()