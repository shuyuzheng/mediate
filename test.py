import json

x = '''{
  "status":"OK",
  "copyright":"Copyright (c) 2008 The New York Times Company.  All Rights Reserved.",
  "has_more":false
  "num_results":8,
  "results":[
     {
        "display_title":"Big Night",
        "sort_name":"Big Night",
        "mpaa_rating":"R",
        "critics_pick":"Y",
        "byline":"Janet Maslin",
        "headline":"",
        "capsule_review":"Restaurateur brothers stake all on one dinner. Succulent comedy.",
        "summary_short":"",
        "publication_date":"1996-03-29",
        "opening_date":"1996-09-20",
        "date_updated":"2008-11-04 03:54:15",
        "link":{
           "type":"article",
           "url":"http:\/\/movies.nytimes.com\/movie\/
                   review?res=9501E6DA1539F93AA15750C0A960958260",
           "suggested_link_text":"Read the New York Times Review of Big Night"
        }
     }
  ]
}'''

y = json.loads(x)["results"]

for i in y:
    print(i["display_title"])
