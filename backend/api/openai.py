from fastapi import FastAPI

app = FastAPI()

@app.get("/playlists")
async def get_playlists():
    # Logic to fetch playlists
    return {"playlists": []}
