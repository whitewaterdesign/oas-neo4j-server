from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
from openai import OpenAI

from app.config import get_config

config = get_config()
app = FastAPI()

client = OpenAI(api_key=config.openai_api_key if hasattr(config, 'openai_api_key') else None)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    model: Optional[str] = "gpt-4"
    stream: Optional[bool] = False


@app.post("/v1/chat/completions")
async def chat_completions(request: ChatRequest):
    """
    Minimal chat completions endpoint compatible with OpenAI API format.

    :param request: ChatRequest - Contains messages, model, and stream flag
    :return: Chat completion response
    """
    messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]

    if request.stream:
        async def generate():
            stream = client.chat.completions.create(
                model=request.model,
                messages=messages,
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield f"data: {chunk.model_dump_json()}\n\n"
            yield "data: [DONE]\n\n"

        return StreamingResponse(generate(), media_type="text/event-stream")
    else:
        response = client.chat.completions.create(
            model=request.model,
            messages=messages
        )
        return response
