#!/usr/bin/env python3
"""Insertion."""


def insert_school(mongo_collection, **kwargs):
    """Insert into a collection and return an id of the newly added object."""
    result = mongo_collection.insert_one(kwargs).inserted_id
    return result
