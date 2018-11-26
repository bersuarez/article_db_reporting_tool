# Project_reporting_tool
Project_reporting_tool is a set of queries to a newspaper database that helps discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. 
## Preparation / installation
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze. For help, follow this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/4dcefa2a-fb54-4909-9708-9ef2839e5340/modules/5dbcf44d-760d-49d4-9055-b6a0a48e5454/lessons/3967218625/concepts/39636486110923) (you might need to pay for the course)

### The virtual machine
This project makes use of a Linux-based virtual machine (VM)

This will give you the PostgreSQL database and support software needed to run the code. If you have used an older version of this VM, you may need to install it into a new directory.

To bring the virtual machine online, use `vagrant up`. Then log into it with `vagrant ssh`.

### Download the data
Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. 

To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

`psql` — the PostgreSQL command line program
`-d news` — connect to the database named news which has been set up for you
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

Connecting from your code
The database that you're working with in this project is running PostgreSQL. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

`db = psycopg2.connect("dbname=news")``

This might need previous installation: 

`sudo pip3 install psycog2`

## Usage
The queries for analyzing the data have already been established and put into three views: 'question1', 'question2', and 'question3' which will have to be recreated as instructed next:
#### Views recreation
##### First query: pregunta1
###### Purpose:
This query answers the following question: 
- What are the most popular three articles of all time? 
- Which articles have been accessed the most?
###### Query code: 
`create view question1 as 
select '"'||articles.title||'"' as title, count(*) as views
    from articles, log 
    where log.path like '%'||articles.slug||'%' 
    group by articles.title 
    order by views desc
    limit 3;`
###### Resulting table:
The resulting table will include the title of the top articles (text) and the number of views it has (integer)
##### Second query: pregunta2
###### Purpose:
This query informs the user about:
- Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views?
###### Query code: 
`create view question2 as 
select authors.name as author, count (*) as views 
    from articles, authors, log 
    where authors.id::text=articles.author::text 
    and log.path like '%'||articles.slug||'%' 
    group by authors.name 
    order by views desc;`
###### Resulting table:
The resulting table will include the name of the author (text) and the number of times it was searched (integer)
##### Third query: pregunta3
###### Purpose:
This query informs the user about:
- On which days did more than 1% of requests lead to errors?
###### Query code: 
`create view question3 as 
select to_char(to_date(tabla1.fecha::text,'YYYY-MM-DD'),'Mon DD YYYY'), round(100.0*tabla1.errores/tabla2.totales,1)||'%' as porcentajes
    from (select time::date as fecha, count(*) as errores
        from log where status!='200 OK'
        group by time::date)
        as tabla1
    join (select log.time::date as fecha, count (*) as totales
        from log group by log.time::date)
        as tabla2
    on tabla1.fecha=tabla2.fecha where 100.0*tabla1.errores/tabla2.totales>1;
###### Resulting table:
The resulting table will include the date (date) and the percentage of errors (float)
#### Accesing the views
Once the views are recreated, running the reporting_tool.py will execute the queries and data will be delivered as text. 
## FAQs
jk, no one has seen this
## License
MIT License

Copyright (c) 2018 Bernardo Suárez Sepúlveda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.