from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, "Bolacha", "Trakinus", "20/12/2022",
        "20/12/2023", "2ZSD5F1FD5", "Em local seco"
    )
    assert product.id == 1
    assert product.nome_do_produto == "Bolacha"
    assert product.nome_da_empresa == "Trakinus"
    assert product.data_de_fabricacao == "20/12/2022"
    assert product.data_de_validade == "20/12/2023"
    assert product.numero_de_serie == "2ZSD5F1FD5"
    assert product.instrucoes_de_armazenamento == "Em local seco"
