import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        if report_type == "simples":
            with open(path, encoding="utf-8") as file:
                inventory = csv.DictReader(file, delimiter=",", quotechar='"')
                inventory_list_simple = list()
                for product in inventory:
                    inventory_list_simple.append(product)
                return SimpleReport.generate(inventory_list_simple)
        else:
            with open(path, encoding="utf-8") as file:
                inventory = csv.DictReader(file, delimiter=",", quotechar='"')
                inventory_list_complete = list()
                for product in inventory:
                    inventory_list_complete.append(product)
                return CompleteReport.generate(inventory_list_complete)
