#!/usr/bin/env python
# coding: utf-8

class Processo(object):

    COLUMNS = ('soi', 'tipo', 'ramo', 'classe')
    
    def __init__(self, input):
        value = self._clean(input)
        self.value = zip(Processo.COLUMNS, value)

    def __repr__(self):
        return str(self.value)

    def _clean(self, input):
        return [
            int(input[0]),
            'Originário' if input[1] == 0 else 'Recursal',
            'Comum' if input[2] == 0 else 'Especial',
            input[3].upper(),
        ]
