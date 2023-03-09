from typing import List

from fastapi import HTTPException, UploadFile

from utils.helpers import is_valid_extension


class FileReader:
	def __init__(self, allowed_extensions: List[str]):
		# Initialize the FileReader object with a list of allowed file extensions.
		self.allowed_extensions = allowed_extensions
	
	async def read_file(self, file: UploadFile) -> bytes:
		# Check if the uploaded file's extension is allowed.
		if not is_valid_extension(file.filename, self.allowed_extensions):
			# Raise an HTTP exception if the extension is not allowed.
			raise HTTPException(status_code=400, detail="Invalid file type. Only .docx files are allowed.")
		
		# Return the contents of the uploaded file as bytes.
		return await file.read()
