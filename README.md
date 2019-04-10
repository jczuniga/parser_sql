
SQL Parser using Natural Language Processing (NLP)
Machine Project: PROGLAN & Databases (CIS204M)

Requirements:
- Python2, PyPI('pip'), MySQL client for Python

Instructions:

1) Clone repository 
2) Install dependencies. Run 'pip install -r requirements.txt' from directory
3) Run main module from command line ('python main.py') - with GUI
4) For test cases, run test module ('test_terminal.py')

MySQL
Note: Nested Queries are not supported

Base Form
<code> SELECT (Columns names)* FROM (Table names)* </code>

WHERE Form
<code> SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] </code>

Average Form
<code> SELECT AVG( (Column name) )(Columns names)* FROM (Table names)*  </code>
<code> SELECT AVG( (Column name) )(Columns names)* FROM (Table names)* [WHERE [Conditions] ] ...  </code>


GROUP By Forms
<code> SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)] </code>
<code> SELECT (Columns names)* FROM (Table names)* [GROUP BY (Colmns name)] </code>

ORDER BY Forms
<code> SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [ORDER BY (Colmns name) (ASC/DESC)] </code>
<code> SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)] [ORDER BY (Colmns name) (ASC/DESC)] </code>

<code> SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)] [ORDER BY (Colmns name) (ASC/DESC)] </code>

Conditions

Col_name (> , =>, <, <=, =) value
Col_name (> , =>, <, <=, =) value (AND/OR) Col_name (> , =>, <, <=, =) value
Col_name LIKE value
Col_name IN (value, value, ...)


# SAMPLE TEST QUERIES #

What are the names of the countries with IDs of 2, 32, 14, 29?
Result : <code> SELECT (Name) FROM country WHERE ID IN (2,32, 14, 29) </code>

What are the countries in Africa?
Result : <code> SELECT * FROM country WHERE Continent='Africa' </code>

What is the average population of all the cities?
Result : <code> SELECT AVG(Population) FROM city </code>

How many countries are there?
Result : <code> SELECT COUNT(*) FROM city </code>

What is the minimum lifeexpectancy of countries with population of less than 500000?
Result : <code> SELECT MIN(LifeExpectancy) FROM country WHERE Population < 500000? </code>

What are the languages that are official?
Result : <code> SELECT * FROM countrylanguages WHERE IsOfficial='T' </code>

Which names of countries have an area greater than 230000?
Result : <code> SELECT (Name) FROM country WHERE SurfaceArea > 2300000 </code>

What are the names and codes of cities sorted by population from the least?
Result : <code> SELECT (Name), (Code) FROM city ORDER BY Population ASC </code>

Who is the leader of the country Philippines?
Result : <code> SELECT (HeadOfState) FROM country WHERE Name='Philippines' </code>

What is the capital of the country Argentina?
Result: <code> SELECT (Capital) From country WHERE Name='Argentina' </code>

Try each of the queries!
