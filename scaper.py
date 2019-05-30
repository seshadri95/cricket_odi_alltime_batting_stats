import bs4 as bs
import urllib.request
import scraping.get_player_data as get_player_stat
import re

def get_html(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'html.parser')
    return soup


country_code = ['AFG','AUS','BAN','BER','CAN','EAF','ENG','HOK','IND','IRE','KEN','NAM','NEP','NED','NZL','OMA','PAK','PNG','SCO','SAF','SRL','UAE','USA','WIN','ZIM']
asp_name ='http://howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country='

class scrapering_result:
    def __init__(self):
        self.final_data_set = {}
        self.exception_ids = []
        for country in country_code:
            print('Crawling player data belonging to country :'+ country)
            soup = get_html(asp_name+country)
            uniq_player_ids = []
            for link in soup.findAll('a'):
                hrf = link.get('href')
                if 'PlayerID' in str(hrf) and 'ODI' in str(hrf):
                    uniq_player_id= re.findall('PlayerID=(.+)',hrf)
                    uniq_player_ids.append(uniq_player_id[0])
            for id in set(uniq_player_ids):
                try:
                    player_name,stats = get_player_stat.get_batting_stat(id,country)
                    self.final_data_set[player_name] = stats
                except:
                    print('unable to scrap stats for player id ' + id)
                    self.exception_ids.append(id)
    def get_total_dataset(self):
        return self.final_data_set

if __name__ == '__main__':
    obj =scrapering_result()
    print(obj.get_total_dataset())
