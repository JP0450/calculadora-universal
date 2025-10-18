import pytest

from bases.decimal import Decimal
from bases.binario import Binario
from bases.hexadecimal import Hexadecimal
from bases.octal import Octal
from bases.romano import Romano


def test_decimal_conversion_and_validation():
    d = Decimal("10")
    assert d.validar() is True
    assert d.a_decimal() == 10
    assert d.desde_decimal(15) == "15"


def test_binario_conversion_and_validation():
    b = Binario("1010")
    assert b.validar() is True
    assert b.a_decimal() == 10
    assert b.desde_decimal(10) == "1010"


def test_hexadecimal_conversion_and_validation():
    h = Hexadecimal("1F")
    assert h.validar() is True
    assert h.a_decimal() == 31
    assert h.desde_decimal(31) == "1F"


def test_octal_conversion_and_validation():
    o = Octal("17")
    assert o.validar() is True
    assert o.a_decimal() == 15
    assert o.desde_decimal(15) == "17"


def test_romano_conversion_and_validation():
    r = Romano("XIV")
    assert r.validar() is True
    assert r.a_decimal() == 14
    assert r.desde_decimal(14) == "XIV"


def test_sumar_and_restar_mixed_bases():
    # 10 (dec) + 1 (bin) => 11 en base decimal (se expresa en la base del primer operando)
    d = Decimal("10")
    b = Binario("1")
    assert d.sumar(b) == "11"

    # 10 (bin) + 1 (dec) => 11 en base binaria
    b2 = Binario("10")
    d2 = Decimal("1")
    assert b2.sumar(d2) == "11"

    # 10 (dec) - 1 (bin) => 9 en base decimal
    assert d.restar(b) == "9"

    # 10 (bin) - 1 (dec) => 1 en base binaria
    assert b2.restar(d2) == "1"


def test_invalid_values():
    assert Decimal("xyz").validar() is False
    assert Binario("102").validar() is False
    assert Hexadecimal("G").validar() is False
    assert Octal("89").validar() is False
    # Romano inválido: usar un símbolo no romano
    r = Romano("A")
    assert r.validar() is False
