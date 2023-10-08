# from passlib.hash import bcrypt
from tortoise import Tortoise, fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

from pydantic import BaseModel
from datetime import datetime
from typing import Tuple


class Post(Model):
    id = fields.IntField(pk = True)
    date = fields.DatetimeField(null = False)
    title = fields.CharField(max_length = 245)
    text = fields.TextField()
    comments = fields.ReverseRelation["Comment"]

    def __str__(self):
        return f"{self.date} - {self.title}"


class Comment(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(max_length = 245)
    date = fields.CharField(max_length = 125)
    text = fields.TextField()
    post = fields.ForeignKeyField(model_name='models.Post', source_field='postid', related_name='comments')

    def __str__(self):
        return f"{self.date} - {self.name}"


Tortoise.init_models(["posts.models"], "models")

PostPydantic = pydantic_model_creator(
    Post,
    name = "Post",
)

CommentPydantic = pydantic_model_creator(
    Comment,
    name = "Comment",
)
