"""
SP-P01: Варіант 15
Задача 05: Оточення дочірнього процесу (додавання і видалення)
"""
import os
import subprocess

VARIANT = 15


def child_env_lines(
    prefix: str,
    set_vars: dict[str, str],
    unset_vars: list[str]
) -> list[str]:
    """
    Запускає /usr/bin/env у дочірньому процесі з модифікованим оточенням.
    Не змінює оточення батьківського процесу os.environ.
    """
    # 1. Створюємо копію поточного оточення
    child_env = os.environ.copy()

    # 2. Видаляємо змінні зі списку unset_vars (ігноруючи відсутні)
    for key in unset_vars:
        child_env.pop(key, None)

    # 3. Додаємо або перезаписуємо пари зі словника set_vars
    for key, val in set_vars.items():
        child_env[key] = str(val)

    # 4. Запускаємо /usr/bin/env у дочірньому процесі з ізольованим child_env
    res = subprocess.run(
        ["/usr/bin/env"],
        env=child_env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True
    )

    # 5. Фільтруємо рядки за prefix та сортуємо за алфавітом
    lines = [
        line for line in res.stdout.splitlines()
        if line.startswith(prefix)
    ]
    lines.sort()

    return lines


if __name__ == "__main__":
    print(f"Запустіть тести: pytest --variant {VARIANT}")