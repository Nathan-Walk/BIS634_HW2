import requests
import xml.etree.ElementTree as ET
import time

if __name__ == "__main__":
    pmid = 20725509
else:
    print("Importing Nathan's module...you will need to set the pmid.")
# pmid = 20725509
# url1 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=\
# pubmed&retmode=xml&id={pmid}"
# #  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=20725509
# url2 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id={pmid}"
# # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id=20725509&id=20725509
# url_auth= f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=\
# pubmed&retmode=xml&rettype=abstract&id={pmid}"



list_desc=[]
author_total={}

###use this for???
# def get_info(pmid):
#     content = requests.get(url).text
#     root = ET.fromstring(content)
#     for id in root.iter("Id"):
#         id_new = int(id.text)
#         print(id_new)


def get_authors(pmid):
    url_auth= f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&rettype=abstract&id={pmid}"
    l_list=[]
    f_list=[]
    time.sleep(0.35)
    content = requests.get(url_auth).text
    root = ET.fromstring(content)
    for auth in root.iter("LastName"):
        last=(auth.text)
        l_list.append(last)
    for auth in root.iter("ForeName"):
        first=(auth.text)
        f_list.append(first)
    author_list=zip(l_list,f_list)
    return(list(author_list))
    # for auth in root.iter("Initials"):
    #     ini=(auth.text)
    #     i_list.append(ini)

def get_links_id(pmid):
    url_links = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin&id={pmid}&id={pmid}"
    link_set = set()
    content = requests.get(url_links).text
    root = ET.fromstring(content)
    for auth in root.iter("Id"):
        id=int(auth.text)
        link_set.add(id)
        if pmid in link_set: link_set.remove(pmid)
    return list(link_set)

#### need to do this one
# def get_links_term(term):
# 	links = Entrez.esearch(db="pubmed", retmax = 1000, term=term)
# 	record = Entrez.read(links)
# 	link_list = record[u'IdList']
#
# 	return link_list

papers = get_links_id(pmid)
for paper in papers:
    authors = get_authors(paper)
    for a in authors:
        author_total[a] = author_total.get(a,0) + 1
for key, val in author_total.items():
    list_desc.append((val,key))
    list_desc.sort(reverse=True)

if __name__ == "__main__":
    print("PMID: {}".format(pmid))
    print("PMID of papers citing this paper: ")
    print(papers)
    print("Authors citing this paper: ")
    print(list_desc)
