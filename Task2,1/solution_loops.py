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
    result = []
    for book in archive:
        if book[BK_YEAR] < YEAR_THRESHOLD and book[BK_PAGES] < PAGES_THRESHOLD:
            result.append(book[BK_TITLE])
    return result
def group_by_author(archive: list) -> dict:
    result = {}
    for  book in archive:
        if book[BK_AUTHOR] not in result:
            result[book[BK_AUTHOR]] = []
        result[book[BK_AUTHOR]].append((book[BK_TITLE], book[BK_AUTHOR], book[BK_YEAR], book[BK_PAGES], book[BK_GENRE]))
    return result
def average_pages(archive: list) -> float:
    if len(archive) == 0:
        return 0.0
    count = 0
    for book in archive:
        count += book[BK_PAGES]
    result = count / len(archive)
    return result
def count_system_per_member(crew: list, systems: dict) -> dict:
    result = {}
    for member in crew:
        result[member[CR_SURNAME]] = 0
    for system, members in systems.items():
        for member in members:
            if member in result:
                result[member] += 1
    return result
def calculate_bonuses(crew: list) -> dict:
    result = {}
    for member in crew:
        if member[CR_EXP] > EXPERIENCE_THRESHOLD:
            bonus = BONUS_HIGH_RATE * member[CR_SALARY]
        else:
            bonus = BONUS_LOW_RATE * member[CR_SALARY]
        result[member[CR_SURNAME]] = bonus
    return result
def get_small_systems(systems: dict) -> list:
    result = []
    for key, values in systems.items():
        if len(values) < WORKERS_THRESHOLD:
            result.append(key)
    return result
def create_crew_profiles(crew: list, systems: dict) -> list:
    result = []
    system_count = count_system_per_member(crew, systems)
    bonuses = calculate_bonuses(crew)
    for member in crew:
        result.append({
            "surname": member[CR_SURNAME],
            "position": member[CR_POSITION],
            "experience": member[CR_EXP],
            "salary": member[CR_SALARY],
            "systems": system_count[member[CR_SURNAME]],
            "bonus": bonuses[member[CR_SURNAME]]
        })
    return result