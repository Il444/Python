YEAR_THRESHOLD = 1950
PAGES_THRESHOLD = 300
EXPERIENCE_THRESHOLD = 5
BONUS_HIGH_RATE = 0.15
BONUS_LOW_RATE = 0.1
WORKERS_THRESHOLD = 2

def get_old_short_books(archive: list) -> list:
    result = []
    for title, _, year, pages, _ in archive:
        if year < YEAR_THRESHOLD and pages < PAGES_THRESHOLD:
            result.append(title)
    return result
def group_by_author(archive: list) -> dict:
    result = {}
    for  title, auth, year, pages, genre in archive:
        author = auth
        if author not in result:
            result[author] = []
        result[author].append((title, author, year, pages, genre))
    return result
def average_pages(archive: list) -> float:
    if len(archive) == 0:
        return 0.0
    count = 0
    for title, author, year, pages, genre in archive:
        count += pages
    result = count / len(archive)
    return result
def count_system_per_member(crew: list, systems: dict) -> dict:
    result = {}
    for surname, position, exp, salary in crew:
        result[surname] = 0
    for system, members in systems.items():
        for member in members:
            if member in result:
                result[member] += 1
    return result
def calculate_bonuses(crew: list) -> dict:
    result = {}
    for surname, position, exp, salary in crew:
        if exp > EXPERIENCE_THRESHOLD:
            bonus = BONUS_HIGH_RATE * salary
        else:
            bonus = BONUS_LOW_RATE * salary
        result[surname] = bonus
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
    for surname, position, exp, salary in crew:
        result.append({
            "surname": surname,
            "position": position,
            "experience": exp,
            "salary": salary,
            "systems": system_count[surname],
            "bonus": bonuses[surname]
        })
    return result