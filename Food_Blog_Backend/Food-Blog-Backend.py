import sqlite3
import argparse


class FoodBlog:

    def __init__(self):
        self.conn = None
        self.query = None

    def create_table(self, data):
        self.conn = sqlite3.connect(data)
        self.query = self.conn.cursor()
        self.query.execute('CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY, '
                           'meal_name VARCHAR NOT NULL UNIQUE)')
        self.query.execute('CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY, '
                           'ingredient_name VARCHAR NOT NULL UNIQUE)')
        self.query.execute('CREATE TABLE IF NOT EXISTS measures (measure_id INTEGER PRIMARY KEY, '
                           'measure_name VARCHAR UNIQUE)')
        self.query.execute('CREATE TABLE IF NOT EXISTS recipes (recipe_id INTEGER PRIMARY KEY, '
                           'recipe_name VARCHAR NOT NULL, recipe_description VARCHAR)')
        self.query.execute('PRAGMA foreign_keys = ON')
        self.query.execute('CREATE TABLE IF NOT EXISTS serve (serve_id INTEGER PRIMARY KEY, '
                           'recipe_id INTEGER NOT NULL, meal_id INTEGER NOT NULL, '
                           'FOREIGN KEY (meal_id) REFERENCES meals(meal_id), '
                           'FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id))')
        self.query.execute('CREATE TABLE IF NOT EXISTS quantity (quantity_id INTEGER PRIMARY KEY, '
                           'quantity INTEGER NOT NULL, recipe_id INTEGER NOT NULL, '
                           'measure_id INTEGER NOT NULL, ingredient_id INTEGER NOT NULL, '
                           'FOREIGN KEY (measure_id) REFERENCES measures(measure_id), '
                           'FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id), '
                           'FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id))')
        self.conn.commit()
        self.add_data()

    def parser_method(self, data, me, ing):
        self.conn = sqlite3.connect(data)
        self.query = self.conn.cursor()
        recipe_names = self.query.execute(f"select recipe_id, recipe_name from recipes where recipe_id in  "
                                          f"(select recipe_id from serve where meal_id in "
                                          f"(select meal_id from meals where meal_name in ({me})) "
                                          f"INTERSECT "
                                          f"select recipe_id from quantity as quantity_ where ingredient_id in"
                                          f"(select ingredient_id from ingredients where "
                                          f"ingredient_name in ({ing}))) ORDER BY recipe_name")
        recipe_names = recipe_names.fetchall()
        _name = self.query.execute(f"select ingredient_name from ingredients")
        _name = _name.fetchall()
        list_of_names = [value[0] for value in _name]
        for x in ing.replace("'", "").replace(" ", "").split(","):
            if x in list_of_names:
                pass
            else:
                print("There are no such recipes in the database.")
                exit()
        if recipe_names is None:
            print("There are no such recipes in the database.")
            exit()
        else:
            for value in recipe_names:
                check = self.query.execute(f"select ingredient_id from quantity where recipe_id ={value[0]}")
                check = check.fetchall()
                check_ = self.query.execute(f"select ingredient_id from ingredients where ingredient_name in ({ing})")
                check_ = check_.fetchall()
                if len(ing.split(",")) != len(set(check) & set(check_)):
                    recipe_names.remove(value)
            name = ""
            for value in recipe_names:
                name += value[1] + ", "
            print("Recipes selected for you: " + name[:-2])
            exit()

    def add_data(self):
        data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
                "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
                "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
        for key in data:
            for value in data[key]:
                if key == "measures":
                    self.query.execute(f"INSERT INTO measures (measure_name) VALUES ('{value}')")
                elif key == "meals":
                    self.query.execute(f"INSERT INTO meals (meal_name) VALUES ('{value}')")
                elif key == "ingredients":
                    self.query.execute(f"INSERT INTO ingredients(ingredient_name) VALUES ('{value}')")
        self.conn.commit()
        print("Pass the empty recipe name to exit.")
        return self.ask_for_recipe()

    def ask_for_recipe(self):
        while True:
            recipe_name = input("Recipe name: ")
            if len(recipe_name) == 0:
                self.conn.close()
                exit()
            recipe_description = input("Recipe description: ")
            self.query.execute(f'INSERT INTO recipes (recipe_name, recipe_description) '
                               f'VALUES ("{recipe_name}", "{recipe_description}")')
            meal_name = self.query.execute('SELECT meal_id, meal_name from meals')
            meal_name_ = meal_name.fetchall()
            meal_str = ""
            for i in meal_name_:
                meal_str += str(i[0]) + ") " + str(i[1]) + "  "
            print(meal_str[:-2])
            recipe_id = self.query.execute('SELECT recipe_id from recipes').lastrowid
            served_dishes = input("Enter proposed meals separated by a space: ").split(" ")
            for num in served_dishes:
                self.query.execute(f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{int(num)}")')
            self.conn.commit()
            self.ask_for_quantity(recipe_id)

    def ask_for_quantity(self, recipe_id):
        while True:
            quantity_input = input("Input quantity of ingredient <press enter to stop>: ")
            if len(quantity_input) == 0 or len(quantity_input) == 1:
                break
            else:
                quantity_input = quantity_input.split(" ")
            if len(quantity_input) == 2:
                ingredient = self.query.execute(f'SELECT ingredient_id FROM ingredients '
                                                f'WHERE ingredient_name = "{quantity_input[1]}"'
                                                f'OR ingredient_name LIKE "%{quantity_input[1]}%"')
                ingredient = ingredient.fetchone()
                measure = self.query.execute(f'SELECT measure_id FROM measures '
                                             f'WHERE measure_name = ""')
                measure = measure.fetchone()
                if ingredient is None:
                    print("The measure is not conclusive!")
                else:
                    self.query.execute(f'INSERT INTO quantity '
                                       f'(quantity, recipe_id, measure_id, ingredient_id) '
                                       f'VALUES '
                                       f'("{quantity_input[0]}", "{recipe_id}", "{measure[0]}", "{ingredient[0]}")')
                    self.conn.commit()
            if len(quantity_input) == 3:
                ingredient = self.query.execute(f'SELECT ingredient_id FROM ingredients '
                                                f'WHERE ingredient_name = "{quantity_input[2]}"'
                                                f'OR ingredient_name LIKE "%{quantity_input[2]}%"')
                ingredient = ingredient.fetchone()
                measure = self.query.execute(f'SELECT measure_id FROM measures '
                                             f'WHERE measure_name = "{quantity_input[1]}"')
                measure = measure.fetchone()
                if ingredient is None or measure is None:
                    print("The measure is not conclusive!")
                else:
                    self.query.execute(f'INSERT INTO quantity '
                                       f'(quantity, recipe_id, measure_id, ingredient_id) '
                                       f'VALUES '
                                       f'("{quantity_input[0]}", "{recipe_id}", "{measure[0]}", "{ingredient[0]}")')
                    self.conn.commit()


if __name__ == '__main__':
    start = FoodBlog()
    parser = argparse.ArgumentParser()
    parser.add_argument("food_blog")
    parser.add_argument("--ingredients")
    parser.add_argument("--meals")
    args = parser.parse_args()
    if args.meals is None:
        start.create_table(args.food_blog)
    else:
        if "," not in args.meals:
            the_meal = "'" + args.meals + "'"
        else:
            the_meal = "'" + args.meals.replace(" ", "").replace(",", "', '") + "'"
        if "," not in args.ingredients:
            the_ingredient = "'" + args.ingredients + "'"
        else:
            the_ingredient = "'" + args.ingredients.replace(" ", "").replace(",", "', '") + "'"
        start.parser_method(args.food_blog, the_meal, the_ingredient)
