import os
import requests

def uploadfile():
    print("uploadfile() function running ...")

    url = "http://localhost:5000/upload_via_post"

    # file_path = "api_sample_uploads\codeGoat - Copy (2).c++"
    # file_path = "api_sample_uploads\codeGoat - Copy.java"
    file_path = "api_sample_uploads\codeGoat.py"

    # Extract the file name
    file_name = os.path.basename(file_path)

    # Prepare the file content and other data
    files = {'file_content': (file_name, open(file_path, 'r'))}
    data = {'file_name': file_name}

    # Make the POST request
    response = requests.post(url, files=files, data=data)

    # Print the response
    print(response.text)

def upload_GitLink():
    print("upload_GitLink() function running ...")
    url = "http://localhost:5000/download_repo"
    # repo_link = "https://github.com/AtharvaPawar456/Raspberry-Pi-Workshop.git"
    repo_link = "https://github.com/AtharvaPawar456/yerunkar-corner.git"

    # Make a GET request to download the repository
    params = {'repo_link': repo_link}
    response = requests.get(url, params=params)

    # Print the response
    print(response.text)

# uploadfile()
# upload_GitLink()
