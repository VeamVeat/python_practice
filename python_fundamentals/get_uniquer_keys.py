from collections import Counter


class CookBook:
    def __iter__(self):
        return self

    def __init__(self, cook_book: dict, sort=False):
        self.cook_book = cook_book
        self.sort = sort
        self.unique_ingredients = self.__get_unique_ingredients()
        self.item = 0
        self.count_elements_unique_ingredients = len(self.unique_ingredients)

    def __get_unique_ingredients(self):
        ingredients = []
        for dish in self.cook_book['Cook Book']:
            ingredients.extend(*dish.values())
        if not self.sort:
            return list(set(ingredients))
        else:
            counter_ingredient = Counter(ingredients)
            return [key for key, _ in counter_ingredient.most_common()]

    def __next__(self):
        if self.item == self.count_elements_unique_ingredients:
            raise StopIteration
        else:
            unique_ingredient = self.unique_ingredients[self.item]
            self.item += 1
            return unique_ingredient


book = {"Cook Book": [
        {"Dish A": ["oil", "bacon", "oil"]},
        {"Dish B": ["eggs", "oil", "eggs"]}
     ]}


book_ingredients = CookBook(book, sort=True)
for ingredient in book_ingredients:
    print(ingredient)

