from app.repository.customer_repository import CustomerRepository
from app.database import SessionLocal


class CustomerService:

    @staticmethod
    async def create_customer(customer_data: dict):
        db = SessionLocal()
        try:
            return await CustomerRepository.create_customer(db, customer_data)
        finally:
            db.close()

    @staticmethod
    async def get_customers():
        db = SessionLocal()
        try:
            return await CustomerRepository.get_customers(db)
        finally:
            db.close()

    @staticmethod
    async def get_customer_by_id(customer_id: int):
        db = SessionLocal()
        try:
            # Fix: Use the correct repository method for
            # getting a customer by ID
            return await CustomerRepository.get_customer_by_id(
                db=db, customer_id=customer_id
            )
        finally:
            db.close()

    @staticmethod
    async def update_customer(customer_id: int, customer_data: dict):
        db = SessionLocal()
        try:
            return await CustomerRepository.update_customer(
                db, customer_id, customer_data
            )
        finally:
            db.close()

    @staticmethod
    async def delete_customer(customer_id: int):
        db = SessionLocal()
        try:
            return await CustomerRepository.delete_customer(db, customer_id)
        finally:
            db.close()
