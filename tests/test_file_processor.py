import io

import pytest
from fastapi import HTTPException, UploadFile

from modules.file_modifier import FileModifier
from modules.file_processor import DocxFileProcessor
from modules.file_reader import FileReader


def test_process_file():
	# Create a mock file reader object
	file_reader = FileReader(allowed_extensions=['docx'])

	# Create a sample file in memory
	file_contents = b'This is a sample file'
	file = UploadFile(filename='sample.docx', file=io.BytesIO(file_contents))

	# Create a mock file modifier object
	file_modifier = FileModifier()

	# Create a DocxFileProcessor instance and process a sample file
	file_processor = DocxFileProcessor(file_reader, file_modifier)

	try:
		with pytest.raises(HTTPException) as exc_info:
			processed_file = file_processor.process_file(file)
	except HTTPException as e:
		assert e.status_code == 400
		assert e.detail == "Invalid file format. Only .docx files are allowed."
	else:
		assert exc_info.value.status_code == 400
		assert exc_info.value.detail == "Invalid file format. Only .docx files are allowed."
