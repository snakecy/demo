#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ================================================

# @FileName          : app.py
# @Author            : zhoushaolong
# @Email             : zhoushaolong@haier.com
# @CreatedTime       : 2023-03-03 20:08
# @ModifiedTime      :

# ================================================
"""
# Decription

"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def query():
    return "hello world"

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


