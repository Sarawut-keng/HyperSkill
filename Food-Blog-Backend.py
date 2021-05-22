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
        return self.ask_for_recipe()

    def ask_for_recipe(self):
        print("Pass the empty recipe name to exit.")
        while True:
            recipe_name = input("Recipe name: ")
            if len(recipe_name) == 0:
                self.conn.close()
                exit()
            recipe_description = input("Recipe description: ")
            self.query.execute(f'INSERT INTO recipes (recipe_name, recipe_description) '
                               f'VALUES ("{recipe_name}", "{recipe_description}")')
            meal_name = self.query.execute(f'SELECT meal_id, meal_name from meals')
            meal_name_ = meal_name.fetchall()
            for i in meal_name_:
                print(f'{i[0]}) {i[1]}')
            recipe_id = self.query.execute(f'SELECT recipe_id from recipes').lastrowid
            served_dishes = input("When the dish can be served: ").split(" ")
            for num in served_dishes:
                self.query.execute(f'INSERT INTO serve (recipe_id, meal_id) VALUES ("{recipe_id}", "{int(num)}")')
            self.conn.commit()


start = FoodBlog()
start.create_table()
