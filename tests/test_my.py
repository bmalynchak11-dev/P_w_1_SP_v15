import pytest
from conftest import load

# Завантажуємо функцію 5-ї задачі
child_env_lines = load(5).child_env_lines


@pytest.mark.parametrize("prefix, set_vars, unset_vars, expected", [
    # Граничний випадок 1: Одне й те саме ім'я є і в unset, і в set (має діяти set_vars)
    (
        "MY_TEST_",
        {"MY_TEST_KEY": "new_value"},
        ["MY_TEST_KEY"],
        ["MY_TEST_KEY=new_value"]
    ),
    # Граничний випадок 2: Значення зі спеціальними символами (лапки, пробіли, долар)
    (
        "SPECIAL_",
        {"SPECIAL_V": "hello $USER 'world'"},
        [],
        ["SPECIAL_V=hello $USER 'world'"]
    ),
    # Граничний випадок 3: Порожнє значення змінної оточення (повинно виводитися як KEY=)
    (
        "EMPTY_",
        {"EMPTY_VAR": ""},
        [],
        ["EMPTY_VAR="]
    ),
    # Граничний випадок 4: Видалення неіснуючих змінних і порожній результат фільтрації
    (
        "NONEXISTENT_PREFIX_",
        {},
        ["DEFINITELY_NOT_EXISTING_XYZ"],
        []
    ),
])
def test_my_edge_cases(prefix, set_vars, unset_vars, expected):
    result = child_env_lines(prefix, set_vars, unset_vars)
    assert result == expected