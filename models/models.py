from dataclasses import dataclass
from datetime import datetime
from typing import List


class BaseModel:
    id:int
    created_at:datetime
    last_modified:datetime


class User(BaseModel):
    name:str
    phone_number:str
    password:str

class Group(BaseModel):
    name:str
    user_list: List[User]
    created_by:User

class ExpenseSplit(BaseModel):
    user:User
    split_amount:float 

class Expense(BaseModel):
    description:str
    paid_by:User
    paid_amount:float
    group:Group
    is_group_expense:bool
    exppense_splits: List[ExpenseSplit]




@dataclass
class Transaction(BaseModel):
    is_group_transaction:bool
    group:Group
    received_by:User
    paid_by:User
    amount:float
    is_settled:bool




