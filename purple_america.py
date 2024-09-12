"""
Module: purple_america

Program for visualizing election results in interesting ways.

Authors:
1) Rodolfo Lopez - rodolfolopez@sandiego.edu
"""

import turtle


def draw_subregion(my_turtle, polygon_points):
    """
    Draws a polygonal subregion.

    Parameters:
    my_turtle (type: Turtle) - The turtle that will do the drawing.
    polygon_points (type: List) - List of tuples of the coordinates of the
      polygonal region.

    Returns:
    None
    """

    my_turtle.penup()

    for x, y in polygon_points:
        my_turtle.goto(x, y)
        my_turtle.pendown()

    x, y = polygon_points[0]
    my_turtle.goto(x, y)


def draw_filled_subregion(my_turtle, polygon_points, style, votes):
    """
    Renders a region, determining the color according to the style and the vote counts for each party.

    Parameters:
    my_turtle (type: Turtle) - The turtle that will do the drawing.
    polygon_points (type: List) - List of tuples of the coordinates of the
      polygonal region.
    style (type: str) - The coloring style to use ('black-white', 'red-blue', or 'purple').
    votes (type: Tuple) - A tuple containing the vote counts for Republican, Democrat, and Other.

    Returns:
    None
    """

    if style == "black-white":
        my_turtle.pencolor("black")
        my_turtle.fillcolor("white")

    elif style == "red-blue":
        my_turtle.pencolor("white")
        if votes[0] > votes[1] and votes[0] > votes[2]:
            my_turtle.fillcolor("red")
        elif votes[1] > votes[0] and votes[1] > votes[2]:
            my_turtle.fillcolor("blue")
        else:
            my_turtle.fillcolor("gray")

    elif style == "purple":
        my_turtle.pencolor("white")
        vote_total = sum(votes)

        if vote_total == 0:
            my_turtle.fillcolor((127, 127, 127))
        else:
            rep = votes[0] / vote_total
            dem = votes[1] / vote_total
            other = votes[2] / vote_total
            my_turtle.fillcolor((rep, other, dem))

    my_turtle.begin_fill()
    draw_subregion(my_turtle, polygon_points)
    my_turtle.end_fill()


def read_subregion(geo_file):
    """
    Retrieves information for one subregion from the provided open file.

    Parameters:
    geo_file (type: file) - An open file object containing geographic data.

    Returns:
    Tuple - A tuple containing:
      - region_name (type: str): The name of the subregion.
      - polygon_points (type: List): List of tuples containing longitude and latitude coordinates.
    """

    geo_file.readline()
    region_name = geo_file.readline().strip()
    geo_file.readline()
    num_points = int(geo_file.readline())

    polygon_points = []
    for _ in range(num_points):
        line = geo_file.readline()
        cols = line.split()
        longitude = float(cols[0])
        latitude = float(cols[1])
        polygon_points.append((longitude, latitude))

    return region_name, polygon_points


def draw_map(geo_filename, vote_results, style):
    """
    Renders the geographic areas using the specified styling.

    Parameters:
    geo_filename (type: str) - The name of the file containing geographic data.
    vote_results (type: Dict) - A dictionary containing vote results for each region.
    style (type: str) - The coloring style to use ('black-white', 'red-blue', or 'purple').

    Returns:
    None
    """

    with open(geo_filename, "r", encoding="utf-8") as f:
        min_line = f.readline()
        cols = min_line.split()
        min_longitude = float(cols[0])
        min_latitude = float(cols[1])

        max_line = f.readline()
        cols = max_line.split()
        max_longitude = float(cols[0])
        max_latitude = float(cols[1])

        num_regions = int(f.readline())

        t = turtle.Turtle()
        t.speed("fastest")
        s = turtle.Screen()

        s.setworldcoordinates(min_longitude, min_latitude, max_longitude, max_latitude)

        s.tracer(0, 0)

        for _ in range(num_regions):
            subregion_name, points = read_subregion(f)
            votes = vote_results.get(
                subregion_name, (0, 0, 0)
            )  # DC has no votes in 1960
            draw_filled_subregion(t, points, style, votes)

        s.update()
        s.exitonclick()


def get_election_results(election_filename):
    """
    Reads election data and stores it in a dictionary.

    Parameters:
    election_filename (type: str) - The name of the file containing election data.

    Returns:
    Dict - A dictionary where keys are region names and values are tuples of vote counts
           (Republican, Democrat, Other).
    """

    vote_results = {}
    with open(election_filename, "r", encoding="utf-8") as f:
        f.readline()

        for line in f:
            cols = line.split(",")
            vote_results[cols[0]] = (int(cols[1]), int(cols[2]), int(cols[3]))

    return vote_results


def main():
    """
    Main function to run the Purple America program.

    Prompts the user for input files and map style, then generates and displays
    the election map based on the provided data.

    Parameters:
    None

    Returns:
    None
    """

    geo_filename = input("Enter the name of the geography file: ")
    election_filename = input("Enter the name of the election data file: ")

    valid_input = False
    while not valid_input:
        prompt_string = "What style of map would you like?\n"
        prompt_string += "Enter 1 for black & white.\n"
        prompt_string += "Enter 2 for red & blue.\n"
        prompt_string += "Enter 3 for purple.\n"
        style_selection = input(prompt_string)
        if style_selection == "1":
            valid_input = True
            style = "black-white"
        elif style_selection == "2":
            valid_input = True
            style = "red-blue"
        elif style_selection == "3":
            valid_input = True
            style = "purple"
        else:
            print("Invalid selection!")

    vote_results = get_election_results(election_filename)
    draw_map(geo_filename, vote_results, style)


# WARNING: Do NOT modify anything below this point.

if __name__ == "__main__":
    main()
