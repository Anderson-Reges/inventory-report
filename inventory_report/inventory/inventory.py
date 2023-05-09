import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_importer(path: str) -> list[dict]:
        with open(path, encoding="utf-8") as file:
            inventory = csv.DictReader(file, delimiter=",", quotechar='"')
            inventory_list = list()
            for product in inventory:
                inventory_list.append(product)
            return inventory_list

    def json_import(path: str) -> list[dict]:
        with open(path) as file:
            inventory = json.load(file)
            inventory_list = list()
            for product in inventory:
                inventory_list.append(product)
        return inventory_list

    def xml_importer(path: str) -> list[dict]:
        tree = ET.parse(path)
        root = tree.getroot()
        inventory_list = [
          {product.tag: product.text for product in record}
          for record in root
        ]
        return inventory_list

    @classmethod
    def check_file_extension(cls, path: str) -> list[dict]:
        if path.split(".")[-1] == "csv":
            return cls.csv_importer(path)
        elif path.split(".")[-1] == "json":
            return cls.json_import(path)
        elif path.split(".")[-1] == "xml":
            return cls.xml_importer(path)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def import_data(cls, path: str, report_type: str) -> str:
        importer = cls.check_file_extension(path)
        if report_type == "simples":
            return SimpleReport.generate(importer)
        else:
            return CompleteReport.generate(importer)
