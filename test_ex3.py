from ex3 import *

def test_ler_dimensoes_objeto():
    assert ler_dimensoes_objeto()
    assert ler_dimensoes_objeto()
    assert ler_dimensoes_objeto()

def test_calcular_preco_volume():
    assert calcular_preco_volume(100)==10.0
    
def test_validar_medida():
    assert validar_medida (1)==1

def test_ler_peso_objeto():
    assert ler_peso_objeto()

def test_calcular_multiplicador_peso():
    assert calcular_multiplicador_peso(10)==3.0


def test_ler_rota():
    assert ler_rota ()

def test_calcular_multiplicador_rota():
  assert calcular_multiplicador_rota("rs")==1.0
 




def test_calcular_frete():
 assert calcular_frete(50,50,50)==125000


def test_resultado_final_ex ():
    resultado_final_ex()

