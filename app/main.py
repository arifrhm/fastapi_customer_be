from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.router.customer_router import customer_router
from app.database import engine, Base
from app.middleware.exception_middleware import ExceptionMiddleware

app = FastAPI()

# Include customer router
app.include_router(customer_router)

# Enable CORS for specific origins
app.add_middleware(
    CORSMiddleware,
    # You can list specific domains or use ["*"] for all origins
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Enable Gzip compression for responses
# minimum_size specifies the minimum response size to compress.
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Add the middleware to the application
app.add_middleware(ExceptionMiddleware)

# Create all the database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer API"}
