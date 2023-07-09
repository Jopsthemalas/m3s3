from ex4 import *

def test_code():
    assert gerar_codigo() 
    assert cadastrar_peca()
    assert imprimir_peca ({
        'codigo': '100',
        'nome': 'peca',
        'fabricante': 'fabricante',
        'valor': 200.0
    }) == '100 fabricante 200.0'


   
    assert consultar_pecas ()== 1

    assert remover_peca ()== 1

    assert definicao ()