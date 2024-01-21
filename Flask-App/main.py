"""import re
import os
import yaml

# Read rule set patterns from config.yaml
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
    rule_set = config["rules"]

rulesScanned = len(rule_set)
print('total rules: ', rulesScanned)

# List all files in the testcode folder
testcode_folder = "testcode"
print("Files in testcode folder:")
for filename in os.listdir(testcode_folder):
    if filename.endswith(".py"):  # Process only Python files
        print(filename)

# Iterate through each file in the testcode folder
for filename in os.listdir(testcode_folder):
    if filename.endswith(".py"):  # Process only Python files
        file_path = os.path.join(testcode_folder, filename)
        with open(file_path, "r") as code_file:
            code_lines = code_file.readlines()

        print("Processing file:", filename)
        
        # Iterate through each line and apply rules
        for line_number, line in enumerate(code_lines, start=1):
            for rule in rule_set:
                try:
                    pattern = rule["pattern"]
                    # print(".")
                    if re.search(pattern, line):
                        print(f"Pattern Match: {pattern}")
                        print(f"Code Line {line_number}: {line.strip()}")
                        print("-" * 30)

                        # No need to continue checking other rules for this line
                        break
                except Exception as e:
                    print(f"An error occurred: {e}")
"""

import re
import os
import yaml

def cliResponse(file_count, numRules, rule_set_name, fileNames):
    response = f"""
┌─────────────┐
│ Scan Status │     SECURIX
└─────────────┘
  Scanning {file_count} files with {numRules} Code rules {rule_set_name}:
                                                                                
  Language      Rules   Files            Rules   Rule Category                     
 ─────────────────────────────        ───────────────────                       
  {rule_set_lang[0]}            {numRules}      {file_count}            {numRules}      {rule_set_name}                    
                                                                                
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00                                                                                

  Files: {fileNames}             
                
┌──────────────┐
│ Scan Summary │
└──────────────┘

Ran {numRules} rules on {file_count} files: {findings} findings.
If SECURIX missed a finding, please send us feedback to let us know!
  $ SECURIX shouldafound --help
                
"""
    return response

'''
┌─────────────┐
│ Scan Status │
└─────────────┘
  Scanning 2 files tracked by git with 1607 Code rules, 536 Pro rules:
                                                                                
  Language      Rules   Files          Origin      Rules                        
 ─────────────────────────────        ───────────────────                       
  <multilang>      58       6          Community    1071                        
  python          351       1          Pro rules     536                        
  json              4       1                                                   
                                                                                
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00                                                                                
                
                
┌──────────────┐
│ Scan Summary │
└──────────────┘

Ran 1607 rules on 2 files: 0 findings.
If Semgrep missed a finding, please send us feedback to let us know!
  $ semgrep shouldafound --help
'''

# Read rule set patterns from config.yaml
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
    rule_set = config["rules"]
    rule_set_name = config["name"]
    rule_set_lang = config["languages"]
    
numRules = len(rule_set)
# print('total rules: ', numRules)

# List all files in the testcode folder
testcode_folder = "testcode"

# Count Files in testcode folder
file_count = 0
for filename in os.listdir(testcode_folder):
    if filename.endswith(".py"):  # Process only Python files
        file_count += 1

findings = 0
fileNames = []
for filename in os.listdir(testcode_folder):
    if filename.endswith(".py"):  # Process only Python files
        fileNames.append(filename)
        # print(filename)

# Create or open the logs.txt file for writing
with open("logs.txt", "w") as logs_file:
    rules_matched = 0  # Counter for matched patterns
    
    # Iterate through each file in the testcode folder
    for filename in os.listdir(testcode_folder):
        if filename.endswith(".py"):  # Process only Python files
            file_path = os.path.join(testcode_folder, filename)
            with open(file_path, "r") as code_file:
                code_lines = code_file.readlines()

            # print("\nProcessing file:", filename)

            # Iterate through each line and apply rules
            for line_number, line in enumerate(code_lines, start=1):
                for rule in rule_set:
                    try:
                        pattern = rule["pattern"]
                        if re.search(pattern, line):
                            rules_matched += 1
                            message = rule["message"]
                            severity = rule["severity"]
                            impact = rule["metadata"]["impact"]
                            cwe = ", ".join(rule["metadata"]["cwe"])
                            owasp = ", ".join(rule["metadata"]["owasp"])

                            findings = findings + 1
                            logs_file.write(
                                f"Line: {line_number} \t Filename: {filename} | \n\t\t\t Code: {line.strip()} | Impact: {impact} | "
                                f"Severity: {severity} |\n\t\t\t Message: {message} |\n\t\t\t CWE: {cwe} |\n\t\t\t OWASP: {owasp}\n\n"
                            )
                            logs_file.write(" " * 80 + "\n")

                            # No need to continue checking other rules for this line
                            break
                    except Exception as e:
                        print(f"An error occurred: {e}")

    if rules_matched > 0:
        # print("Patterns matched:", rules_matched)
        print("Results saved in logs.txt")
    else:
        print("No patterns matched.")

# print(cliResponse(file_count, numRules, rule_set_name, fileNames))