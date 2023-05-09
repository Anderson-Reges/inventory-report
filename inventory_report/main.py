import sys
from inventory_report.inventory.inventory import Inventory


def main():
    try:
        input_path = sys.argv[1]
        report_type = sys.argv[2]
        report = Inventory.import_data(input_path, report_type)
        sys.stdout.write(report)
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")


if __name__ == "__main__":
    main()
