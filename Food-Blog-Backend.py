import sqlite3


class FoodBlog:

    def __int__(self):
        self.conn = None
        self.query = None

    def create_table(self):
        self.conn = sqlite3.connect('food_blog.db')
        self.query = self.conn.cursor()
        self.query.execute('CREATE TABLE meals (meal_id INTEGER PRIMARY KEY, meal_name VARCHAR NOT NULL UNIQUE)')
        self.query.execute('CREATE TABLE ingredients (ingredient_id INTEGER PRIMARY KEY, ingredient_name VARCHAR NOT NULL UNIQUE)')
        self.query.execute('CREATE TABLE measures (measure_id INTEGER PRIMARY KEY, measure_name VARCHAR UNIQUE)')
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


start = FoodBlog()
start.create_table()
