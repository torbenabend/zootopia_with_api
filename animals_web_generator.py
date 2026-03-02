import json


ANIMAL_CHARACTERISTICS = {
    "Name": lambda d: d.get("name"),
    "Scientific name": lambda d: d.get("taxonomy", {}).get("scientific_name"),
    "Diet": lambda d: d.get("characteristics", {}).get("diet"),
    "Location": lambda d: (
        ", ".join(d.get("locations")) if d.get("locations") else None
    ),
    "Type": lambda d: d.get("characteristics", {}).get("type"),
    "Skin type": lambda d: d.get("characteristics", {}).get("skin_type")
}


def load_data(file_path):
    """ Load a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_html_template(file_path):
    """ Load an HTML template """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def create_webpage(html_input):
    """ Create html file for webpage """
    with open("animals.html", "w", encoding="utf-8") as html:
        html.write(html_input)


def render_animal_name(animal_info):
    """ Render HTML syntax of animal name"""
    rendered_name = ""
    animal_name = ANIMAL_CHARACTERISTICS["Name"](animal_info)
    if animal_name is not None:
        rendered_name += '<div class="card__title">'
        rendered_name += f'{animal_name}'
        rendered_name += '</div>'
    return rendered_name


def render_animal_characteristic(characteristic, animal_info):
    """ Render HTML syntax of animal characteristics"""
    rendered_characteristic = ""
    animal_characteristic = ANIMAL_CHARACTERISTICS[characteristic](animal_info)
    if animal_characteristic is not None:
        rendered_characteristic += (f'<li style="list-style-type: disc"><strong>{characteristic.capitalize()}'
                                    f':</strong> ')
        rendered_characteristic += f'{animal_characteristic}</li>'
    return rendered_characteristic


def render_animal_html(animals):
    """ Render animal information in HTML syntax for each animal """
    animals_html = ""
    for animal in animals:
        animals_html += '<li class="cards__item">'
        animals_html += render_animal_name(animal)
        animals_html += '<div class="card__text">'
        animals_html += '<ul>'
        animals_html += render_animal_characteristic("Scientific name", animal)
        animals_html += render_animal_characteristic("Diet", animal)
        animals_html += render_animal_characteristic("Location", animal)
        animals_html += render_animal_characteristic("Type", animal)
        animals_html += '</ul>'
        animals_html += '</div>'
        animals_html += "</li>"
    return animals_html


def get_skin_types(animals):
    """ Get every possible skin type"""
    skin_types = set()
    for animal in animals:
        skin_type = ANIMAL_CHARACTERISTICS["Skin type"](animal)
        if skin_type:
            skin_types.add(skin_type)
    return skin_types


def user_selection_skin_type(skin_types):
    """ Prompt the user to select a skin type """
    while True:
        print("Skin types:")
        for skin_type in skin_types:
            print(f"- {skin_type}")
        user_skin_type = input("\nPlease enter a skin type: ")
        if user_skin_type in skin_types:
            return user_skin_type
        print("Invalid input! Please try again.\n")


def main():
    # LOAD DATA
    animals_data = load_data("animals_data.json")
    template_data = load_html_template("animals_template.html")
    # FILTER BY SKIN TYPE
    skin_types = get_skin_types(animals_data)
    user_skin_type = user_selection_skin_type(skin_types)
    animals_data_filtered = [
        animal for animal in animals_data
        if ANIMAL_CHARACTERISTICS["Skin type"](animal) == user_skin_type
    ]
    # CREATE WEBPAGE
    animals_html = render_animal_html(animals_data_filtered)
    animals_webpage = template_data.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )
    create_webpage(animals_webpage)


if __name__ == "__main__":
    main()
