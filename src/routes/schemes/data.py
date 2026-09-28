from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100   # Default chunk size if not provided
    overlap_size: Optional[int] = 20  # Default overlap size if not provided
    do_reset: Optional[int] = 0       # Default reset value if not provided