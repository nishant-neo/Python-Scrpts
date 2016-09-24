#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NISHANT
#
# Created:     02-04-2015
# Copyright:   (c) NISHANT 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from lxml import html
import requests
f = open( "output.txt", "w" )
def scrapcast(link):
    """
    The function follows the link of a movie and scrapes the cast from the page of
    the movie.
    """
    k = link.rfind("/")
    link = link[:k] + '/fullcredits?ref_=tt_ov_st_sm'
    page = requests.get(link)
    tree = html.fromstring(page.text)
    cast = tree.xpath('//*[@id="fullcredits_content"]/table[3]/tr/td[2]/a/span/text()')#|//*[@id="fullcredits_content"]/table[3]/tr/td[4]/div/text()')

    f.write('***************CAST*****************\n\n')
    for i in cast:
        try:
            f.write(str(i)+'\n')
        except:
            pass

    f.write('\n\n')
    #f.close()


def scrapmovie(link,n):
    """
    This function scrapes out the name of the ith movie from the list of movie
    and then calls scrapcast(link) to scrape the cast.
    """
    page = requests.get(link)
    tree = html.fromstring(page.text)
    xp1 = '//*[@id="main"]/div/div[2]/table/tbody/tr[%d]/td[2]/a/text()' %n
    xp2 = '//*[@id="main"]/div/div[2]/table/tbody/tr[%d]/td[2]/a/@href' %n
    movie_name = tree.xpath(xp1)
    try:
        mvi=str(movie_name[0])
    except:
        pass
    links = tree.xpath(xp2)
    link = 'http://www.imdb.com' + links[0]

    f.write("*********MOVIE***********\n\n")
    f.write(mvi+'\n\n')
    scrapcast(link)


def scrapmovies(link,n):
    """
    This function is provided with n the number of movies to be scraped from the boxoffice
    page of the IMDB website. The initiates everything and saves to "output.txt"

    """
    for i in range(1,n+1):
        scrapmovie(link,i)

response = input("Please enter the number of movies to be scraped : ")
scrapmovies('http://www.imdb.com/chart/top?ref_=cht_ql_2',int(response))
f.close()

