#!/usr/bin/env python3

class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'
        
    @property
    def species(self):
        return(self._species)
