import wikipedia, bs4, parse_wiki_page, requests

page = wikipedia.page('List_of_intelligence_agencies')
html_doc = requests.get(page.url).text
soup = bs4.BeautifulSoup(html_doc, 'html.parser')
main_div = soup.find('div', class_='mw-parser-output')


link_list=[]
h3_list = main_div.find_all('h3')

for h3 in h3_list:
    country = h3.find('span').get('id').encode('utf-8')
    ul = h3.fetchNextSiblings('ul')[0]
    print country
    this_link_list = []
    for a in ul.find_all('a'):
        title = a.get('title')
        print title
        if not title:
            title = a.text.encode('utf-8')

        try:
            page = parse_wiki_page.wiki_page(title)
        except:
            continue
        site_links = page.get_infobox_site_links()
        ext_links = page.get_external_links()
        this_link_list = this_link_list + site_links + ext_links

    link_list.append([country, this_link_list])


    with open('/home/user1/PycharmProjects/Intelligence_ORGS.txt', 'ab') as f:
        f.write(country+'\t')
        f.write(str(this_link_list)+'\n')




