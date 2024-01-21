// ## bufferOverflowExample1

char dest[100];
char src[] = "Hello, World!";
strcpy(dest, src);

char buffer[256];
const char* input = "Copy this!";
strcpy(buffer, input);

char destination[50];
const char* source = "Example String";
strcpy(destination, source);

char destinationArray[100];
const char* sourceString = "Copying data";
strcpy(destinationArray, sourceString);

char target[20];
const char* sourceData = "Test String";
strcpy(target, sourceData);

char bufferString[30];
const char* inputString = "Buffer Overflow";
strcpy(bufferString, inputString);

char result[50];
const char* inputText = "Copy me!";
strcpy(result, inputText);

char output[200];
const char* inputMessage = "Long message to copy";
strcpy(output, inputMessage);

char destBuffer[50];
const char* srcText = "Buffer Copy";
strcpy(destBuffer, srcText);

char destinationString[100];
const char* sourceValue = "Secure Copy";
strcpy(destinationString, sourceValue);

// ### bufferOverflowExample2
char buffer[100];
gets(buffer);

char input[256];
gets(input);

char data[50];
gets(data);

char userInput[200];
gets(userInput);

char text[30];
gets(text);

char inputString[100];
gets(inputString);

char outputBuffer[80];
gets(outputBuffer);

char inputBuffer[150];
gets(inputBuffer);

char userText[120];
gets(userText);

char inputArray[200];
gets(inputArray);

// ### bufferOverflowExample7

char dest1[50];
char src1[] = "Source Data";
memcpy(dest1, src1, sizeof(src1));

char dest2[100];
const char* src2 = "Copy this content";
memcpy(dest2, src2, strlen(src2) + 1);

int dest3[10];
int src3[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
memcpy(dest3, src3, sizeof(src3));

float dest4[20];
float src4[20] = {1.1, 2.2, 3.3, 4.4, 5.5};
memcpy(dest4, src4, sizeof(src4));

char dest5[30];
const char* src5 = "Copy me!";
memcpy(dest5, src5, strlen(src5));

double dest6[5];
double src6[5] = {0.1, 0.2, 0.3, 0.4, 0.5};
memcpy(dest6, src6, sizeof(src6));

struct Data {
    int x;
    double y;
};

Data dest7;
Data src7 = {42, 3.14};
memcpy(&dest7, &src7, sizeof(Data));

char dest8[25];
char src8[] = "Memory Copy Example";
memcpy(dest8, src8, sizeof(src8));

int dest9[5][5];
int src9[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}};
memcpy(dest9, src9, sizeof(src9));

unsigned char dest10[100];
unsigned char src10[100];
memset(src10, 0x41, sizeof(src10));
memcpy(dest10, src10, sizeof(src10));


// ### bufferOverflowExample7
char dest1[50];
char src1[] = "Source Data";
memcpy(dest1, src1, sizeof(src1));

char dest2[100];
const char* src2 = "Copy this content";
memcpy(dest2, src2, strlen(src2) + 1);

int dest3[10];
int src3[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
memcpy(dest3, src3, sizeof(src3));

float dest4[20];
float src4[20] = {1.1, 2.2, 3.3, 4.4, 5.5};
memcpy(dest4, src4, sizeof(src4));

char dest5[30];
const char* src5 = "Copy me!";
memcpy(dest5, src5, strlen(src5));

double dest6[5];
double src6[5] = {0.1, 0.2, 0.3, 0.4, 0.5};
memcpy(dest6, src6, sizeof(src6));

struct Data {
    int x;
    double y;
};

Data dest7;
Data src7 = {42, 3.14};
memcpy(&dest7, &src7, sizeof(Data));

char dest8[25];
char src8[] = "Memory Copy Example";
memcpy(dest8, src8, sizeof(src8));

int dest9[5][5];
int src9[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}};
memcpy(dest9, src9, sizeof(src9));

unsigned char dest10[100];
unsigned char src10[100];
memset(src10, 0x41, sizeof(src10));
memcpy(dest10, src10, sizeof(src10));

char dest1[50] = "Hello, ";
const char* src1 = "World!";
strcat(dest1, src1);

char dest2[100];
const char* src2 = "Concatenate ";
strcat(dest2, src2);

char dest3[20] = "123";
const char* src3 = "456";
strcat(dest3, src3);

char dest4[30];
const char* src4 = "Append me!";
strcat(dest4, src4);

char dest5[40] = "Initial ";
const char* src5 = "String";
strcat(dest5, src5);

char dest6[15] = "ABC";
const char* src6 = "DEF";
strcat(dest6, src6);

char dest7[50] = "Copy ";
const char* src7 = "This";
strcat(dest7, src7);

char dest8[25] = "Old ";
const char* src8 = "New";
strcat(dest8, src8);

char dest9[10] = "Concat";
const char* src9 = "enate";
strcat(dest9, src9);

char dest10[60] = "Programming";
const char* src10 = " is fun!";
strcat(dest10, src10);


// ### sqlInjectionExample2

std::string sqlQuery1 = "SELECT * FROM table1";
query(sqlQuery1);

const char* sqlQuery2 = "UPDATE users SET password = 'newpass' WHERE id = 123";
query(sqlQuery2);

std::string sqlCommand3 = "DELETE FROM records WHERE status = 'expired'";
query(sqlCommand3);

const char* sqlCommand4 = "INSERT INTO products (name, price) VALUES ('Product A', 19.99)";
query(sqlCommand4);

std::string dbQuery5 = "SELECT username FROM users WHERE age > 18";
query(dbQuery5);

const char* dbCommand6 = "UPDATE orders SET shipped = true WHERE order_id = 456";
query(dbCommand6);

std::string sqlStatement7 = "INSERT INTO logs (message) VALUES ('New log entry')";
query(sqlStatement7);

const char* sqlCommand8 = "DELETE FROM customers WHERE last_purchase_date < '2022-01-01'";
query(sqlCommand8);

std::string dbQuery9 = "SELECT * FROM transactions WHERE amount > 1000";
query(dbQuery9);

const char* sqlCommand10 = "UPDATE employees SET salary = salary * 1.1 WHERE department = 'Sales'";
query(sqlCommand10);


// 

runDynamicQuery("SELECT * FROM employees WHERE department = 'IT'");

std::string dynamicSql1 = "UPDATE products SET stock = stock - 1 WHERE id = 123";
runDynamicQuery(dynamicSql1);

const char* dynamicQuery2 = "DELETE FROM tasks WHERE status = 'completed'";
runDynamicQuery(dynamicQuery2);

std::string sqlCommand3 = "INSERT INTO logs (event) VALUES ('New event')";
runDynamicQuery(sqlCommand3);

const char* dynamicCommand4 = "UPDATE customers SET points = points + 10 WHERE id = 456";
runDynamicQuery(dynamicCommand4);

runDynamicQuery("SELECT * FROM orders WHERE total_price > 1000");

std::string dbStatement5 = "INSERT INTO messages (content) VALUES ('Hello, World')";
runDynamicQuery(dbStatement5);

const char* sqlQuery6 = "UPDATE inventory SET quantity = quantity - 5 WHERE product_id = 789";
runDynamicQuery(sqlQuery6);

std::string dynamicSql7 = "DELETE FROM users WHERE last_login_date < '2022-01-01'";
runDynamicQuery(dynamicSql7);

const char* dbQuery8 = "SELECT * FROM transactions WHERE amount > 500";
runDynamicQuery(dbQuery8);
