from enum import Enum
from fastapi import UploadFile, File

class ResponseSignal(Enum):
    
    FILE_VALIDATION_SUCCESS = "File validation successfully."
    FILE_TYPE_NOT_ALLOWED = "File type is not supported."
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds the maximum limit."
    FILE_UPLOAD_SUCCESS = "File uploaded successfully."
    FILE_UPLOAD_FAILED = "File upload failed."
    FILE_NOT_FOUND = "File not found."
    FILE_PROCESSING_FAILED = "File processing failed."
    FILE_PROCESSING_SUCCESS = "File processing successfully."
    
