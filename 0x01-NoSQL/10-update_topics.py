#!/usr/bin/env python3
"""Data updates."""


def update_topics(mongo_collection, name, topics):
    """Update data according to the parameters."""
    target = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_one(target, new_values)
