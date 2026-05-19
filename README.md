# StreamLens DB Engine 🚀

A lightweight database engine built in Python implementing SQL parsing, query planning, execution engine, and disk-based B+ Tree indexing.

## Features
- SQL SELECT support
- Index Scan (B+ Tree)
- Full Table Scan fallback
- Nested Loop Join
- Buffer Pool + Disk Layer

## Run
uvicorn api.server:app --reload

## Example
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"sql":"SELECT * FROM users WHERE id = 2"}'
