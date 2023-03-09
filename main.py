import logging

from fastapi import FastAPI, UploadFile

from modules.file_modifier import FileModifier
from modules.file_processor import DocxFileProcessor
from modules.file_reader import FileReader

# Create a FastAPI application instance
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create instances of the required classes
file_reader = FileReader(allowed_extensions=[".docx"])
file_modifier = FileModifier()
docx_processor = DocxFileProcessor(file_reader=file_reader, file_modifier=file_modifier)

# Define a route for modifying a DOCX file
@app.post("/modify-docx-file/")
async def modify_docx_file(file: UploadFile):
	# Process the file using the DocxFileProcessor instance
	return await docx_processor.process_file(file)
