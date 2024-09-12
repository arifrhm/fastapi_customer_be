from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    address_city: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: int

    # Use ConfigDict instead of class Config
    model_config = ConfigDict(from_attributes=True)
