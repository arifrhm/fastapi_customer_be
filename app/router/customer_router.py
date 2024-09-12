from fastapi import APIRouter, HTTPException
from app.controller.customer_controller import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer,
    delete_customer,
)
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate

customer_router = APIRouter()


# Create customer
@customer_router.post("/customers/")
async def create(customer: CustomerCreate):
    return await create_customer(customer)


# Get all customers
@customer_router.get("/customers/")
async def read_all():
    return await get_customers()


# Get customer by ID
@customer_router.get("/customers/{customer_id}")
async def read_by_id(customer_id: int):
    customer = await get_customer_by_id(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


# Update customer
@customer_router.put("/customers/{customer_id}")
async def update(customer_id: int, customer: CustomerUpdate):
    updated_customer = await update_customer(customer_id, customer)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer


# Delete customer
@customer_router.delete("/customers/{customer_id}")
async def delete(customer_id: int):
    is_deleted = await delete_customer(customer_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"detail": "Customer deleted successfully"}
