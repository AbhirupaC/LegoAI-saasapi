from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules import smart_query
from app.modules import wrangler, canvas, governance, users
from core.conf import APP_CONFIG

from core.logger import log

router = FastAPI(prefix="/api/v1/")
# router.include_router(smart_query.router, tags=["Smart Query"],  prefix="/smart_query")
# router.include_router(wrangler.router, tags=["Ontocraft"],  prefix="/wrangler")
# router.include_router(canvas.router, tags=["Canvas"],  prefix="/canvas")
# router.include_router(governance.router, tags=["Governance"],  prefix="/governance")
router.include_router(users.router, tags=["Users"],  prefix="/users")


@router.on_event("startup")
def startup_event():
    log.info("Application starting")

@router.on_event("shutdown")
def shutdown_event():
    log.info("Application shutdown")

origins = ["*"]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)