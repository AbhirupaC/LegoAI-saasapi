from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")



oauth_token = Depends(oauth2_scheme)