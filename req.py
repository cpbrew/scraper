from craigslist import CraigslistForSale

class Scrapper:

  class Craigslist:

    def __init__(self, site='seattle', category='syp'):
        self.site = site
        self.category = category

    def get_listings(self, query=None, max_price=None):
      filters = {}
      if query:
        filters['query'] = query
      if max_price:
        filters['max_price'] = max_price

      cl_fs = CraigslistForSale(site=self.site, category=self.category, filters=filters)
      return cl_fs.get_results(sort_by='newest')


cl = Scrapper.Craigslist()
for r in cl.get_listings(query='gtx', max_price=100):
  print(f"{r['id']}: {r['name']} - {r['price']}\n{r['url']}")
