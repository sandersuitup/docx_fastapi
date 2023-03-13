import logging

from fastapi import HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from .file_modifier import FileModifier
from .file_reader import FileReader

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocxFileProcessor:
	def __init__(self, file_reader: FileReader, file_modifier: FileModifier):
		"""
		Constructor for the DocxFileProcessor class

		:param file_reader: Instance of the FileReader class
		:param file_modifier: Instance of the FileModifier class
		"""
		self.file_reader = file_reader
		self.file_modifier = file_modifier

	async def process_file(self, file: UploadFile) -> StreamingResponse:
		"""
		Async method to process a docx file

		:param file: An instance of the FastAPI UploadFile class representing the file to be processed
		:return: A StreamingResponse object containing the modified file contents
		"""
		try:
			# Read in the file contents using the FileReader object
			file_contents = await self.file_reader.read_file(file)

			# Modify the docx file contents using the FileModifier object
			modified_file_contents = self.file_modifier.modify_docx(file_contents)

			# Return a StreamingResponse object containing the modified file contents
			return StreamingResponse(iter([modified_file_contents]),
									media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
									headers={"content-disposition": f"attachment; filename={file.filename}"})
		except Exception as e:
			# Log the error and raise a HTTPException with a 500 status code
			logger.error(f"Error processing file {file.filename}: {e}")
			raise HTTPException(status_code=500, detail="Error processing file. Please try again later.")
