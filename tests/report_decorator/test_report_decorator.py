from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport


def test_decorar_relatorio():
    list = [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        },
        {
            "id": 2,
            "nome_do_produto": "Mocha",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2023-05-08",
            "data_de_validade": "2024-12-31",
            "numero_de_serie": "CN101",
            "instrucoes_de_armazenamento": "instrucao",
        },
    ]

    simple_report = SimpleReport()
    complete_report = CompleteReport()

    colored_simple_report = ColoredReport(simple_report)
    colored_complete_report = ColoredReport(complete_report)

    colored_keys = [
        "\033[32mData de fabricação mais antiga:\033[0m",
        "\033[32mData de validade mais próxima:\033[0m",
        "\033[32mEmpresa com mais produtos:\033[0m",
    ]

    colored_values = [
        "\033[36m2020-07-04\033[0m",
        "\033[36m2024-12-31\033[0m",
        "\033[31mCafes Nature\033[0m",
    ]

    expected_simple_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}"
    )

    expected_complete_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}\n"
        "Produtos estocados por empresa:\n"
        "- Cafes Nature: 2\n"
    )

    assert colored_simple_report.generate(list) == (
        expected_simple_report
    )
    assert colored_complete_report.generate(list) == (
        expected_complete_report
    )
