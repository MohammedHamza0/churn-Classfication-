from pydantic import BaseModel, Field
from typing import Literal


class CustomData(BaseModel):
     CreditScore: int = Field(description="Customer's Credit Score")
     Geography: Literal["France", "Spain", "Germany"] = Field(description="Customer's Country")
     Gender: Literal["Male", "Female"] = Field(description="Customer Gender")
     Age: int = Field(description="Custumer Age", ge=18, le=100)
     Tenure: int = Field(description="Years as a customer (0-10)", ge=0, le=10)
     Balance: float = Field(description="Customer Balance", ge=0)
     NumOfProducts: int = Field(description="Number of bank products (0-4)", ge=0, le=4)
     HasCrCard: Literal[0, 1] = Field(description="Has a credit card (0 = No, 1 = Yes)")
     IsActiveMember: Literal[0, 1] = Field(description="Active member state (0=No, 1=Yes)")
     EstimatedSalary: float = Field(description="Estimated annual salary", ge=0)