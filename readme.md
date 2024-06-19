# A* Pathfinding Algorithm

This project implements the A* pathfinding algorithm to find the shortest path on a grid-based map. The algorithm is designed to avoid obstacles and find the most efficient path from a start point to an end point.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Introduction

The A* algorithm is a popular pathfinding and graph traversal algorithm used in many applications, such as AI for games, robotics, and GPS navigation. It combines the strengths of Dijkstra's algorithm and Greedy Best-First-Search by using a heuristic to guide its search.

## Features

- Reads grid data from a `.in` file
- Implements the A* algorithm to find the shortest path
- Handles obstacles and ensures valid pathfinding
- Outputs the path from start to end, if one exists

## Installation



Clone the repository to your local machine using:

`git clone https://github.com/yourusername/astar-pathfinding.git`
`cd astar-pathfinding`

Ensure you have Python installed. This code is compatible with Python 3.

## Usage

Prepare the grid file: Create a .in file (e.g., grid.in) with the grid layout. Each line represents a row in the grid, and each cell is separated by a space. 0 represents a walkable cell, and 1 represents an obstacle.



## Example
Here is an example of how to use the A* algorithm with a grid file.

Grid File (grid.in)
` 
0 1 0 0 0 | 0 1 0 1 0 | 0 0 0 1 0 | 0 1 0 0 0 | 0 0 0 0 0
`

## Running the Example
Ensure grid.in is in the same directory as astar.py. Run the script:


The output will be the path found by the A* algorithm:

Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
