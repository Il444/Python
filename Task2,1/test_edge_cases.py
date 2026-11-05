import pytest
import solution_comprehension as compr
import solution_loops as loops
from data import library_archive

def test_average_empty():
    assert loops.average_pages([]) == 0.0
    assert compr.average_pages([]) == 0.0

def test_a3_empty():
    assert loops.get_old_short_books([]) == []
    assert compr.get_old_short_books([]) == []

def test_b5_empty():
    assert loops.get_small_systems({}) == []
    assert compr.get_small_systems({}) == []

def test_average_known_answer():
    assert loops.average_pages(library_archive) == pytest.approx(330.1)
    assert compr.average_pages(library_archive) == pytest.approx(330.1)