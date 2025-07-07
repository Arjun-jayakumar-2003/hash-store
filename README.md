# 🔐 hash-store

A simple Python tool to **generate**, **store**, and **lookup** SHA-256 hashes of files — useful for verifying file integrity or detecting tampering.

---

## 📦 Features

- Add any file’s SHA-256 hash to a local database (`hash_database.json`)
- Lookup files using their hash value
- Prevent duplicates or detect changes in file content
- Lightweight and beginner-friendly

---

## 🚀 Getting Started

### 1. Clone the repository


### 2. Run the script


### 3. Choose a mode

- `add`: Store a file’s SHA-256 hash in the database  
- `find`: Look up a file path by its SHA-256 hash

---

## 📂 Example Usage

### Add a file to the database:

```
Do you want to [add] a file or [find] a file by its hash ?: add  
Enter the file path: "C:\Users\me\Documents\example.pdf"
```

### Find a file by hash:

```
Do you want to [add] a file or [find] a file by its hash ?: find  
Enter the SHA-256 hash value: d2d2d0a334b66c8a...
```

---

## 🧠 Why Use This?

- Check if a file has been tampered with  
- Quickly identify duplicate files  
- Keep track of important or sensitive files

---

## 📁 Database Format

- JSON file: `hash_database.json`
- Format:

```json
{
    "d2d2d0a334b66c8a...": "C:\\path\\to\\file.mp4"
}
```

---

## ✅ To-Do (Optional Improvements)

- Add CLI flags (e.g., `--add`, `--find`)
- GUI version
- Support for multiple hash algorithms (e.g., MD5, SHA-1)

---

## 📄 License

MIT License. Use freely and modify as needed.
