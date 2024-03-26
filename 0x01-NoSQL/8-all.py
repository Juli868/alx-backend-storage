#!/usr/bin/env python3
"""Mongo db."""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Return all files."""
    result = mongo_collection.find()
    return result
