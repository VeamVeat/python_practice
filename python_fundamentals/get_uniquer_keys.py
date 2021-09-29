
def get_unique_ingredients(cook_book: dict) -> dict:
    unique_ingredients = {}

    for all_ingredients in cook_book["Cook Book"]:
        for key_ingredients in all_ingredients:
            for value_ingredients in all_ingredients[key_ingredients]:
                if value_ingredients in unique_ingredients:
                    unique_ingredients[f"{value_ingredients}"] += 1
                else:
                    unique_ingredients[f"{value_ingredients}"] = 1
    unique_ingredients = {k: unique_ingredients[k] for k in sorted(unique_ingredients, key=unique_ingredients.get,
                                                                   reverse=True)}
    return list(unique_ingredients)


class CookBook:
    def __init__(self, dic_cook_book):
        self.dic_cook_book = get_unique_ingredients(dic_cook_book)
        self.index = 0

    def __next__(self):
        if self.index <= len(self.dic_cook_book) - 1:
            i = self.index
            self.index += 1
            return self.dic_cook_book[i]
        else:
            raise StopIteration

    def __iter__(self):
        return self


item = {"Cook Book": [
        {"Dish A": ["oil", "bacon", "oil"]},
        {"Dish B": ["eggs", "oil", "eggs"]}
     ]}

d = CookBook(item)
print(next(d))
print(next(d))
print(next(d))
print(next(d))