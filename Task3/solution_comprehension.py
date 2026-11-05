YEAR_THRESHOLD = 1950
PAGES_THRESHOLD = 300
EXPERIENCE_THRESHOLD = 5
BONUS_HIGH_RATE = 0.15
BONUS_LOW_RATE = 0.1
WORKERS_THRESHOLD = 2

def get_old_short_books(archive: list) -> list:
    return [title for title, _, year, pages, _ in archive if year < YEAR_THRESHOLD and pages < PAGES_THRESHOLD]
def group_by_author(archive: list) -> dict:
    authors = {auth for  title, auth, year, pages, genre in archive}
    return {author: [(title, author, year, pages, genre) for title, auth, year, pages, genre in archive if auth == author]
            for author in authors}
def average_pages(archive: list) -> float:
    pages = [pages for title, author, year, pages, genre in archive]
    return sum(pages) / len(archive) if pages else 0.0
def count_system_per_member(crew: list, systems: dict) -> dict:
    return {surname: sum(1 for members in systems.values() if surname in members)
            for surname, _, _, _ in crew}
def calculate_bonuses(crew: list) -> dict:
    return {
        surname: BONUS_HIGH_RATE * salary if exp > EXPERIENCE_THRESHOLD else BONUS_LOW_RATE * salary
        for surname, _, exp, salary in crew
            }
def get_small_systems(systems: dict) -> list:
    return [key for key, values in systems.items() if len(values) < WORKERS_THRESHOLD]
def create_crew_profiles(crew: list, systems: dict) -> list:
    systems_count = count_system_per_member(crew, systems)
    bonuses = calculate_bonuses(crew)
    return [{
        "surname": surname,
        "position": position,
        "experience": exp,
        "salary": salary,
        "systems": systems_count[surname],
        "bonus": bonuses[surname]
    } for surname, position, exp, salary in crew]