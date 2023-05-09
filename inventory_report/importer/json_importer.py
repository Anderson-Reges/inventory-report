from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(filename: str):
        data_list = list()
        if not filename.split(".")[-1] == "json":
            raise ValueError("Arquivo inválido")
        with open(filename) as file:
            inventory = json.load(file)
            for product in inventory:
                data_list.append(product)
        return data_list
