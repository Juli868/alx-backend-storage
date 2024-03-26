#!/usr/bin/env python3
"""Search specifically."""
def schools_by_topic(mongo_collection, topic):
    parameters = {"topics": topic}
    return mongo_collection.find(parameters)
