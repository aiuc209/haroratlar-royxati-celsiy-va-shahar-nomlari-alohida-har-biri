import pytest

def create_city_temperature_strings(city_names, temperatures):
    return [f"{city}: {temp}°C" for city, temp in zip(city_names, temperatures)]

def test_create_city_temperature_strings():
    city_names = ["Toshkent", "Samarqand", "Buxoro"]
    temperatures = [25, 30, 28]
    expected_result = ["Toshkent: 25°C", "Samarqand: 30°C", "Buxoro: 28°C"]
    assert create_city_temperature_strings(city_names, temperatures) == expected_result

def test_create_city_temperature_strings_empty_lists():
    city_names = []
    temperatures = []
    expected_result = []
    assert create_city_temperature_strings(city_names, temperatures) == expected_result

def test_create_city_temperature_strings_unequal_list_lengths():
    city_names = ["Toshkent", "Samarqand"]
    temperatures = [25, 30, 28]
    with pytest.raises(ValueError):
        create_city_temperature_strings(city_names, temperatures)
