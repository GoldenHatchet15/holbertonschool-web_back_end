#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient

def log_stats(mongo_collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{mongo_collection.count_documents({})} logs")

    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


def main():
    """ Main function """
    # Connection to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017/')
    # Select the 'logs' database and 'nginx' collection
    db = client.logs
    nginx_collection = db.nginx

    # Call the function with the selected collection
    log_stats(nginx_collection)

if __name__ == "__main__":
    main()
