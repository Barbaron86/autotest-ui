import pytest


@pytest.mark.xfail(reason="Тест содержит баг, который нужно исправить")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте все еще висит маркировка xfail")
def test_without_bug(): ...
