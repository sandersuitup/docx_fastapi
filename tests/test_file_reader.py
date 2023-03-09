import asyncio
import io

import pytest
from fastapi import UploadFile

from modules.file_reader import FileReader


def test_read_file():
	# Create a sample file in memory
	file_contents = b'This is a sample file'
	file = UploadFile(filename='sample.txt', file=io.BytesIO(file_contents))

	# Read the file using FileReader
	file_reader = FileReader(allowed_extensions=['txt'])
	read_file_contents = asyncio.run(file_reader.read_file(file))

	# Check if the file contents match
	assert read_file_contents == file_contents

def test_read_file_invalid_extension():
	# Create a sample file in memory
	file_contents = b'This is a sample file'
	file = UploadFile(filename='sample.txt', file=io.BytesIO(file_contents))

	# Read the file using FileReader with an invalid extension
	file_reader = FileReader(allowed_extensions=['docx'])
	with pytest.raises(Exception):
		asyncio.run(file_reader.read_file(file))
