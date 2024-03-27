from flask import Flask, render_template, request, send_file
# from flask_ngrok import run_with_ngrok


import getpass
import os
from pyngrok import ngrok, conf

import os
import requests
from zipfile import ZipFile
from io import BytesIO
import subprocess
import shutil
import re
import yaml
import json



app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when the app is run


# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(5000).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, 5000))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'static/uploads_files'
app.config['GITHUB_FOLDER'] = 'static/github_folders'
app.config['SETUP_FOLDER'] = 'static/setup'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GITHUB_FOLDER'], exist_ok=True)
os.makedirs(app.config['SETUP_FOLDER'],  exist_ok=True)

'''
@app.route("/")
def index():
    return "Hello from Colab!"

@app.route("/greet/<username>")
def greet_user(username):
    print(f"Hello, {username}!")
    return f"Hello, {username}!"

# Start the Flask server without threading
app.run(port=5000, use_reloader=False)
'''

# main code ------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/file_scan', methods=['POST'])
def file_scan():
    # Clear existing files in the upload folder
    clear_upload_folder()

    # Get the file content and other information from the POST request
    scan_mode = request.form.get('mode')

    file_content = request.files.get('file_content')
    file_name = request.form.get('file_name')

    if not file_content or not file_name:
        return "No file content or file name provided"

    # Save the file content to a file
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file_content.save(filename)

    if scan_mode == 'regex':
        
        # List all files in the testcode folder
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        testcode_file = files[0]
        # print("testcode_file :", testcode_file)
        file_type = ''

        # file_type_list = ['.py', '.java', '.c++']
        if testcode_file.endswith('.py'):  # Process only Python files
            file_type += 'python'
            RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/py_config.yaml')
        
        elif testcode_file.endswith('.java'): # Process only Java files  
            file_type += 'java'
            RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/java_config.yaml')

        elif testcode_file.endswith('.c++') or testcode_file.endswith('.cpp'):  # Process only c++ or cpp files
            file_type += 'c++'
            RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/c_plus_plus_config.yaml')
        print(f"input file_type : ", file_type, "RuleFilePath : ", RuleFilePath)

        # Read rule set patterns from config.yaml
        with open(RuleFilePath, "r") as config_file:
            try:
                config = yaml.safe_load(config_file)
                rule_set = config["rules"]
                # rule_set_name = config["name"] # rule_set_lang = config["languages"]
            except subprocess.CalledProcessError as e:
                print(f"Error running batch file: {e}")

            
        numRules = len(rule_set)
        print("numRules :", numRules)
        logs_data = []

        # Create or open the logs.json file for writing
        testcode_file_path = os.path.join(app.config['UPLOAD_FOLDER'], testcode_file)
        with open(testcode_file_path, "r") as code_file:
            code_lines = code_file.readlines()

        # Iterate through each line and apply rules
        for line_number, line in enumerate(code_lines, start=1):
            for rule in rule_set:
                try:
                    pattern = rule["pattern"]
                    if re.search(pattern, line):
                        message = rule["message"]
                        severity = rule["severity"]
                        impact = rule["metadata"]["impact"]
                        cwe = rule["metadata"]["cwe"]
                        owasp = rule["metadata"]["owasp"]

                        if file_type == 'c++' or file_type == 'java':
                            logs_data.append({
                                "id": rule["id"],
                                "line_number": line_number,
                                "filename": testcode_file,
                                "code": line.strip(),
                                "impact": impact,
                                "severity": severity,
                                "message": message,
                                "cwe": cwe,
                                "owasp": owasp,

                                # for java & cpp only
                                "approxcorrectCode" : rule["correctcode"]
                            })
                        else:
                            logs_data.append({
                                "id": rule["id"],
                                "line_number": line_number,
                                "filename": testcode_file,
                                "code": line.strip(),
                                "impact": impact,
                                "severity": severity,
                                "message": message,
                                "cwe": cwe,
                                "owasp": owasp,
                            })

                        # No need to continue checking other rules for this line
                        break

                except Exception as e:
                    print(f"An error occurred: {e}")

        # Save data to logs.json
        LogsFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/logs.json')
                    
        with open(LogsFilePath, "w") as logs_json_file:
            json.dump(logs_data, logs_json_file, indent=2)

        print("Results saved in logs.json") if logs_data else print("No patterns matched.")
        # retData = f"Scanned files successfully !!! \n\n {logs_data}"        
        return logs_data

    else:
        inputfolder = "static/uploads_files"
        json_file_path = "static/setup/semgrep_mode/output.json"
        print("semgrep - json_file_path : ", json_file_path)

        # !semgrep --config=auto static/github_folders --output=static/setup/semgrep_mode/output.json --json --verbose
        os.system(f"semgrep --config=auto {inputfolder} --output={json_file_path} --json --verbose")

        # Read the content from the JSON file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
        jData = json.dumps(json_data, indent=2)
        
        # print("scanned repo with semgrep successfully !!!")
        return jData




















@app.route('/repo_scan', methods=['POST'])
def repo_scan():
    # Clear existing files in the upload folder
    # clear_upload_folder()

    # Get the file content and other information from the POST request
    scan_mode = request.files.get('mode')

    repo_link = request.args.get('repo_link')

    if not repo_link:
        return "Repo link not provided"
    
    clone_path = os.path.join('static', 'github_folders', repo_link[19:].replace('/', '_'))
    
    os.system('rm -r static/github_folders/*') # Delete all previous clones

    # Use subprocess to run the git clone command
    try:
        subprocess.run(['git', 'clone', repo_link, clone_path])

    except subprocess.CalledProcessError as e:
        print(f"Error Cloneing Git Repo: {e}")

    if scan_mode == 'regex':
        return "service unavailable"

    else:
        inputfolder = "static/github_folders"
        json_file_path = "static/setup/semgrep_mode/output.json"
        print("semgrep - json_file_path : ", json_file_path)

        # !semgrep --config=auto static/github_folders --output=static/setup/semgrep_mode/output.json --json --verbose
        os.system(f"!semgrep --config=auto {inputfolder} --output={json_file_path} --json --verbose")

        # Read the content from the JSON file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
        jData = json.dumps(json_data, indent=2)
        
        # print("scanned repo with semgrep successfully !!!")
        return jData



























# unit testing ------------------------------------------

@app.route('/upload', methods=['POST'])
def upload_file():
    # Clear existing files in the upload folder
    clear_upload_folder()

    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # filename = f"/content/SECUIRX-v2-Flask-API/static/uploads_files/{file.filename}"
        file.save(filename)
        return "File uploaded successfully"
    
def clear_upload_folder():
    # List all files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    # print("list files : ", files)

    # Delete each file in the upload folder
    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        # file_path = f"/content/SECUIRX-v2-Flask-API/static/uploads_files/{file}"

        os.remove(file_path)
        print("deleted files : ", file_path)


@app.route('/upload_via_post', methods=['POST'])
def upload_file_via_post():
    # Clear existing files in the upload folder
    clear_upload_folder()

    # Get the file content and other information from the POST request
    file_content = request.files.get('file_content')
    # file_type = request.form.get('file_type')
    file_name = request.form.get('file_name')

    if not file_content or not file_name:
        return "No file content or file name provided"

    # Save the file content to a file
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    # filename = f"/content/SECUIRX-v2-Flask-API/static/uploads_files/{file_name}"

    file_content.save(filename)

    return "File uploaded successfully via POST"




# @app.route('/download_repo', methods=['GET'])
def download_repo(repo_link):
    # repo_link = request.args.get('repo_link')

    if not repo_link:
        return "Repo link not provided"

    # Clone the repo to the static/github_folders directory and delete previous clones
    clone_github_repo(repo_link)

    return "Repository cloned successfully"

def clone_github_repo(repo_link):
    # Assuming the repo link is in the format "https://github.com/username/repo"
    repo_url = repo_link
    clone_path = os.path.join('static', 'github_folders', repo_link[19:].replace('/', '_'))

    # Delete all previous clones
    clear_previous_clones()

    # Use subprocess to run the git clone command
    try:
        # Run the batch file
        subprocess.run(['git', 'clone', repo_url, clone_path])
        # print("Previous clones deleted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error Cloneing Git Repo: {e}")

def clear_previous_clones():

    # !rm -r /content/SECUIRX-v2-Flask-API/static/github_folders/*
    # subprocess.run(['!rm', '-r', '/content/SECUIRX-v2-Flask-API/static/github_folders/*'])
    # os.system('!rm -r /content/SECUIRX-v2-Flask-API/static/github_folders/*')
    os.system('rm -r static/github_folders/*')
    print("prev git repo deleted successfully !!!")




# Scanning
@app.route('/scanrepo', methods=['GET'])
def scanrepo():
    repo_link = request.args.get('repo_link')
    download_repo(repo_link)

    # !semgrep --config=auto railsgoat --output=output.json --json --verbose
    inputfolder = "static/github_folders"
    json_file_path = "static/setup/semgrep_mode/output.json"
    
    # json_file_path = os.path.join(app.config['SETUP_FOLDER'], 'semgrep_mode', 'output.json')
    print("semgrep - json_file_path : ", json_file_path)

    # !semgrep --config=auto static/github_folders/AtharvaPawar456_yerunkar-corner.git --output=static/setup/semgrep_mode/output.json --json --verbose

    os.system(f"!semgrep --config=auto {inputfolder} --output={json_file_path} --json --verbose")

    # Read the content from the JSON file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    jData = json.dumps(json_data, indent=2)
    print("scanned repo with semgrep successfully !!!")
    return jData


# py, java, c++ files scan
@app.route('/scanfiles', methods=['GET'])
def scanpyfile():
    # List all files in the testcode folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    testcode_file = files[0]
    print("testcode_file :", testcode_file)

    file_type = ''

    # file_type_list = ['.py', '.java', '.c++']
    # Process only Python files
    if testcode_file.endswith('.py'):  
        file_type += 'python'
        RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/py_config.yaml')
    
    # Process only Java files
    elif testcode_file.endswith('.java'):  
        file_type += 'java'
        RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/java_config.yaml')


    # Process only c++ or cpp files
    elif testcode_file.endswith('.c++') or testcode_file.endswith('.cpp'):  
        file_type += 'c++'
        RuleFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/ruleSets/c_plus_plus_config.yaml')

    print("input file_type : ", file_type)
    print("RuleFilePath : ", RuleFilePath)

    # Read rule set patterns from config.yaml
    with open(RuleFilePath, "r") as config_file:
        try:
            config = yaml.safe_load(config_file)
            rule_set = config["rules"]
            # rule_set_name = config["name"]
            # rule_set_lang = config["languages"]
        
        except subprocess.CalledProcessError as e:
            print(f"Error running batch file: {e}")
            print("---")

        
    numRules = len(rule_set)
    print("numRules :", numRules)

    # Create or open the logs.json file for writing
    logs_data = []

    testcode_file_path = os.path.join(app.config['UPLOAD_FOLDER'], testcode_file)
    with open(testcode_file_path, "r") as code_file:
        code_lines = code_file.readlines()

    # Iterate through each line and apply rules
    for line_number, line in enumerate(code_lines, start=1):
        for rule in rule_set:
            try:
                pattern = rule["pattern"]
                if re.search(pattern, line):
                    message = rule["message"]
                    severity = rule["severity"]
                    impact = rule["metadata"]["impact"]
                    cwe = rule["metadata"]["cwe"]
                    owasp = rule["metadata"]["owasp"]

                    logs_data.append({
                        "id": rule["id"],
                        "line_number": line_number,
                        "filename": testcode_file,
                        "code": line.strip(),
                        "impact": impact,
                        "severity": severity,
                        "message": message,
                        "cwe": cwe,
                        "owasp": owasp,

                        # for java & cpp only
                        "approxcorrectCode" : rule["correctcode"]
                    })

                    # No need to continue checking other rules for this line
                    break

            except Exception as e:
                print(f"An error occurred: {e}")

    # Save data to logs.json
    LogsFilePath = os.path.join(app.config['SETUP_FOLDER'], 'regex_mode/logs.json')
                
    with open(LogsFilePath, "w") as logs_json_file:
        json.dump(logs_data, logs_json_file, indent=2)

    # Print results
    if logs_data:
        print("Results saved in logs.json")
    else:
        print("No patterns matched.")


    print("scanned files successfully !!!")
    retData = f"Scanned files successfully !!! \n\n {logs_data}"
    
    return retData



if __name__ == '__main__':
    # app.run(debug=True)
    # app.run()
    app.run(port=5000, use_reloader=False)
