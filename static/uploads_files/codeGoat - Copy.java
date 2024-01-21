
// 1. SQL Injection:
String query = "SELECT * FROM users WHERE username = '" + userInput + "' AND password = '" + password + "'";

PreparedStatement statement = connection.prepareStatement("SELECT * FROM users WHERE username = " + userInput + " AND password = " + password);

Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM products WHERE id = " + productId);


PreparedStatement pstmt = conn.prepareStatement("INSERT INTO users (username, password) VALUES (" + username + ", " + password + ")");

Statement stmt = connection.createStatement();
stmt.executeUpdate("UPDATE accounts SET balance = balance - " + amount + " WHERE account_id = " + accountId);


PreparedStatement ps = connection.prepareStatement("DELETE FROM orders WHERE order_id = " + orderId);
Statement stmt = connection.createStatement();
ResultSet rs = stmt.execute("SELECT * FROM products WHERE category = " + category);

Statement stmt = connection.createStatement();
stmt.execute("DROP TABLE " + tableName);

PreparedStatement ps = connection.prepareStatement("INSERT INTO logs (message) VALUES (" + logMessage + ")");


Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM customers WHERE name = " + customerName);

PreparedStatement ps = connection.prepareStatement("UPDATE employees SET salary = " + newSalary + " WHERE id = " + employeeId);




// 2. Cross-Site Scripting (XSS):
out.print("<script>alert('Hello, XSS!');</script>");

  Runtime.getRuntime().exec("ls -l " + userInput);

  ProcessBuilder pb = new ProcessBuilder("echo", userInput);
Process process = pb.start();

  Runtime.getRuntime().exec("rm -rf " + directoryName);

  ProcessBuilder pb = new ProcessBuilder("cat " + fileName);
Process process = pb.start();

  ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "dir " + directoryPath);
Process process = pb.start();

  Runtime.getRuntime().exec("shutdown -r -t 0");

  ProcessBuilder pb = new ProcessBuilder("touch " + newFileName);
Process process = pb.start();

  Runtime.getRuntime().exec("mv " + sourceFile + " " + destinationDirectory);

  ProcessBuilder pb = new ProcessBuilder("curl", "-X", "POST", "-d", "data=" + postData, url);
Process process = pb.start();

1    Runtime.getRuntime().exec("cp " + sourceFile + " " + destinationDirectory);


// 3. Command Injection:
String command = "ls -l " + userInput;
Runtime.getRuntime().exec(command);

DirContext.search("ou=People," + userInput, "(objectclass=person)");
 DirContext.search("ou=Groups," + groupName, "(member=" + userDn + ")");
 DirContext.search("ou=Users," + ouName, "(cn=" + commonName + ")");
 DirContext.search("ou=Employees," + department, "(&(objectClass=user)(sAMAccountName=" + username + "))");
 DirContext.search(baseDn, "(&(objectClass=person)(uid=" + userId + "))");
 DirContext.search("ou=Accounts," + branch, "(accountNumber=" + accountNumber + ")");
 DirContext.search("ou=Groups," + group, "(memberUid=" + memberId + ")");
 DirContext.search("ou=People," + department, "(employeeNumber=" + employeeNumber + ")");
 DirContext.search("ou=Customers," + organization, "(cn=" + customerName + ")");
 DirContext.search("ou=Projects," + project, "(projectManager=" + managerId + ")");
 DirContext.search("ou=Users," + domain, "(sAMAccountName=" + username + ")");
 DirContext.search("ou=Resources," + resourceType, "(resourceId=" + resourceId + ")");
 DirContext.search("ou=Roles," + roleName, "(roleType=" + type + ")");
 DirContext.search("ou=Assets," + assetType, "(assetId=" + assetId + ")");
 DirContext.search("ou=Teams," + team, "(teamLead=" + leadId + ")");
 DirContext.search("ou=Events," + eventType, "(eventDate=" + date + ")");
 DirContext.search("ou=Locations," + location, "(zipCode=" + zipCode + ")");
 DirContext.search("ou=Departments," + department, "(departmentCode=" + code + ")");
 DirContext.search("ou=Contracts," + contractType, "(contractId=" + contractId + ")");
 DirContext.search("ou=Projects," + project, "(projectCode=" + projectCode + ")");
 DirContext.search("ou=Users," + organization, "(employeeId=" + employeeId + ")");
 DirContext.search("ou=Customers," + country, "(customerCode=" + customerCode + ")");
 DirContext.search("ou=Orders," + customer, "(orderNumber=" + orderNumber + ")");
 DirContext.search("ou=Assets," + asset, "(assetCode=" + assetCode + ")");
 DirContext.search("ou=Teams," + team, "(teamCode=" + teamCode + ")");
 DirContext.search("ou=Locations," + city, "(cityCode=" + cityCode + ")");
 DirContext.search("ou=Departments," + organization, "(deptCode=" + deptCode + ")");
 DirContext.search("ou=Contracts," + vendor, "(vendorCode=" + vendorCode + ")");
 DirContext.search("ou=Projects," + division, "(projectNum=" + projectNum + ")");


// 4. LDAP Injection:
DirContext ctx = new InitialDirContext();
NamingEnumeration<SearchResult> results = ctx.search("ou=People," + userInput, "(objectclass=person)");

// 5. Path Traversal:
String fileName = "/path/to/directory/" + userInput;
FileOutputStream fos = new FileOutputStream(fileName);

 File.createNewFile("path/to/directory/" + fileName);
 FileOutputStream fos = new FileOutputStream("data/" + dataFile + ".txt");
 FileInputStream fis = new FileInputStream("config/" + configFile);
 File.createNewFile("uploads/" + username + "_profile.jpg");
 FileOutputStream fos = new FileOutputStream("logs/" + logFileName, true);
 File.createNewFile("documents/" + documentName + ".pdf");
 FileOutputStream fos = new FileOutputStream("output/" + outputFileName);
 FileInputStream fis = new FileInputStream("input/" + inputFileName);
 File.createNewFile("images/" + imageName + ".png");
 FileOutputStream fos = new FileOutputStream("backup/" + backupFileName);
 FileInputStream fis = new FileInputStream("data/" + dataFileName);
 File.createNewFile("files/" + fileName + ".txt");
 FileOutputStream fos = new FileOutputStream("attachments/" + attachmentName);
 FileInputStream fis = new FileInputStream("resources/" + resourceName);
 File.createNewFile("downloads/" + downloadFileName);
 FileOutputStream fos = new FileOutputStream("logs/" + logFile);
 FileInputStream fis = new FileInputStream("input/" + userInput + "_file.txt");
 File.createNewFile("backup/" + backupFileName);
 FileOutputStream fos = new FileOutputStream("output/" + outputFileName);
 FileInputStream fis = new FileInputStream("data/" + dataFile + ".csv");
 File.createNewFile("files/" + fileName);
 FileOutputStream fos = new FileOutputStream("logs/" + logFileName);
 FileInputStream fis = new FileInputStream("documents/" + documentName + ".pdf");
 File.createNewFile("uploads/" + username + "_profile.jpg");
 FileOutputStream fos = new FileOutputStream("attachments/" + attachmentName);
 FileInputStream fis = new FileInputStream("resources/" + resourceName);
 File.createNewFile("downloads/" + downloadFileName);
 FileOutputStream fos = new FileOutputStream("logs/" + logFile);
 FileInputStream fis = new FileInputStream("input/" + userInput + "_file.txt");


// 6. XML Injection:
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
SAXParser saxParser = factory.newDocumentBuilder().parse(userInput);

SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlData + maliciousData)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlString + additionalData)));
 SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlContent + dynamicData)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlInput + userData)));
 SAXParserFactory.newInstance().newSAXParser().parse(new InputSource(new StringReader(xmlDocument + maliciousInput)), new MyHandler());
 DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new InputSource(new StringReader(xmlSource + userContent)));
 SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlData + inputData)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlString + dynamicData)));
 SAXParserFactory.newInstance().newSAXParser().parse(new InputSource(new StringReader(xmlDocument + userContent)), new MyHandler());
 DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new InputSource(new StringReader(xmlInput + maliciousData)));
 SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlContent + inputData)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlSource + dynamicData)));
 SAXParserFactory.newInstance().newSAXParser().parse(new InputSource(new StringReader(xmlDocument + userContent)), new MyHandler());
 DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new InputSource(new StringReader(xmlInput + maliciousInput)));
 SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlData + additionalData)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlString + userInput)));
 SAXParserFactory.newInstance().newSAXParser().parse(new InputSource(new StringReader(xmlDocument + dynamicData)), new MyHandler());
 DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new InputSource(new StringReader(xmlInput + maliciousData)));
 SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
 parser.parse(new InputSource(new StringReader(xmlContent + userInput)), new MyHandler());
 DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
 Document document = builder.parse(new InputSource(new StringReader(xmlSource + dynamicData)));
 SAXParserFactory.newInstance().newSAXParser().parse(new InputSource(new StringReader(xmlDocument + inputData)), new MyHandler());
 DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new InputSource(new StringReader(xmlInput + additionalData)));


// 7. Code Execution:
String command = "ls -l " + userInput;
Runtime.getRuntime().exec(command);

Runtime.getRuntime().exec("cmd /c " + command);
 ProcessBuilder pb = new ProcessBuilder("echo", userInput);
 Process process = pb.start();
 Runtime.getRuntime().exec("ls -l " + directory);
 ProcessBuilder pb = new ProcessBuilder("cat " + fileName);
 Process process = pb.start();
 Runtime.getRuntime().exec("rm -rf " + directory);
 ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "dir " + path);
 Process process = pb.start();
 Runtime.getRuntime().exec("shutdown -r -t 0");
 ProcessBuilder pb = new ProcessBuilder("touch " + newFile);
 Process process = pb.start();
 Runtime.getRuntime().exec("mv " + source + " " + destination);
 ProcessBuilder pb = new ProcessBuilder("curl", "-X", "POST", "-d", "data=" + postData, url);
 Process process = pb.start();
 Runtime.getRuntime().exec("cp " + sourceFile + " " + destinationDirectory);
 ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "copy " + source + " " + destination);
 Process process = pb.start();
 Runtime.getRuntime().exec("java -cp " + classpath + " MainClass");
 ProcessBuilder pb = new ProcessBuilder("ls", "-la");
 Process process = pb.start();
 Runtime.getRuntime().exec("cat " + filename);
 ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "type " + file);
 Process process = pb.start();
 Runtime.getRuntime().exec("python " + scriptPath);
 ProcessBuilder pb = new ProcessBuilder("python", scriptName);
 Process process = pb.start();
 Runtime.getRuntime().exec("javac " + sourceFile);
 ProcessBuilder pb = new ProcessBuilder("javac", fileName);
 Process process = pb.start();
 Runtime.getRuntime().exec("node " + scriptPath);
 ProcessBuilder pb = new ProcessBuilder("node", scriptName);
 Process process = pb.start();
 Runtime.getRuntime().exec("gcc -o " + output + " " + source);
 ProcessBuilder pb = new ProcessBuilder("gcc", "-o", output, source);
 Process process = pb.start();
 Runtime.getRuntime().exec("perl " + scriptPath);
 ProcessBuilder pb = new ProcessBuilder("perl", scriptName);
 Process process = pb.start();


// 8. Insecure Deserialization:
ObjectInputStream ois = new ObjectInputStream(inputStream);
Object obj = ois.readObject();

// 9. Insecure File Upload:
FileItem fileItem = new DiskFileItemFactory().createItem(fieldName, contentType, isFormField, fileName);
