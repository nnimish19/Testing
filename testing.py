local master changes in line 1
#
# author: nimish 
#
#small change!
import urllib2
from bs4 import BeautifulSoup
from urlparse import urljoin

#soup=BeautifulSoup("<p>Some<b>bad<i>HTML</p>  <p>haha</p>   <p>.</p> haha")      
#print soup      #print soup('p')      #print soup.prettify()       #print soup.contents         #print '\n\n\n'

wi = [[x for x in range(1,10)] for y in range(11,20)]   #Read like wi = [[] for y in range(11,20)]      [ [], [], []... ]   <- 2Darray
wi = [x for y in range(11,20) for x in range(1,10)]     #<- single list. 1D array
print wi

c=urllib2.urlopen('http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm')

#remote origin master changed line in middle

#print c.read()
soup=BeautifulSoup('<a href="/guidadfaes/">Tutorials</a>')             #"<p><i>helo</i></p>"  "<p>Some<b>bad<i>HTML</p>  <p>haha</p>   <p>.</p> haha"
#soup=BeautifulSoup(c.read( ))
page='http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm'
links=soup('a')
print links
for l in links:
    print l
    print l['href']
    print l.attrs
for link in links:
    if ('href' in dict(link.attrs)):
        url=urljoin(page,link['href'])      #urljoin('s1','s2') = #http://domain_name_of_s1_(xyz.com)/s2
        print url                                                                       
        if url.find("'")!=-1: continue
        url=url.split('#')[0] # remove location portion

#print links

#if 'href' in dict(links.attrs):
    #print 23
    
# remote/origin master last line changed
# change again


