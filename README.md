# FastApi with docx upload POST request
- Test for job interview

# Virtualenv
- source env/bin/activate

# Docker commands
1. Build: docker build -t app .
2. Run: docker run -p 80:80 app
3. Test: docker run app python3.9 -m pytest tests/

# Postman
Open Postman and create a new request by clicking on the "New" button in the top left corner of the window.
1. In the "Enter request URL" field, enter the URL http://localhost:80/modify-docx-file/.
2. Select the HTTP method for the request (in this case, POST) from the dropdown menu next to the URL field.
3. Click on the "Body" tab and select the "form-data" option.
4. In the Key select File and in the value you click "Choose Files". Select the .DOCX file.
5. Click on the "Send" button to send the request to the endpoint.
6. When the request has been processed, the response should contain the modified .DOCX file as binary data.