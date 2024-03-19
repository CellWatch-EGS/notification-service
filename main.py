import uvicorn
import importlib

app = importlib.import_module("notification-api.app").app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)