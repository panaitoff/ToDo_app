from comments.models import Comment

comments_db = []

def get_all_comments():
    return comments_db

def create_comment(task_id: int, user_id: int, content: str):
    comment = Comment(task_id=task_id, user_id=user_id, content=content)
    comments_db.append(comment)
    return comment
