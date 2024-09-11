from pydantic import BaseModel

class Comment(BaseModel):
    task_id: int
    user_id: int
    content: str
