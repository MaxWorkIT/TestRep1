from fastapi import FastAPI

app = FastAPI(
    title="TestRep1"
)


@app.get(path="/greeting{name}", description="greeting by name")
def greeting(name: str) -> str:
    """
    :param name: str
    :return: str = f"Halo, {name}!"
    """
    return f"Halo, {name}!"


@app.get(path="/farewell{name}", description="farewell by name")
def farewell(name: str) -> str:
    return f"Bye, {name}!"
