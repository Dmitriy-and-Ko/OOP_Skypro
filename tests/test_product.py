
def test_product_init(first_product):
    assert first_product.name == 'hyundai i20'
    assert first_product.description == 'Cубкомпактный хетчбэк, выпускающийся с 2008 года. В большинстве стран Hyundai i20 пришёл на смену модели Getz'
    assert first_product.price == 1700000
    assert first_product.quantity == 5