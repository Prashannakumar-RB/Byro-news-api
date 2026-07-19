import json
from datetime import datetime

data = {
    "last_update": datetime.utcnow().isoformat() + "Z",
    "status": "GitHub Action is working!",
    "events": []
}

with open("news.json", "w") as f:
    json.dump(data, f, indent=4)

print("news.json created successfully")
