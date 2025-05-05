from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 그룹 생성 페이지 보여주기
@router.get("/create", response_class=HTMLResponse)
async def create_group_form(request: Request):
    return templates.TemplateResponse("group_create.html", {"request": request})

# 그룹 생성 처리
@router.post("/create")
async def create_group(request: Request, group_name: str = Form(...), description: str = Form("")):
    # 지금은 임시 처리. DB 없이 단순 로그 출력
    print(f"✅ 그룹 생성됨: 이름 = {group_name}, 설명 = {description}")
    return RedirectResponse("/", status_code=302)
