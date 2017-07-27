#!/usr/bin/env python

import json

from updater import app

@app.task
def query_rows(q):
    """
    Should retrieve relational database rows based on the
    given query.
    """
    return (
        (123, 0, 1, 'RE'),
        (456, 1, 1, 'ARE'),
        (789, 0, 0, 'ADI'),
    )

@app.task
def jsonify_records(rset, columns):
    """
    Given a resultset and a list with the columns for the
    proper identification, convert the data into json format.
    """
    records = []
    for record in rset:
         records.append(dict(zip(columns, record)))
    return json.dumps(records)
