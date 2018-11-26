#!/usr/bin/python3

import psycopg2


def busqueda(pregunta, titulo, unidad):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute("select * from "+pregunta)
    results = cursor.fetchall()
    formated_results = "\n".join(
        [str(result[0])+" - "+str(result[1])+unidad for result in results])
    print("\n"+(titulo))
    print(formated_results)
    conn.close()


get_popular_articles = busqueda(
    'question1', 'Most popular articles: ', ' views')
get_popular_authors = busqueda(
    'question2', 'Most popular authors: ', ' views')
get_buggy_days = busqueda(
    'question3', 'Buggy days: ', ' errors')
