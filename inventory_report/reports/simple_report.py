from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(product_list: list[dict]):
        actual_date = datetime.now().strftime('%Y-%m-%d')
        old_fabrication = min(
            [
                product['data_de_fabricacao'] for product in product_list
            ]
        )
        old_validity = min(
            [
                product['data_de_validade'] for product in product_list
                if product['data_de_validade'] > actual_date
            ],
            default="EMPTY"
        )
        company_name = max(
            company['nome_da_empresa'] for company in product_list
        )

        return (
            f"""
            Data de fabricação mais antiga: {old_fabrication}
            Data de validade mais próxima: {old_validity}
            Empresa com mais produtos: {company_name}
            """
        )
