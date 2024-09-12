from typing import List, Optional
from app.service.customer_service import CustomerService
from app.schemas.customer_schema import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)


# Create customer
async def create_customer(customer_data: CustomerCreate) -> CustomerResponse:
    # Convert Pydantic model to dict before passing to the service
    customer_dict = customer_data.model_dump()
    return await CustomerService.create_customer(customer_dict)


# Get all customers
async def get_customers() -> List[CustomerResponse]:
    return await CustomerService.get_customers()


# Get customer by ID
async def get_customer_by_id(customer_id: int) -> Optional[CustomerResponse]:
    return await CustomerService.get_customer_by_id(customer_id)


# Update customer
async def update_customer(
    customer_id: int, customer_data: CustomerUpdate
) -> Optional[CustomerResponse]:
    # Convert Pydantic model to dict before passing to the service
    customer_dict = customer_data.model_dump()
    return await CustomerService.update_customer(customer_id, customer_dict)


# Delete customer
async def delete_customer(customer_id: int) -> bool:
    return await CustomerService.delete_customer(customer_id)
