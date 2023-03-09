from typing import List


def is_valid_extension(filename: str, allowed_extensions: List[str]) -> bool:
	"""
	Check if the given filename has one of the allowed extensions.

	Args:
		filename (str): The name of the file to check.
		allowed_extensions (List[str]): A list of allowed extensions.

	Returns:
		bool: True if the filename has one of the allowed extensions, False otherwise.
	"""
	return any(filename.endswith(ext) for ext in allowed_extensions)
