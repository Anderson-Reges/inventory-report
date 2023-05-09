from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(product_list: list[dict]) -> str:
        actual_date = datetime.now().strftime('%Y-%m-%d')
        old_fabrication: int = min(
            [
                product['data_de_fabricacao'] for product in product_list
            ]
        )
        old_validity: int = min(
            [
                product['data_de_validade'] for product in product_list
                if product['data_de_validade'] > actual_date
            ]
        )
        company_name: str = max(
            company['nome_da_empresa'] for company in product_list
        )
        company_name_rm_limited = company_name.replace('LIMITED', '').strip()

        return (
            f"Data de fabricação mais antiga: {old_fabrication}\n"
            f"Data de validade mais próxima: {old_validity}\n"
            f"Empresa com mais produtos: {company_name_rm_limited}"
        )
