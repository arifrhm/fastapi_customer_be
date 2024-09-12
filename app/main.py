from fastapi import FastAPI
from app.router.customer_router import customer_router
from app.database import engine, Base

app = FastAPI()

# Include customer router
app.include_router(customer_router)

# Create all the database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer API"}
