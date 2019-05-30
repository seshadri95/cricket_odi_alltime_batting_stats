import re
import urllib.request
import bs4 as bs

#Below code is customised based on html code in http://howstat.com



def  get_batting_stat(id,country):

    source = urllib.request.urlopen('http://howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID='+id).read()
    soup = bs.BeautifulSoup(source, 'html.parser')


    # Extracting html data data only for batting
    table = soup.find("div", attrs={"id":"bat"}).find("table", attrs={"class":"TableLined"})

    # The first tr contains the field names.
    headings = [th.get_text().strip() for th in table.find("tr").find_all("td")]
    headings.append('country')
    # Extracting player name from html title
    player_name = (re.findall("-(.+)-",str(soup.title)))[0].strip()

    year_wise_batting_stats  = []
    for row in table.find_all("tr")[1:]:
        values = [td.get_text().strip() for td in row.find_all("td")]
        values.append(country)
        dataset = dict(zip(headings,values))
        year_wise_batting_stats.append(dataset)

    return player_name,year_wise_batting_stats




