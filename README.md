# Purple America Election Visualization

This program visualizes U.S. election results using different coloring styles, including a "purple" style that blends red and blue based on vote proportions.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Features

- Reads geographic data and election results from files
- Supports three visualization styles:
  1. Black and white
  2. Red and blue
  3. Purple (blended colors)
- Uses Python's turtle graphics for rendering

## Dependencies

- Python 3.x
- turtle (standard library)

## Usage

1. Ensure you have Python installed on your system.
2. Run the program:
   ```
   python purple_america.py
   ```
3. When prompted, enter:
   - The name of the geography file (e.g., "USA.txt")
   - The name of the election data file (e.g., "USA2020.txt")
   - The desired map style (1, 2, or 3)

## File Formats

### Geography File

Contains coordinates for drawing state boundaries. Format:

- Minimum longitude and latitude
- Maximum longitude and latitude
- Number of regions
- For each region:
  - Region name
  - Number of points
  - List of longitude/latitude pairs

### Election Results File

Contains vote counts for each state. Format:

- Header row
- Rows with: State name, Republican votes, Democrat votes, Other votes
