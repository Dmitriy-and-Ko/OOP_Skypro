def test_category_init(first_category, second_category):
    assert first_category.name == "автомобили"
    assert (
        first_category.description
        == """Самодвижущееся транспортное средство с двигателем для перевозки грузов и пассажиров
         по безрельсовым путям"""
    )
    assert first_category.products == ["Hyundai i20", "Lada Vesta", "Daewoo Matiz"]
    assert len(first_category.products) == 3

    assert second_category.name == "стрелковое оружие"
    assert (
        second_category.description
        == """орудия (изделия), для стрельбы, изготовленные человеком для добычи зверя, развлечения (спорт),
         борьбы со своим противником или иного."""
    )
    assert len(second_category.products) == 3

    assert first_category.category_quantity == 2
    assert second_category.category_quantity == 2

    assert first_category.products_quantity == 6
    assert second_category.products_quantity == 6
