import random

def battle_simulation(clones: int, droids: int, droid_attack_power: int = 5, hit_threshold: int = 35, verbose: bool = True) -> tuple[int, int, int]:
    clone_remains = clones
    droid_remains = droids
    rounds = 0
    while clone_remains != 0 and droid_remains != 0:
        rounds += 1
        clones_killed = droid_remains // droid_attack_power
        clone_remains = max(0, clone_remains - clones_killed)

        for _ in range(clone_remains):
            if droid_remains == 0:
                break
            chance = random.randint(0, 99)
            if chance < hit_threshold:
                droid_remains -= 1
        if verbose:
            print(f"Round {rounds}: the amount of clones - {clone_remains}, droids - {droid_remains}")

    if verbose:
        if droid_remains == 0 and clone_remains != 0:
            print(f"The forces of Galactic Republic won! The amount of clones - {clone_remains}")
        elif clone_remains == 0 and droid_remains != 0:
            print(f"The forces of Trade Federation won! The amount of droids - {droid_remains}")
        else:
            print(f"Draw! Everyone died in the field of battle")

    return rounds, clone_remains, droid_remains

def run_series(clones: int, droids:int, n: int = 1000, droid_attack_power: int = 5, hit_threshold: int = 30) -> tuple[float, float, float, float]:
    rounds = 0
    clone_wins = 0
    droid_wins = 0
    amount_of_survivors = 0
    for _ in range(n):
        round, clone_remains, droid_remains = battle_simulation(clones, droids, droid_attack_power, hit_threshold, False)
        rounds += round
        if clone_remains != 0 and droid_remains == 0:
            amount_of_survivors += clone_remains
            clone_wins += 1
        elif droid_remains != 0 and clone_remains == 0:
            amount_of_survivors += droid_remains
            droid_wins += 1

    clone_wins = clone_wins / n * 100
    droid_wins = droid_wins / n * 100
    rounds = rounds / n
    amount_of_survivors = amount_of_survivors / n
    print(f"{"Side":<10} | {"Win Share":>12} | {"Avg rounds":>12} | {"Avg survivors":>14}"
          f"\n{"-" * 57}"
          f"\n{"Clones":<10} | {clone_wins:>11.2f}% | {"":>12} |"
          f"\n{"Droids":<10} | {droid_wins:>11.2f}% | {"":>12} |"
          f"\n{"-" * 57}"
          f"\n{"Overall":<10} | {"":>12} | {rounds:>12} | {amount_of_survivors:>14.2f}")
    return clone_wins, droid_wins, rounds, amount_of_survivors

def main():
    print("Battle 1: ")
    battle_simulation(50, 10)
    print("Battle 2: ")
    battle_simulation(1, 100)
    print("Battle 3: ")
    battle_simulation(1390, 2200, 1000, 12, 24)

    print("Play Game")
    run_series(1390, 2200, 1000, 12, 34)


if __name__ == "__main__":
    random.seed(64)
    main()