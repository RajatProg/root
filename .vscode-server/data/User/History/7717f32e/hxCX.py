from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a main function to run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)