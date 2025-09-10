import secrets


def roll_dice() -> int:
    return secrets.randbelow(6) + 1


def main() -> None:
    return None


if __name__ == '__main__':
    main()
