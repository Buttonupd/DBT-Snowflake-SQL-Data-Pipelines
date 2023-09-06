from django.db import models

# schema for the database backing our django project

class Movie:
    def __init__(self, title):
        self.title = title

    def __str__(self) -> str:
        return super().__str__()

mov = Movie
m = mov.title = "Test"
print(m)