import psycopg2

#1
select '"'||articles.title||'"' as title, count(*) as views
    from articles, log 
    where log.path like '%'||articles.slug||'%' 
    group by articles.title 
    order by views desc
    limit 3;

#2
select authors.name as author, count (*) as views 
    from articles, authors, log 
    where authors.id::text=articles.author::text 
    and log.path like '%'||articles.slug||'%' 
    group by authors.name 
    order by views desc;


#3
#tabla errores con fechas (31 rows):
select time::date, errores from (select time::date, count(*) as errores from log where status!='200 OK' group by time::date) as subq;
#tabla totales con fechas (31 queries):
select log.time::date, count (*) from log group by log.time::date;
#se puede hacer operaciones entre valores de diferentes tablas
select articles.author/authors.id from articles, authors;
#join las tablas y queda fecha, errores, totales
select tabla1.fecha,tabla1.errores,tabla2.totales from (select time::date as fecha, count(*) as errores from log where status!='200 OK' group by time::date) as tabla1 join (select log.time::date as fecha, count (*) as totales from log group by log.time::date)as tabla2 on tabla1.fecha=tabla2.fecha;
#respuesta: (falta filtrar porcentajes>1):
select tabla1.fecha,tabla1.errores, tabla2.totales, 100.0*tabla1.errores/tabla2.totales as porcentajes from (select time::date as fecha, count(*) as errores from log where status!='200 OK' group by time::date) as tabla1 join (select log.time::date as fecha, count (*) as totales from log group by log.time::date) as tabla2 on tabla1.fecha=tabla2.fecha;

create view pregunta3 as select to_char(to_date(tabla1.fecha::text,'YYYY-MM-DD'),'Mon DD YYYY'), round(100.0*tabla1.errores/tabla2.totales,1)||'%' as porcentajes
    from (select time::date as fecha, count(*) as errores
        from log where status!='200 OK'
        group by time::date)
        as tabla1
    join (select log.time::date as fecha, count (*) as totales
        from log group by log.time::date)
        as tabla2
    on tabla1.fecha=tabla2.fecha where 100.0*tabla1.errores/tabla2.totales>1;


def get_popular_articles():
  db = psycopg2.connect(database=)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close(
  return posts

def get_popular_authors():
  db = psycopg2.connect(database=)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts

def get_buggy_days():
  db = psycopg2.connect(database=)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts

   