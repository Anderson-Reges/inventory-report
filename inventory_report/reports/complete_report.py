from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(product_list: list[dict]) -> str:
        simple = super(CompleteReport, CompleteReport).generate(product_list)
        complete = dict()
        complete_return = ''
        for product in product_list:
            if product["nome_da_empresa"] in complete:
                complete[product["nome_da_empresa"]] += 1
            else:
                complete[product["nome_da_empresa"]] = 1

        for company in complete.items():
            complete_return += f"- {company[0]}: {company[1]}\n"
        return (
            f'{simple}'
            f'\nProdutos estocados por empresa:\n'
            f'{complete_return}'
        )
