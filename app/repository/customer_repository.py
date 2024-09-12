from sqlalchemy.orm import Session
from app.models.customer import Customer  # Assuming you have a Customer model


class CustomerRepository:

    @staticmethod
    async def create_customer(db: Session, customer_data: dict):
        new_customer = Customer(**customer_data)
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer

    @staticmethod
    async def get_customers(db: Session):
        return db.query(Customer).all()

    @staticmethod
    async def get_customer_by_id(db: Session, customer_id: int):
        return db.query(Customer).\
            filter(Customer.id == customer_id).first()

    @staticmethod
    async def update_customer(db: Session,
                              customer_id: int,
                              customer_data: dict):
        customer = db.query(Customer).\
            filter(Customer.id == customer_id).first()
        if customer:
            for key, value in customer_data.items():
                setattr(customer, key, value)
            db.commit()
            db.refresh(customer)
        return customer

    @staticmethod
    async def delete_customer(db: Session, customer_id: int):
        customer = db.query(Customer).\
            filter(Customer.id == customer_id).first()
        if customer:
            db.delete(customer)
            db.commit()
        return customer
