''' dfdf'''
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from connect import News, db, Sobis, Sotrud

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/new')
async def get_news():
    ''' kjkj'''
    new = News.select()
    return [{'name': ne.name, 'date': ne.date, 'text': ne.text,
             'img': ne.img}
            for ne in new]


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    ''' kjkj'''
    with db.connection_context():
        news_items = News.select().order_by(News.date.desc())
        formatted_news = [{
            "name": item.name,
            "date": item.date.strftime("%Y-%m-%d %H:%M:%S"),  # Формат даты
            "text": item.text,
            "img": item.img
        } for item in news_items]  # pylint: disable=E1133
        sobis = Sobis.select().order_by(Sobis.date.desc())
        ogost = [{
            'name': it.name,
            'date': it.date,
            'avtor': it.avtor,
            'text': it.text
        } for it in sobis]  # pylint: disable=E1133
        sotrud = Sotrud.select()
        ss = [{
            'name': ii.name,
            'dol': ii.dol,
            'email': ii.email,
            'phone': ii.phone,
            'date': ii.date
        } for ii in sotrud]
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "news_items": formatted_news,
                                       "sobis": ogost,
                                       'sotrud': ss})
