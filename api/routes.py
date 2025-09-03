from fastapi import APIRouter, UploadFile, File, Form
from io import BytesIO
from services.excel_upload import parse_and_upload_excel
from models.data_model import UploadRequest

router = APIRouter()

@router.post("/upload-excel-data")
async def upload_excel_data(
    file: UploadFile = File(...),
    description: str = Form(None)
):
    request = UploadRequest(description=description)

    contents = await file.read()
    result = parse_and_upload_excel(BytesIO(contents))

    return {
        "file_name": file.filename,
        "metadata": request.model_dump(),
        "result": result
    }
