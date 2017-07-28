#!/usr/bin/env python

import json

from updater import app
from updater.parser import Processo

@app.task
def fetch(q):
    """
    Should fetch relational database rows based on the
    given query.
    """
    return (
        (123, 0, 1, 'RE'),
        (456, 1, 1, 'ARE'),
        (789, 0, 0, 'ADI'),
    )

@app.task
def parse(data, tablename='processo'):
    """
    Should intercept the data fetched from the db and apply
    the formating, cleanse, wrangling and all proper data
    preparation steps.
    """
    parsed = []
    if tablename == 'processo':
        for datum in data:
            p = Processo(datum)
            parsed.append(p.value)
    return parsed

@app.task
def jsonify(data):
    """
    Given a resultset and a list with the columns for the
    proper identification, convert the data into json format.
    """
    data = [{column: value for column, value in datum} for datum in data]
    return json.dumps(data)
