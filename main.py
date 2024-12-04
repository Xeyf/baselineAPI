from fastapi import FastAPI

app = FastAPI()

@app.get("/baseline")
async def baseline():
    return {"message": "Baseline test successful"}

@app.post("/baseline")
async def baseline_post(input: dict):
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5151)