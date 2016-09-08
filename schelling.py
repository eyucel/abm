import matplotlib.pyplot as plt
import itertools
import random
import copy

class Schelling:
    def __init__(self, width, height, empty_ratio, similarity_threshold, n_iterations, races = 2):
        self.width = width
        self.height = height
        self.races = races
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.empty_houses = []
        self.agents = {}

    def populate(self):
        ....

    def is_unsatisfied(self, x, y):
        ....

    def update(self):
        ....

    def move_to_empty(self, x, y):
        ....

    def plot(self):
        ....