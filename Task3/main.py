import solution_loops as solution
from data import library_archive
from data import crew_members
from data import ship_systems


def print_result(title: str, data):
    print(f"--- {title} ---")

    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")

    elif isinstance(data, list):
        for item in data:
            print(item)

    elif isinstance(data, float):
        print(f"{data:.2f}")

    else:
        print(data)


def main():
    print_result("A3: ", solution.get_old_short_books(library_archive))
    print_result("A4: ", solution.group_by_author(library_archive))
    print_result("A5: ", solution.average_pages(library_archive))

    print_result("B3: ", solution.count_system_per_member(crew_members, ship_systems))
    print_result("B4: ", solution.calculate_bonuses(crew_members))
    print_result("B5: ", solution.get_small_systems(ship_systems))

    profiles = solution.create_crew_profiles(crew_members, ship_systems)
    print("--- B6: Profiles ---")
    for profile in profiles:
        print(profile)