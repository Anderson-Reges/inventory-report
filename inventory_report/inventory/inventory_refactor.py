from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path: str, report_type: str):
        new_data = self.importer.import_data(file_path)
        self.data += new_data

    def generate_report(self, report_type):
        if report_type == "simples":
            report = SimpleReport.generate(self.data)
        elif report_type == "completo":
            report = CompleteReport.generate(self.data)
        else:
            raise ValueError("Invalid report type")

        return report

    def __iter__(self):
        return InventoryIterator(self.data)
