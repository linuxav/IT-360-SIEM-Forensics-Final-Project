import os
import requests

# Create a dummy file locally for testing
test_filename = "test_upload_file.txt"
with open(test_filename, "w") as f:
    f.write("Hello World! This is a test file for my Python script.")

# Use httpbin.org/post to test the file upload
test_url = "https://httpbin.org/post"

with open(test_filename, "rb") as file_to_upload:
    files = {"file": file_to_upload}
    response = requests.post(test_url, files=files)

# Print out what the server received
print("--- Response Data ---")
#print(response.json())

# Print only the relevant data from the JSON
data = response.json()
uploadedData = data.get("files", {}).get("file", {})
print(uploadedData)

# 4. Clean up the dummy file (optional)
if os.path.exists(test_filename):
    os.remove(test_filename)
