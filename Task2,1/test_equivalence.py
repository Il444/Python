import pytest
from data import library_archive, crew_members, ship_systems
import solution_loops as loops
import solution_comprehension as compr

def test_a3():
    assert loops.get_old_short_books(library_archive) == compr.get_old_short_books(library_archive)

def test_a4():
    assert loops.group_by_author(library_archive) == compr.group_by_author(library_archive)

def test_a5():
    assert loops.average_pages(library_archive) == pytest.approx(compr.average_pages(library_archive))

def test_b3():
    assert loops.count_system_per_member(crew_members, ship_systems) == compr.count_system_per_member(crew_members, ship_systems)

def test_b4():
    assert loops.calculate_bonuses(crew_members) == compr.calculate_bonuses(crew_members)

def test_b5():
    assert loops.get_small_systems(ship_systems) == compr.get_small_systems(ship_systems)

def test_b6():
    assert loops.create_crew_profiles(crew_members, ship_systems) == compr.create_crew_profiles(crew_members, ship_systems)