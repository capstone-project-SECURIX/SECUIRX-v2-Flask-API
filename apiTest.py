import os
import requests

domain_link = "https://cb84-35-229-130-116.ngrok-free.app/"


def uploadfile():
    print("uploadfile() function running ...")

    # url = "http://localhost:5000/upload_via_post"
    url = f"{domain_link}upload_via_post"

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
    # url = "http://localhost:5000/download_repo"
    url = f"{domain_link}download_repo"

    # repo_link = "https://github.com/AtharvaPawar456/Raspberry-Pi-Workshop.git"
    repo_link = "https://github.com/AtharvaPawar456/yerunkar-corner.git"

    # Make a GET request to download the repository
    params = {'repo_link': repo_link}
    response = requests.get(url, params=params)

    # Print the response
    print(response.text)

# def scan_file(mode='regex'):
def scan_file():
    print("upload_GitLink() function running ...")
    # url = "http://localhost:5000/download_repo"
    # url = f"{domain_link}scanrepo"
    url = f"{domain_link}scanfiles"


    # Make a GET request to download the repository
    # params = {'mode': mode}
    # response = requests.get(url, params=params)
    response = requests.get(url)

    # Print the first 500 characters of the response
    print(response.text[:500])    
    
    # You can also save the response to a file for further analysis
    with open('research/response_content.txt', 'w') as file:
        file.write(response.text)













# def scan_file(mode='regex'):
def scan_file_final():
    print("upload_GitLink() function running ...")
    # url = "http://localhost:5000/download_repo"
    # url = f"{domain_link}scanrepo"
    url = f"{domain_link}file_scan"

    mode = 'regex'
    # mode = 'semgrep'

    file_path = "api_sample_uploads\codeGoat - Copy (2).c++"
    # file_path = "api_sample_uploads\codeGoat - Copy.java"
    # file_path = "api_sample_uploads\codeGoat.py"

    # Extract the file name
    file_name = os.path.basename(file_path)

    # Prepare the file content and other data
    files = {'file_content': (file_name, open(file_path, 'r'))}
    data = {'file_name': file_name, 'mode': mode}

    response = requests.post(url, files=files, data=data)

    # Make the POST request
    # response = requests.post(url, files=files, data=data)

    # Make a GET request to download the repository
    # params = {'mode': mode, 'file_name': file_name, 'file_content': (file_name, open(file_path, 'r'))}
    # response = requests.post(url, params=params)
    
    # response = requests.get(url)

    # Print the first 500 characters of the response
    print(response.text[:500])    
    
    # You can also save the response to a file for further analysis
    with open('research/response_content.txt', 'w') as file:
        file.write(response.text)



# uploadfile()
# upload_GitLink()
scan_file_final()