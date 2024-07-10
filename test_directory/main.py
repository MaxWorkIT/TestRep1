from fastapi import FastAPI

app = FastAPI(
    title="TestRep1"
)


@app.get(path="/greeting{name}", description="greeting by name")
def greeting(name: str) -> str:
    return f"Halo, {name}"
