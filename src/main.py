from App import App
from utils.absoulte_path import get_absoulte_path
from utils.find import find
import json


if __name__ == "__main__":
    f = open(get_absoulte_path(__file__, "../themes.json"), "r")

    themes = json.load(f)

    f.close()

    theme = find(themes, "name", "light")

    app = App(theme)
    app.run()
