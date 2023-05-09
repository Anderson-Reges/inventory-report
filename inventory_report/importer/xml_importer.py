from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(filename: str):
        if not filename.split(".")[-1] == "xml":
            raise ValueError("Arquivo inválido")
        tree = ET.parse(filename)
        root = tree.getroot()
        data_list = [
          {product.tag: product.text for product in record}
          for record in root
        ]
        return data_list
