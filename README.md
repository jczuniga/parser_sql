
SQL Parser using Natural Language Processing (NLP)
Machine Project: PROGLAN & Databases (CIS204M)

Requirements:
- Python2, PyPI('pip'), MySQL client for Python

Instructions:

1) Clone repository 
2) Install dependencies. Run 'pip install -r requirements.txt' from directory
3) Run main module from command line ('python main.py') - with GUI
4) For test cases, run test module ('test_terminal.py')

## MySQL
## Note: Nested Queries are not supported

## Base Form
# SELECT (Columns names)* FROM (Table names)*

## WHERE Form
# SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ]

## Average Form
# SELECT AVG( (Column name) )(Columns names)* FROM (Table names)*
# SELECT AVG( (Column name) )(Columns names)* FROM (Table names)* [WHERE [Conditions] ] ...


## GROUP By Forms
# SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)]
# SELECT (Columns names)* FROM (Table names)* [GROUP BY (Colmns name)]

## ORDER BY Forms
# SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [ORDER BY (Colmns name) (ASC/DESC)]
# SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)] [ORDER BY (Colmns name) (ASC/DESC)]

# SELECT (Columns names)* FROM (Table names)* [WHERE [Conditions] ] [GROUP BY (Colmns name)] [ORDER BY (Colmns name) (ASC/DESC)]

###############################
### Conditions

# Col_name (> , =>, <, <=, =) value
# Col_name (> , =>, <, <=, =) value (AND/OR) Col_name (> , =>, <, <=, =) value

#  Col_name LIKE value

#  Col_name IN (value, value, ...)


### SAMPLE TEST QUERIES ###
# What are the names of the countries with IDs of 2, 32, 14, 29?
Result : SELECT (Name) FROM country WHERE ID IN (2,32, 14, 29)

# What are the countries in Africa?
Result : SELECT * FROM country WHERE Continent='Africa'

# What is the average population of all the cities?
Result : SELECT AVG(Population) FROM city

# How many countries are there?
Result : SELECT COUNT(*) FROM city

# What is the minimum lifeexpectancy of countries with population of less than 500000?
Result : SELECT MIN(LifeExpectancy) FROM country WHERE Population < 500000?

# What are the languages that are official?
SELECT * FROM countrylanguages WHERE IsOfficial='T'

# Which names of countries have an area greater than 230000?
SELECT (Name) FROM country WHERE SurfaceArea > 2300000

# What are the names and codes of cities sorted by population from the least?
SELECT (Name), (Code) FROM city ORDER BY Population ASC

# Who is the leader of the country Philippines?
SELECT (HeadOfState) FROM country WHERE Name='Philippines'

# What is the capital of the country Argentina?
SELECT (Capital) From country WHERE Name='Argentina'

Try each of the queries!