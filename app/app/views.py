from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from . import service

router = APIRouter(prefix="/items")

templates = Jinja2Templates(directory="app/app/templates")

@router.get("/", response_class=HTMLResponse)
async def get_items(
    request: Request,
    message: Annotated[str, Depends(service.create_message)]
    ):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": message}
        )