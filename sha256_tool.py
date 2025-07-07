import hashlib
import os
import json

HASH_DB = "hash_database.json"

def load_hash_db():  
    if os.path.exists(HASH_DB):
        with open(HASH_DB,"r") as f:
            return json.load(f)
    return {} 


def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f: 
        while chunk:= f.read(4096):
            sha256.update(chunk)
        return sha256.hexdigest()

def save_hash_db(db): 
    with open(HASH_DB,"w") as f:
        json.dump(db,f,indent=4)

def add_file_to_db(file_path):
    if not os.path.exists(file_path): 
        print("file not found")
        return
    file_hash = hash_file(file_path) 
    db = dict(load_hash_db()) 
    db[file_hash] = file_path 
    save_hash_db(db)
    
def find_file_by_hash(query_hash): 
    db = load_hash_db()
    file = db.get(query_hash) 
    if file:
        print(f"found file {file}")
    else:
        print("file not found")

def main():
    mode = input("Do you want to [add] a file or [find] a file by its hash ?: ").lower()

    if mode == "add":
        file_path = input("Enter the file path: ").strip('"')
        add_file_to_db(file_path)
    elif mode == "find":
        query = input("Enter the SHA-256 hash value: ")
        find_file_by_hash(query)
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main()
    
