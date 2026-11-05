from math import log10
from enum import Enum


class Choice(Enum):
    WATTS_TO_DBM = 1
    DBM_TO_WATTS = 2
    VOLTS_TO_DBV = 3
    DBV_TO_VOLTS = 4
    EXIT = 5


def conversion_vats_into_dbm(p: float) -> float:
    power_dbm = 10 * log10(p * 1000)
    return power_dbm


def conversion_dbm_into_vats(p: float) -> float:
    power_vats = (10 ** (p / 10)) / 1000
    return power_vats


def conversion_volts_into_dbv(u: float) -> float:
    voltage_dbv = 20 * log10(u)
    return voltage_dbv


def conversion_dbv_into_volts(u: float) -> float:
    voltage_volts = 10 ** (u / 20)
    return voltage_volts


def get_choice() -> Choice:
    prompt = int(input("What path would you like to go:\n"
                       "1. Conversion vats into Dbm\n"
                       "2. Conversion DBm into vats\n"
                       "3. Conversion volts into DBv\n"
                       "4. Conversion DBv into volts\n"
                       "5. Exit\n"))
    return Choice(prompt)


def get_range(choice: Choice) -> tuple[float, float, float]:
    while True:
        if choice == Choice.WATTS_TO_DBM or choice == Choice.DBM_TO_WATTS:
            try:
                start_pos = float(input("Write power range you like to conversion:\n"
                                        "From: "))
                if start_pos < 0 and choice != Choice.DBM_TO_WATTS:
                    print("Your numbers cannot be less than zero!")
                    continue
                end_pos = float(input("To: "))
                if end_pos < 0 and choice != Choice.DBM_TO_WATTS:
                    print("Your numbers cannot be less than zero!")
                    continue
                elif end_pos <= start_pos:
                    print("End point must be greater than start!")
                    continue
                step = float(input("Step: "))
                if step <= 0:
                    print("Step must be positive!")
                    continue
            except ValueError:
                print("Write correct number")
                continue
            break
        elif choice == Choice.VOLTS_TO_DBV or choice == Choice.DBV_TO_VOLTS:
            try:
                start_pos = float(input("Write voltage range you like to conversion:\n"
                                        "From: "))
                if start_pos < 0 and choice != Choice.VOLTS_TO_DBV:
                    print("Your numbers cannot be less than zero!")
                    continue
                end_pos = float(input("To: "))
                if end_pos < 0 and choice != Choice.VOLTS_TO_DBV:
                    print("Your numbers cannot be less than zero!")
                    continue
                elif end_pos <= start_pos:
                    print("End point must be greater than start!")
                    continue
                step = float(input("Step: "))
                if step <= 0:
                    print("Step must be positive!")
                    continue
            except ValueError:
                print("Write correct number")
                continue
            break
    return start_pos, end_pos, step


def get_titles_from_choice(choice: Choice) -> tuple[str, str]:
    if choice == Choice.WATTS_TO_DBM:
        return "P_vat", "P_dbm"
    elif choice == Choice.DBM_TO_WATTS:
        return "P_dbm", "P_vat"
    elif choice == Choice.VOLTS_TO_DBV:
        return "U_volt", "U_dbv"
    elif choice == Choice.DBV_TO_VOLTS:
        return "U_dbv", "U_volt"
    return "", ""


def print_table(data1: list[float], data2: list[float], choice: Choice) -> None:
    title1, title2 = get_titles_from_choice(choice)
    print(f"{title1:<10} | {title2:>10}")
    print("-" * 23)
    for i, j in zip(data1, data2):
        print(f"{i:<10.4g} | {j:>10.4g}")
    print()


def main():
    print("Welcome to conversion program!")
    while True:
        try:
            choice = get_choice()
        except (ValueError, KeyError):
            print("Write number from 1 to 5")
            continue

        if choice == Choice.EXIT:
            break
        elif choice == Choice.WATTS_TO_DBM or choice == Choice.DBM_TO_WATTS:
            start_pos, end_pos, step = get_range(choice)
            input_list = [start_pos + i * step for i in range(int((end_pos - start_pos) / step) + 1) if
                          (start_pos + i * step) <= end_pos]

            if choice == Choice.WATTS_TO_DBM:
                data = [conversion_vats_into_dbm(p) for p in input_list]
            elif choice == Choice.DBM_TO_WATTS:
                data = [conversion_dbm_into_vats(p) for p in input_list]

            print_table(input_list, data, choice)

        elif choice == Choice.VOLTS_TO_DBV or choice == Choice.DBV_TO_VOLTS:
            start_pos, end_pos, step = get_range(choice)
            input_list = [start_pos + i * step for i in range(int((end_pos - start_pos) / step) + 1) if
                          (start_pos + i * step) <= end_pos]

            if choice == Choice.VOLTS_TO_DBV:
                data = [conversion_volts_into_dbv(p) for p in input_list]
            elif choice == Choice.DBV_TO_VOLTS:
                data = [conversion_dbv_into_volts(p) for p in input_list]

            print_table(input_list, data, choice)


if __name__ == "__main__":
    main()
