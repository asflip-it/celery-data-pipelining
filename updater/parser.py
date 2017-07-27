#!/usr/bin/env python

class Processo(object):

    COLUMNS = ('soi', 'tipo', 'ramo', 'classe')
    
    def __init__(self, input):
        self.value = clean(input)

    def __repr__(self):
        return self.value

    def _clean(input):
        pass

