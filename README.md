# Zootopia

This Python project allows users to search for animals and generate a simple HTML webpage displaying their details. The program fetches data from the API Ninjas Animals API
 and provides filtering options based on skin type. The generated webpage shows key characteristics of each animal in a structured and readable format.

## Features

- Search for animals: Prompt the user to enter an animal name.
- Filter by skin type: After fetching results, users can select a skin type to filter displayed animals.
- Render HTML page: Displays the following information for each animal:
  - Name
  - Scientific name
  - Diet
  - Location
  - Type
- Error handling: If the searched animal does not exist or the API returns no results, a clear error message is displayed on the webpage.
## Installation

To install this project, simply clone the repository and install the dependencies in requirements.txt using `pip`

## Usage

1. To use this project, run the following command - `python animals_web_generator.py`.
2. Enter the animal name when prompted.
3. If multiple results are returned, select a skin type from the list to filter animals.
4. The program generates an HTML file named animals.html in the current directory.
5. Open animals.html in a browser to view the results.
