YEAR_THRESHOLD = 1950
PAGES_THRESHOLD = 300
EXPERIENCE_THRESHOLD = 5
BONUS_HIGH_RATE = 0.15
BONUS_LOW_RATE = 0.1
WORKERS_THRESHOLD = 2

BK_TITLE = 0
BK_AUTHOR = 1
BK_YEAR = 2
BK_PAGES = 3
BK_GENRE = 4

CR_SURNAME = 0
CR_POSITION = 1
CR_EXP = 2
CR_SALARY = 3

def get_old_short_books(archive: list) -> list:
    return [book[BK_TITLE] for book in archive if book[BK_YEAR] < YEAR_THRESHOLD and book[BK_PAGES] < PAGES_THRESHOLD]
def group_by_author(archive: list) -> dict:
    authors = {book[BK_AUTHOR] for  book in archive}
    return {author: [book for book in archive if book[BK_AUTHOR] == author]
            for author in authors}
def average_pages(archive: list) -> float:
    pages = [book[BK_PAGES] for book in archive]
    return sum(pages) / len(archive) if pages else 0.0
def count_system_per_member(crew: list, systems: dict) -> dict:
    return {member[CR_SURNAME]: sum(1 for members in systems.values() if member[CR_SURNAME] in members)
            for member in crew}
def calculate_bonuses(crew: list) -> dict:
    return {
        member[CR_SURNAME]: BONUS_HIGH_RATE * member[CR_SALARY] if member[CR_EXP] > EXPERIENCE_THRESHOLD else BONUS_LOW_RATE * member[CR_SALARY]
        for member in crew
            }
def get_small_systems(systems: dict) -> list:
    return [key for key, values in systems.items() if len(values) < WORKERS_THRESHOLD]
def create_crew_profiles(crew: list, systems: dict) -> list:
    systems_count = count_system_per_member(crew, systems)
    bonuses = calculate_bonuses(crew)
    return [{
        "surname": member[CR_SURNAME],
        "position": member[CR_POSITION],
        "experience": member[CR_EXP],
        "salary": member[CR_SALARY],
        "systems": systems_count[member[CR_SURNAME]],
        "bonus": bonuses[member[CR_SURNAME]]
    } for member in crew]