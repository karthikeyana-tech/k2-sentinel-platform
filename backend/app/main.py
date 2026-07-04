from fastapi import FastAPI
from app.core.database import Base, engine

from app.api.tourist import router as tourist_router
from app.api.incident import router as incident_router
from app.api.alert import router as alert_router

app = FastAPI(title="K2 Sentinel")

# create tables
Base.metadata.create_all(bind=engine)

# routers
app.include_router(tourist_router, prefix="/api/v1/tourists", tags=["Tourists"])
app.include_router(incident_router, prefix="/api/v1/incidents", tags=["Incidents"])
app.include_router(alert_router, prefix="/api/v1/alerts", tags=["Alerts"])


@app.get("/")
def root():
    return {"status": "running"}