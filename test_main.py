import pytest
import pygame
from main import escalar_img, contar_elementos, nombres_carpetas

pygame.init()

def test_escalar_img():
    # Crear una superficie para simular una imagen
    original = pygame.Surface((100, 100))
    escalada = escalar_img(original, 2)
    assert escalada.get_width() == 200
    assert escalada.get_height() == 200

def test_contar_elementos(tmpdir):
    # Crear un directorio temporal
    test_dir = tmpdir.mkdir("test_dir")
    test_dir.join("file1.txt").write("content")
    test_dir.join("file2.txt").write("content")
    count = contar_elementos(str(test_dir))
    assert count == 2

def test_nombres_carpetas(tmpdir):
    # Crear subdirectorios dentro del directorio temporal
    test_dir = tmpdir.mkdir("test_dir")
    test_dir.mkdir("subdir1")
    test_dir.mkdir("subdir2")
    names = sorted(nombres_carpetas(str(test_dir)))
    assert names == ["subdir1", "subdir2"]



