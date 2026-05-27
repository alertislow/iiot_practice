from pymongo import MongoClient

# 嘗試連線到你之前啟動的 Docker MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    # 叫資料庫回報它的清單
    databases = client.list_database_names()
    print("✅ 資料庫連線大成功！")
    print(f"目前資料庫清單有：{databases}")
    print(f"你好目前共有 {len(databases)} 個資料庫！")
except Exception as e:
    print("❌ 連線失敗，原因如下：")
    print(e)