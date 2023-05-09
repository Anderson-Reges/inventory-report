from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(filename: str):
        data_list = list()
        if not filename.split(".")[-1] == "csv":
            raise ValueError("Arquivo inválido")
        with open(filename) as file:
            inventory = csv.DictReader(file)
            for product in inventory:
                data_list.append(product)
        return data_list
