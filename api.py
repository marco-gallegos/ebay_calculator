# Import statements
from fastapi import FastAPI
# from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import calculator

client_apps = ['http://localhost:3000']#Our REACT app will be running on this IP and PORT

# Create app
app = FastAPI()
# register your router
# app.include_router(student_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# modularizing routes
app.include_router(calculator)

#Register App with CORS middleware to allow resourse sharing between different domains/origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
  uvicorn.run(
    "api:app",
    host="0.0.0.0", 
    port=8080,
    log_level="debug",
    # debug=True,
    #reload=True
   )
