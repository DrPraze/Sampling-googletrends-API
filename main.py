# pip install googletrends (library for getting google search data)
import googletrends as googletrends

""" 
Documentation:
This code runs a simple flask API that can provide data on google data based on trending results, timed results and geographical results.
Global params for making searches:
* Searchwords (keywords for search)
Example: searchwords = ['bitcoin', 'ethereum']
* Geography filters (for collecting data based on geo)
Example: geo = ['NG', 'italy']
* Starting date filters to get data from specific date
Example: date_start = '01-12-2022'
"""
"""
Fetching data through googletrends library:
# Temporal
results = googletrends.temporal(searchwords, geo=geo, date_start=date_start)
googletrends.plot(results, color_by_searchword=True, group_by_searchword=False)

#  spatio (get results based on location)
results_spatio = googletrends.spatio(searchwords, geo=geo, date_start=date_start)
googletrends.plot(results_spatio)

# Trending (Get trending results)
results_trending = googletrends.trending(searchwords, geo=geo, date_start=date_start)
googletrends.plot(results_trending)

"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def get_googletrends(keywords, geo=None, date_start=None):
    results = googletrends.temporal(keywords, geo=geo, date_start=date_start)
    geo_results = googletrends.spatio(keywords, geo=geo, date_start=date_start)
    trending_results = googletrends.trending(keywords, geo=geo, date_start=date_start)
    return {
        "results": results,
        "geo_results": geo_results,
        "trending_results": trending_results
    }
class Geo(Resource):
    def get(self):
        # %% Get all country names
        geo_names = googletrends.get_geo_names()

        return {
            "Success": True,
            "geo_names": geo_names
            }
    
class Main(Resource):
	def get(self, keywords, geo, date_start):
            keywords = list(keywords.split(","))
            geo = list(geo.split(","))
            output = get_googletrends(keywords, geo, date_start)

            return {"Success": True,
                        "keywords":str(keywords),
                        "geo":str(geo),
                        "date_start":date_start,
                        "data": output
                        }

api.add_resource(Geo, "/geo_info")
# api.add_resource(Main, "/googletrends/<str:keywords>/<str:geo>/<str:date_start>") 

if __name__== '__main__':
	# app.run(debug=True)
    keywords = ["Ethereum", "Bitcoin"]
    geo = ["NG", "italy"]
    date_start = "02-03-2022"
    get_googletrends(keywords, geo, date_start)
