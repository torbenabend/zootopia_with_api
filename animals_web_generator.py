import data_fetcher

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


def get_animal_name_from_user():
    """ Prompt user to insert an animal name """
    return input("Enter a name of an animal: ").lower()


def load_html_template(file_path):
    """ Load an HTML template """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def create_webpage(html_template, html_data):
    """ Create html file for webpage """
    animals_webpage = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", html_data
    )
    with open("animals.html", "w", encoding="utf-8") as html:
        html.write(animals_webpage)


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
    html_parts = []
    for animal in animals:
        card_html_parts = [
                '<li class="cards__item">',
                render_animal_name(animal),
                '<div class="card__text">',
                '<ul>',
                render_animal_characteristic("Scientific name", animal),
                render_animal_characteristic("Diet", animal),
                render_animal_characteristic("Location", animal),
                render_animal_characteristic("Type", animal),
                '</ul>',
                '</div>',
                '</li>'
        ]
        for command in card_html_parts:
            html_parts.append(command)
    animal_html = "".join(html_parts)

    return animal_html


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


def filter_by_skin_type(animals_data):
    skin_types = get_skin_types(animals_data)
    user_skin_type = user_selection_skin_type(skin_types)
    animals_data_filtered = [
        animal for animal in animals_data
        if ANIMAL_CHARACTERISTICS["Skin type"](animal) == user_skin_type
    ]
    return animals_data_filtered


def render_error_html(animal_name):
    return f"<h2>The animal {animal_name} doesn't exist.</h2>"


def main():
    # LOAD DATA
    animal_name = get_animal_name_from_user()
    animals_data = data_fetcher.fetch_data(animal_name)
    template_data = load_html_template("animals_template.html")
    if animals_data:
        # FILTER BY SKIN TYPE
        animals_data_filtered = filter_by_skin_type(animals_data)
        animals_html = render_animal_html(animals_data_filtered)
    else:
        animals_html = render_error_html(animal_name)
    # CREATE WEBPAGE
    create_webpage(template_data, animals_html)


if __name__ == "__main__":
    main()
