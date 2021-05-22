import sqlite3


class FoodBlog:

    def __init__(self):
        self.query = None
        self.conn = None

    def create_table(self):
        self.conn = sqlite3.connect('food_blog.db')
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
        return self.add_data()

    def add_data(self):
        data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
                "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
                "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
        for key in data:
            for value in data[key]:
                if key == "measures":
                    self.query.execute(f"INSERT INTO measures(measure_name) VALUES ('{value}')")
                elif key == "meals":
                    self.query.execute(f"INSERT INTO meals(meal_name) VALUES ('{value}')")
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
            for i in meal_name_:
                print(f'{i[0]}) {i[1]}')
            recipe_id = self.query.execute('SELECT recipe_id from recipes').lastrowid
            served_dishes = input("Enter proposed meals separated by a space: ").split(" ")
            for num in served_dishes:
                self.query.execute(f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{int(num)}")')
            self.conn.commit()
            self.ask_for_quantity(recipe_id)

    def ask_for_quantity(self, recipe_id):
        while True:
            quantity_input = input("Input quantity of ingredient <press enter to stop>: ")
            if len(quantity_input) == 0:
                break
            else:
                quantity_input = quantity_input.split(" ")
            if len(quantity_input) == 2:
                ingredient = self.query.execute(f'SELECT ingredient_id FROM ingredients '
                                                f'WHERE ingredient_name = "{quantity_input[1]}"'
                                                f'OR ingredient_name LIKE "%{quantity_input[1]}%"')
                ingredient = ingredient.fetchone()
                measure = self.query.execute(f'SELECT measure_id FROM measures '
                                             f'WHERE mearsure_name = ""')
                measure = measure.fetchone()
                if ingredient is None:
                    print("The measure is not conclusive!")
                else:
                    self.query.execute(f'INSERT INTO quantity (quantity, recipe_id, measure_id, ingredient_id) '
                                       f'VALUES ("{quantity_input[0]}", "{recipe_id}", "{measure[0]}", "{ingredient[0]}")')
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
                    self.query.execute(f'INSERT INTO quantity (quantity, recipe_id, measure_id, ingredient_id) '
                                       f'VALUES ("{quantity_input[0]}", "{recipe_id}", "{measure[0]}", "{ingredient[0]}")')
                    self.conn.commit()


start = FoodBlog()
start.create_table()
