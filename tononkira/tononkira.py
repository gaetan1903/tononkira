import requests
from bs4 import BeautifulSoup


class Tononkira:
    '''
        Have the lyrics of Malagasy songs
    '''

    url: str = 'https://tononkira.serasera.org/tononkira'


    def scrap_list(self, data):
        res_value = []
        res = data.tbody.find_all('tr')
        for value in res:
            val = value.find_all('td')
            res_value.append({
                    'title' : val[1].text,
                    'artist' : val[2].text,
                    'url' : val[1].a['href'],
                }
            )
        return res_value


    def search(self, query: str) -> list:
        '''
            Search a song in tononkira serasera
        '''
        res_value = []

        rp = requests.post(self.url + '/hira/results', data={'filter[tadiavo]': query})

        soup = BeautifulSoup(rp.text, 'html.parser')
        tb = soup.find('table', class_='list')
        if not tb:
            return res_value

        return self.scrap_list(tb)


    def search_by(self, title='', artist='', lyrics='') -> str:
        '''
            Search a song by title and artist
        '''
        res_value = []
        if title == '' and artist == '' and lyrics == '':
            return res_value

        rp = requests.get(
            self.url, 
            params={
                'lohateny_like': 'on', 'lohateny': title, 
                'anarana_like': 'on', 'anarana': artist, 
                'submit': 'form_tadiavo', 'hira': lyrics
            }
        )

        
        soup = BeautifulSoup(rp.text, 'html.parser')
        tb = soup.find('table', class_='list')

        if not tb:
            return res_value

        return self.scrap_list(tb)


    def fetch(self, url: str) -> str:
        '''
            Fecth a lyrics song with url
        '''

        rp = requests.get(url)
        soup = BeautifulSoup(rp.text, 'html.parser')

        text = []
        head = soup.find('h1')
        for val in soup.find("div", {"class": "adminbox"}).next_siblings:
            if val.name == 'div': 
                break
            if val.string is None: 
                continue
            
            text.append(val.string.replace('tononkira.serasera.org',''))
        
        return head.text + '\n-------------\n\n' +  ' '.join(text).strip()


    def get(self, query: str) -> str:
        ''' 
            Get directly a song by best match
        '''
        res = self.search(query)
        if res:
            return self.fetch(res[0]['url'])
        return ''

