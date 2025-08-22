from pydantic import BaseModel

class MathSchema(BaseModel):
    is_math_question: bool
    reason_math: str

class PoliticalSchema(MathSchema):
    is_political_question: bool
    reason_political: str