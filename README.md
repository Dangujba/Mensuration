# Mensuration Mathematics Package

This Python package is designed to solve various mensuration problems in mathematics. It provides functions to calculate the area, perimeter, volume, and surface area of 15 different shapes. Additionally, it includes functions to draw the diagrams of these shapes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Shapes](#available-shapes)
  - [2D Shapes](#2d-shapes)
  - [3D Shapes](#3d-shapes)
- [Examples](#examples)
  - [Calculating Area](#calculating-area)
  - [Drawing Shapes](#drawing-shapes)
- [Contributing](#contributing)
- [License](#license)

## Features

- Calculate area, perimeter, volume, and surface area for 15 different shapes.
- Draw diagrams of 2D shapes.
- Simple and intuitive API.

## Installation

You can install this package using pip:

```bash
pip install mensuration
```
Or clone the repository:
```bash
git clone https://github.com/yourusername/mensuration.git
cd mensuration
```
## Usage 
Import the package and use the functions to perform mensuration calculations or draw shapes.

```python
from mensuration import circle_area, draw_square

# Calculate the area of a circle with radius 5
area = circle_area(5)
print(f"Area of the circle: {area}")

# Draw a square with side length 10
draw_square(10)
```

## Available Shapes

### 2D Shapes

- **Circle**
  - `area(radius)`
  - `circumference(radius)`
  - `draw(radius)`
- **Square**
  - `area(side)`
  - `perimeter(side)`
  - `draw(side)`
- **Rectangle**
  - `area(length, width)`
  - `perimeter(length, width)`
  - `draw(length, width)`
- **Triangle**
  - `area(base, height)`
  - `perimeter(side1, side2, side3)`
  - `draw(side1, side2, side3)`
- **Parallelogram**
  - `area(base, height)`
  - `perimeter(base, side)`
  - `draw(base, side)`
- **Ellipse**
  - `area(major_axis, minor_axis)`
  - `circumference(major_axis, minor_axis)`
  - `draw(major_axis, minor_axis)`
- **Trapezoid**
  - `area(base1, base2, height)`
  - `perimeter(base1, base2, side1, side2)`
  - `draw(base1, base2, height)`
- **Rhombus**
  - `area(diagonal1, diagonal2)`
  - `perimeter(side)`
  - `draw(side)`
- **Pentagon**
  - `area(side)`
  - `perimeter(side)`
  - `draw(side)`
- **Hexagon**
  - `area(side)`
  - `perimeter(side)`
  - `draw(side)`
- **Octagon**
  - `area(side)`
  - `perimeter(side)`
  - `draw(side)`

### 3D Shapes

- **Prism**
  - `volume(base_area, height)`
  - `surface_area(base_perimeter, base_area, height)`
- **Pyramid**
  - `volume(base_area, height)`
  - `surface_area(base_perimeter, slant_height, base_area)`
- **Cone**
  - `volume(radius, height)`
  - `surface_area(radius, slant_height)`
- **Cylinder**
  - `volume(radius, height)`
  - `surface_area(radius, height)`
  - `draw(radius, height)`

## Examples

### Calculating Area

Calculate the area of a rectangle:
```python
from mensuration import rectangle_area

length = 10 width = 5 area = rectangle_area(length, width) print(f"The area of the rectangle is {area}")
```

### Drawing Shapes

Draw a hexagon with a side length of 7:
```python
from mensuration import draw_hexagon

draw_hexagon(7)
```
