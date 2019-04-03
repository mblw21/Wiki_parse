import wikipedia, bs4, parse_wiki_page, requests

page = wikipedia.page('List_of_major_arms_industry_corporations_by_country')
html_doc = requests.get(page.url).text
soup = bs4.BeautifulSoup(html_doc, 'html.parser')
tab = soup.find('table', class_='wikitable sortable')


link_list=[]
trs = tab.find_all('tr')[1:]
for tr in trs:
    this_link_list = []
    a_list = tr.find_all('a')
    country = a_list[0].text.encode('utf-8')
    print country
    for a in a_list[1:]:
        title = a.get('title')
        print title
        if not title:
            title = a.text.encode('utf-8')
            link = a.get('href')
            if title and link:
                this_link_list.append([title, link])
                print title
            else:
                continue

        try:
            page = parse_wiki_page.wiki_page(title)
        except:
            continue
        site_links = page.get_infobox_site_links()
        ext_links = page.get_external_links()
        this_link_list = this_link_list + site_links + ext_links

    link_list.append([country, this_link_list])


    with open('/home/user1/PycharmProjects/88/VPK_ORGS.txt', 'ab') as f:
        f.write(country+'\t')
        f.write(str(this_link_list)+'\n')




