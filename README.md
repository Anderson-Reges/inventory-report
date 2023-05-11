# O Inventory Report é um script que lida com as informações de um stock/inventory, desenvolvido durante meus estudos na [Trybe](https://www.betrybe.com/)

## :man_technologist: O que foi ser desenvolvido

Nesse projeto foi implementado um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

  <strong>🚵 Habilidades que foram trabalhadas:</strong>
 
  <ul>
    <li>Aplicar conceitos de Orientação a Objetos em Python;</li>
    <li>Aplicar padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON).</li>
  </ul>
  
  <strong>📄 Arquivos em que desenvolvi:</strong>
  
  <ul>
    <li>tests/product/test_product.py</li>
    <li>inventory_report/reports/simple_report.py</li>
    <li>inventory_report/reports/complete_report.py</li>
    <li>inventory_report/inventory/inventory.py</li>
    <li>inventory_report/importer/importer.py</li>
    <li>tests/product_report/test_product_report.py</li>
    <li>tests/report_decorator/test_report_decorator.py</li>
    <li>inventory_report/inventory/inventory_iterator.py</li>
    <li>inventory_report/main.py</li>
  </ul>
  
  *:warning: Atenção: fora esses arquivos todo resto é propriedade intelectual da Trybe*
  
## Técnologias usadas

<a href="https://www.python.org/" target="_blank">![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)</a>
  
## Instalando Dependências

> Crie um ambiemte virtual e ative:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

> Agora instale as dependencias:
```bash
python3 -m pip install -r dev-requirements.txt
```

> Execute para poder usar a linha comando:
```bash
pip install .
```

## Executando aplicação

Para executar o gerador de relatorio você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>
