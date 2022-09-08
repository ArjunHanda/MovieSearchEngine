from django.shortcuts import render
import urllib.request as url
import bs4

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    name1 = request.GET['your_name']
    name1 = "+".join(name1.split())    

    path1 = f"https://www.imdb.com/find?q={name1}&ref_=nv_sr_sm"
    response = url.urlopen(path1)
    page = bs4.BeautifulSoup(response, features="html.parser")
    movie_name = page.find('td', class_='result_text')
    movie_link = movie_name.find('a').get('href')
    path2 = (f"https://www.imdb.com{movie_link}?ref_=fn_al_tt_1")
    movie_link2 = url.urlopen(path2)
    page2 = bs4.BeautifulSoup(movie_link2, features="html.parser")
    title = page2.find('h1')
    rating = page2.find('span',{'class':'sc-7ab21ed2-1 jGRxWM'})
    summary = page2.find('span',{'class':'sc-16ede01-2 gXUyNh'})
    #movie_suggestions_code = page.find('dev',class_='ipc-poster-card ipc-poster-card--base ipc-poster-card--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2')
    #print(movie_suggestions_code)
    #movie_suggestions = movie_suggestions_code.find('a')
    #print("Title: "+title.text)
    #print("Rating: "+rating.text)
    #print("Summary: "+summary.text)
    results = [title.text,rating.text,summary.text]
    
    #print("More Like This: "+movie_suggestions
    
    return render(request, 'search.html', {'searchresults':results})

    