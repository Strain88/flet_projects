class Model:
    products: dict = {
        0: {
            "id": "111",
            "img_src": "/assets/phone1.jpg",
            "name": "Product 1",
            "description": "Experience the excellence of Product 1, a cutting-edge creation designed to elevate your daily routine. Crafted with precision and innovation, this product offers unmatched quality and performance. Enhance your lifestyle with Product 1 today.",
            "price": "$21.55",
        },
        1: {
            "id": "222",
            "img_src": "/assets/phone2.jpg",
            "name": "Product 2",
            "description": "Immerse yourself in the sophistication of Product 2. Uniquely crafted to meet your needs, this product combines style and functionality seamlessly. Elevate your daily experiences with the exceptional features of Product 2.",
            "price": "$32.99",
        },
        2: {
            "id": "333",
            "img_src": "/assets/phone3.jpg",
            "name": "Product 3",
            "description": "Discover the versatility of Product 3, a dynamic solution designed for modern living. Whether it's convenience, durability, or style you seek, Product 3 delivers on all fronts. Make a statement with this exceptional product",
            "price": "$45.75",
        },
    }

    cart: dict = {}

    @staticmethod
    def get_products():
        return Model.products

    @staticmethod
    def get_cart():
        return Model.cart

    @staticmethod
    def add_item_to_cart(data: str):
        for _, values in Model.products.items():
            for key, value in values.items():
                if value == data:
                    if not Model.cart.get(value):
                        Model.cart[value] = {"quantity": 1, **values}

                    else:
                        Model.cart[value]["quantity"] += 1
