from random import shuffle


class CookBook:
    def __init__(self, dic_cook_book: dict, random_key=False):

        self.index = 0
        self.dic_cook_book = self.__get_unique_ingredients(dic_cook_book, random_key)

    @staticmethod
    def __get_unique_ingredients(dic_cook_book: dict, random_key: bool) -> list:
        unique_ingredients = {}

        for all_ingredients in dic_cook_book["Cook Book"]:
            for key_ingredients in all_ingredients:
                for value_ingredients in all_ingredients[key_ingredients]:
                    if value_ingredients in unique_ingredients:
                        unique_ingredients[f"{value_ingredients}"] += 1
                    else:
                        unique_ingredients[f"{value_ingredients}"] = 1

        if random_key:
            random_list_unique_ingredients = list(unique_ingredients.keys())
            shuffle(random_list_unique_ingredients)
            return random_list_unique_ingredients
        else:
            unique_ingredients = {k: unique_ingredients[k] for k in
                                  sorted(unique_ingredients, key=unique_ingredients.get, reverse=True)}

        return list(unique_ingredients)

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


d = CookBook(item, random_key=True)

print(next(d))
print(next(d))
print(next(d))
print(next(d))

