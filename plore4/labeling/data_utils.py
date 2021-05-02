from labeling.models import ConditionMeta, Condition, Article

import requests, re

def fetch_article_data(pmid):
    try:
        # get summary data only, no abstract
        api_key = "5aeb8d74d74e99db30b38efabc089ad20709"
        base_url = str(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json&api_key={api_key}")
        result = requests.get(base_url)
        json_data = result.json()
        data = json_data['result']
        uid = data['uids'][0]
        subdata = data[uid]

        pubdate = subdata['pubdate']
        year = re.search('[0-9]{4}', pubdate).group(0)

        source = subdata['source']
        author_list = subdata['authors']
        author_names = []

        for a in author_list:
            author_names.append(a['name'])

        author_string = ', '.join(author_names)

        title = subdata['title']

        pubtype = subdata['pubtype'][0]

        # get abstract data
        url = str(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=text&rettype=abstract&api_key={api_key}")
        response = requests.get(url)
        abstract = str(response.text)

        finald = {'title': title,
                  'pubyear': year,
                  'authors': author_string,
                  'pubtype': pubtype,
                  'abstract': abstract,
                  'source': source}

        return finald
    except:
        return None

def data_loader_1():
    # create articles
    pmids = ['27870579', '26969618', '29464801', '31464298', '10318745', '25370281']
    new_article_objects = []
    for pmid in pmids:
        article_data = fetch_article_data(pmid)
        if article_data:
            print('success')
            new_article = Article(pmid=pmid,
                                  title=article_data['title'],
                                  abstract=article_data['abstract'],
                                  pub_year=article_data['pubyear'],
                                  source=article_data['source'],
                                  authors=article_data['authors'],
                                  pubtype=article_data['pubtype'])
            new_article.save()
            new_article_objects.append(new_article)
        else:
            print('failure')

    new_condition = Condition(title='Example Condition')
    new_condition.save()

    new_condition_meta = ConditionMeta(condition=new_condition)
    new_condition_meta.save()

    for new_article_object in new_article_objects:
        new_condition_meta.article_pool.add(new_article_object)

    new_condition_meta.save()

data_loader_1()
