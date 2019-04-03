import wikipedia, re, requests
from bs4 import BeautifulSoup


class wiki_page(object):
    ''' wiki page object'''

    def __init__(self, title):
        self.title = title
        self.artiles_list = wikipedia.search(self.title)
        self.page = wikipedia.page(self.artiles_list[0])
        self.html_doc = requests.get(self.page.url).text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')
        self.table_info = self.soup.find('table', class_=re.compile('infobox'))


    def get_legislatives_from_infobox(self):
        if not self.table_info:
            return []

        self.legisl_articles = [self.table_info.find('th', text=re.compile('Legislature')).parent.find('a').get('title')] if self.table_info.find('th', text=re.compile('Legislature')) else []
        # save to articles_list name of artilce Legislature

        self.tr_list = self.table_info.find('th', text=re.compile('Legislature')).parent.fetchNextSiblings() if self.table_info.find('th', text=re.compile('Legislature')) else []
        for tr in self.tr_list:
            if tr.attrs.has_key('class') and ('mergedrow' in tr.attrs['class'] or 'mergedbottomrow' in tr.attrs['class']) and 'mergedtoprow' not in tr.attrs['class']:
                # while exists attr CLASS and it equals (MERGEDROW or MERGEDBOTTOMROW ) and not equal mergedtoprow
                self.legisl_articles.append(tr.td.find('a').get('title'))
            else:
                #self.legisl_articles = [['Legists', val] for val in self.legisl_articles]
                return self.legisl_articles

        #self.legisl_articles = [['Legists', val] for val in self.legisl_articles]
        return self.legisl_articles


    def get_governors_from_infobox(self):
        if not self.table_info:
            return []

        self.govern_articles = []
        self.tr_list = self.table_info.find('th', text=re.compile('Government')).parent.fetchNextSiblings() if self.table_info.find('th', text=re.compile('Government')) else []

        for tr in self.tr_list[1:]:  # first tr is empty
            if tr.attrs.has_key('class') and ('mergedrow' in tr.attrs['class'] or 'mergedbottomrow' in tr.attrs['class']) and 'mergedtoprow' not in tr.attrs['class']:
                # WHILE exists attr CLASS and it equals (MERGEDROW or MERGEDBOTTOMROW ) and not equal mergedtoprow
                self.govern_articles.append(tr.th.find('a').get('title'))
            else:
                #self.govern_articles = [['Governors', val] for val in self.govern_articles]
                return self.govern_articles

        #self.govern_articles = [['Governors', val] for val in self.govern_articles]
        return self.govern_articles


    def get_parties_from_infobox(self):
        if not self.table_info:
            return []

        self.politics_articles=[]
        self.politics_tr = self.table_info.find('th', text=re.compile('olitical groups')).fetchParents('tr')[0] if self.table_info.find('th', text=re.compile('olitical groups')) else []
        # Take TR with words "Political groups" and find links in it
        if self.politics_tr:
            self.politics_articles = [val.get('title') for val in self.politics_tr.find_all('a')]

        return self.politics_articles

    def get_infobox_site_links(self):
        if not self.table_info:
            return []

        self.site_tag = self.table_info.find(text=re.compile('site'))  # find tag with word SITE
        self.site_links = []
        if self.site_tag:
            self.next_tr_tags = self.site_tag.fetchParents('tr')[0].fetchNextSiblings() + self.site_tag.fetchParents('tr')  # take TR parent for tag with word SITE and find external links in next TR tags
            self.external_links_tags = []
            for next_tr_tag in self.next_tr_tags:
                self.external_links_tags = self.external_links_tags + next_tr_tag.find_all('a', re.compile('external (text|free)'))
            for a in self.external_links_tags:
                self.site_links.append(a.text)

        self.site_links = [[self.title, val] for val in self.site_links]
        return self.site_links


    def get_external_links(self):
        self.ext_links = []
        self.External_links_Next_siblings = self.soup.find('span', id='External_links').parent.fetchNextSiblings() if self.soup.find('span', id='External_links') else []
        for tag in self.External_links_Next_siblings:
            for link_tag in tag.find_all('a', class_='external text'):
                self.ext_links.append([link_tag.text + ' (' + self.page.title + ')', link_tag.get('href')])

        return self.ext_links

