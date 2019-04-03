import wikipedia, bs4, parse_wiki_page, requests

with open('/home/user1/PycharmProjects/top_100_vpk.txt', 'rb') as f1:
    data = f1.readlines()

orgs_list=[]
for org in data:
    print org
    page = parse_wiki_page.wiki_page(org[:-1].replace('\t',' '))
    site_links = page.get_infobox_site_links()
    ext_links = page.get_external_links()
    this_link_list = site_links + ext_links

    #link_list.append([org[:-1].replace('\t',' ')+'\t', this_link_list])

    with open('/home/user1/PycharmProjects/top_100_export.txt', 'ab') as f:
        for name, link in this_link_list:
            f.write(org[:-1].replace('\t',' ')+'\t')
            f.write(name.encode('utf-8') + '\t' + link.encode('utf-8') +'\n')


