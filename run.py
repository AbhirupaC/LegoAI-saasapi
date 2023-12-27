import uvicorn
from core.conf import APP_CONFIG
from app import api

if __name__ == "__main__":
    uvicorn.run(
        "app.api:router",
        host="0.0.0.0",
        port=int(APP_CONFIG["PORT"]),
        # reload_dirs="app" if APP_CONFIG["DEPLOYMENT"].upper() != "PROD" else False,
        # reload_excludes=[APP_CONFIG.get("LOG_FILE", "apiservice.log"), "__pycache__"],
        reload=True
        # ssl_keyfile='certs/key.pem',
        # ssl_certfile='certs/certificate.pem'
    )
