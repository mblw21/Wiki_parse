from parse_wiki_page import *

def main():
    country_word = 'Slovakia'
    #soup = bs4.BeautifulSoup(wikipedia.requests.get(wikipedia.page('Kazakhstan').url).text, 'html.parser')

    Page = wiki_page(country_word)
    print 'Reseive wiki_page object'

    ext_links_list = Page.get_external_links()
    print 'EXTERN Links: ', ext_links_list


    official_sites_list = Page.get_infobox_site_links()
    print 'Official Sites: ', official_sites_list

    res_list = ext_links_list + official_sites_list


    governors_articles  = Page.get_governors_from_infobox()
    print 'GOVERNORS: ', governors_articles
    for gov_title in governors_articles:
        gov_page = wiki_page(gov_title)
        res_list =  gov_page.get_external_links() + gov_page.get_infobox_site_links()


    legist_articles     = Page.get_legislatives_from_infobox()
    for legist_name in legist_articles:
        parties_list = []
        print 'legist_page: ', legist_name
        legist_page = wiki_page(legist_name)
        res_list = res_list + legist_page.get_external_links() + legist_page.get_infobox_site_links()
        parties_list = legist_page.get_parties_from_infobox()
        print parties_list

        for party_title in parties_list:
            if not party_title:
                continue
            print 'party: ' , party_title
            party_page = wiki_page(party_title)
            party_site_links = [ [title + '(party)', link] for title, link in  party_page.get_infobox_site_links()]
            party_ext_links = [[title + '(party)', link] for title, link in party_page.get_external_links()]

            res_list = res_list + party_ext_links + party_site_links


    print('this is main')

    with open('/home/user1/PycharmProjects/SK/1.txt', 'wb') as f:
        for title, link in res_list:
            print 'title: ' , title, 'link: ', link
            f.write(title.encode('utf-8')+'\t')
            f.write(link.encode('utf-8')+'\n')
    return res_list

def parse_wiki_lists():
    wiki_page_titles=[ 'Ministry of Agriculture',
                      'Ministry of Education', 'Ministry of Finance', 'Ministry of Health', 'Ministry of Immigration', 'Ministry of Industry',
                      'Ministry of Information', 'Ministry of Interior', 'International development ministry',
                      'List of environmental ministries', 'List of forestry ministries', 'List of health departments and ministries',
                      'List of ministries of climate change', 'List of ministries of communications', 'List of public works ministries',
                      'Ministry of Labor', 'Ministry of Defence', 'Ministry of Energy',  'Ministry of Foreign Affairs',
                      'Ministry of Home Affairs', 'Ministry of Justice', 'Ministry of Petroleum', 'Ministry of Religious Affairs',
                      'Ministry of Science', 'Ministry of Sports', 'Ministry of Statistics', 'Ministry of Trade and Industry', 'Ministry of Transport',
                      'Office of the President (disambiguation)', 'Prime minister', 'Ministry of Sports', 'Ministry of Tourism']
    # copy wiki_page_titles = ['Cabinet department', 'Ministry of Culture', 'Deputy prime minister',      'Ministry of Agriculture',   'Ministry of Statistics and Programme Implementation',      'Ministry of Education', 'Ministry of Finance', 'Ministry of Health', 'Ministry of Immigration',                        'Ministry of Industry',                        'Ministry of Information', 'Ministry of Interior', 'International development ministry',                        'List of agriculture ministries',                        'List of current finance ministries', 'List of current interior ministries',                        'List of education ministries',                        'List of environmental ministries', 'List of forestry ministries',                        'List of health departments and ministries',                        'List of ministries of climate change', 'List of ministries of communications',                        'List of public works ministries',                        'Ministry of Labour', 'Ministry of Defence', 'Ministry of Energy', 'Ministry of Finance',                        'Ministry of Foreign Affairs',                        'Ministry of Home Affairs', 'Ministry of Justice', 'Ministry of Labor', 'Ministry of Petroleum',                        'Ministry of Religious Affairs',                        'Ministry of Science', 'Ministry of Sports', 'Ministry of Trade and Industry',                        'Ministry of Transport',                        'Office of the President (disambiguation)', 'Prime minister', 'Ministry of Sports',                        'Ministry of Tourism']

    for title in wiki_page_titles:
        res_links = []
        print 'ATTENTION!!!', title
        Page = wiki_page(title)
        links_list = Page.page.links
        #links_list = links_list[70:]
        for link_title in links_list :
            print link_title
            if link_title in wiki_page_titles or link_title == 'Minister for Fisheries (Western Australia)' or link_title == 'Ministry for Rural Affairs (Sweden)':
                print '\t\t\tpass'
                continue
            try:
                page_link = wiki_page(link_title)
            except:
                continue
            res_links = res_links + page_link.get_infobox_site_links() + page_link.get_external_links()

        with open('/home/user1/PycharmProjects/88/all_ministries.txt', 'ab') as f:
            for title_link, link in res_links:
                #print 'title: ' , title, 'link: ', link
                f.write(title.encode('utf-8') + '\t')
                f.write(title_link.encode('utf-8')+'\t')
                f.write(link.encode('utf-8')+'\n')


def parse_wiki_lists_2():
    wiki_page_titles=[ 'Ministry of Agriculture',
                      'Ministry of Education', 'Ministry of Finance', 'Ministry of Health', 'Ministry of Immigration', 'Ministry of Industry',
                      'Ministry of Interior', 'International development ministry',
                      'List of environmental ministries', 'List of forestry ministries', 'List of health departments and ministries',
                      'List of ministries of climate change', 'List of ministries of communications','List of public works ministries',
                      'Ministry of Labor', 'Ministry of Defence', 'Ministry of Energy',  'Ministry of Foreign Affairs',
                      'Ministry of Home Affairs', 'Ministry of Justice', 'Ministry of Petroleum', 'Ministry of Religious Affairs',
                      'Ministry of Science', 'Ministry of Sports', 'Ministry of Trade and Industry', 'Ministry of Transport',
                       'list of presidents', 'Prime minister', 'Ministry of Tourism']
    # copy wiki_page_titles = ['Cabinet department', 'Ministry of Culture', 'Deputy prime minister',      'Ministry of Agriculture',   'Ministry of Statistics and Programme Implementation',      'Ministry of Education', 'Ministry of Finance', 'Ministry of Health', 'Ministry of Immigration',                        'Ministry of Industry',                        'Ministry of Information', 'Ministry of Interior', 'International development ministry',                        'List of agriculture ministries',                        'List of current finance ministries', 'List of current interior ministries',                        'List of education ministries',                        'List of environmental ministries', 'List of forestry ministries',                        'List of health departments and ministries',                        'List of ministries of climate change', 'List of ministries of communications',                        'List of public works ministries',                        'Ministry of Labour', 'Ministry of Defence', 'Ministry of Energy', 'Ministry of Finance',                        'Ministry of Foreign Affairs',                        'Ministry of Home Affairs', 'Ministry of Justice', 'Ministry of Labor', 'Ministry of Petroleum',                        'Ministry of Religious Affairs',                        'Ministry of Science', 'Ministry of Sports', 'Ministry of Trade and Industry',                        'Ministry of Transport',                        'Office of the President (disambiguation)', 'Prime minister', 'Ministry of Sports',                        'Ministry of Tourism']

    links_list=[]


    for title in wiki_page_titles:
        print 'ATTENTION!!!', title
        Page = wiki_page(title)
        links_list = links_list + Page.page.links
        print 'LIST LEN:', len(links_list)
        #links_list = links_list[70:]

    links_list = list(set(links_list))
    links_list.sort()
    print 'LIST LEN:', len(links_list)

    with open('/home/user1/PycharmProjects/88/links_list.txt', 'wb') as f:
        for i in links_list:
            f.write(i.encode('utf-8') + '\n')

    print 'Write file DONE'

    for link_title in links_list :
        print link_title

        if link_title in wiki_page_titles or link_title == 'Minister for Fisheries (Western Australia)' or link_title == 'Ministry for Rural Affairs (Sweden)':
            print '\t\t\tpass'
            continue
        try:
            page_link = wiki_page(link_title)
        except:
            continue
        res_links = page_link.get_infobox_site_links() + page_link.get_external_links()

        with open('/home/user1/PycharmProjects/88/all_ministries_2.txt', 'ab') as f:
            for title_link, link in res_links:
                #print 'title: ' , title, 'link: ', link
                f.write(title_link.encode('utf-8')+'\t')
                f.write(link.encode('utf-8')+'\n')
        print link_title , ' Done'


if __name__ == '__main__':
    #parse_wiki_lists_2()
    main()

