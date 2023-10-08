import json
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, Request

# from constants import redis
from posts.models import Post, Comment, PostPydantic, CommentPydantic

post_router = APIRouter()

@post_router.get("/posts", response_model = List[PostPydantic], tags = ["posts"])
async def get_posts():

    # Fetch all posts
    posts = Post.all().prefetch_related("comments")
    return await PostPydantic.from_queryset(posts)
