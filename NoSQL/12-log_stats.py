#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    print(f"{mongo_collection.count_documents({'method': 'GET', 'path': '/status'})} status check")
