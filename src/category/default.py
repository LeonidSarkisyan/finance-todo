from dataclasses import dataclass, asdict


@dataclass
class SubCategory:
    title: str


@dataclass
class Category:
    title: str
    sub_categories: list[SubCategory]


def make_category(category_title: str, *args: str):
    category = Category(
        title=category_title, sub_categories=[SubCategory(arg) for arg in args]
    )
    return category


DEFAULT_CATEGORIES = [
    make_category("Еда", "Продукты", "Ресторан, фаст-фуд", "Кафе, бар"),
    make_category("Транспорт", "Дальние поездки", "Деловые поездки", "Общественный транспорт", "Такси"),
    make_category(
        "Покупки", "Аптека", "Дети", "Дом и сад", "Домашние животные", "Красота и здоровье", "Одежда и обувь",
        "Отдых", "Подарки", "Электроника", "Ювелирные изделия"
    ),
    make_category("Здоровье", "Клиника", "Операции"),
    make_category("Личные"),
]
