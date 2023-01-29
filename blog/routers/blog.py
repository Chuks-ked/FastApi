from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

    # blogs = db.query(models.Blog).all()
    # return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request, db)

    # new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id, db, request)

    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    # blog.update(request.dict())
    # db.commit()
    # return 'updated'

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id:int, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id, db)

    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail=f'blog with the id {id} is not available')
    # return blog
      