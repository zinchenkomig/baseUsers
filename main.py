from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from authentication.router import auth_router
from authentication.dependencies import get_current_user

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # ToDo: Change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_router,
                   prefix='/auth',
                   tags=['auth']
                   )


@app.get('/email')
async def get_email(user=Depends(get_current_user)):
    return user.email
