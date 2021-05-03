import requests
import json


def lwTopSearches(keyword, prodIds): 
    url_lw = 'https://<rest-endpoint-new-system>/us/en/search/products/service'

    query_params = {'keyword':keyword}

    r = requests.get(url = url_lw, params = query_params)

    data = r.json() 

    if("productResults" in data):
        i = 0
        for productResult in data['productResults']:
            productId = productResult['productId']
            print ("ProductIdLW %s: %s"  %(i, productId))
            i += 1
            if (i > 10):
                break

        i = 1
        for prodId in prodIds:     
            j = 0
            for productResult in data['productResults']:
                j += 1
                productId = productResult['productId']
                if (prodId == productId):
                    print ("ProdId: %s, End Pos:, %s, LW Pos: %s" %(productId, i, j))
            i += 1

def endecaTopSearches(keyword): 
    prodIds=[]

    url_endeca = 'https://<rest-endpoint-old-system>/us/en/service/search/products'

    query_params = {'keyword':keyword}

    r = requests.get(url = url_endeca, params = query_params)

    data = r.json() 

    i = 0
    for productResult in data['productResults']:
        productId = productResult['productId']
        print ("ProductIdEN %s: %s"  %(i, productId))
        prodIds.append(productId)
        i += 1
        if (i > 10):
            break

    lwTopSearches(keyword, prodIds)

def loadKeywords(): 
   keywords=[]

   file = open('keywords.txt', 'r')
   for line in file.readlines():
     keywords.append((line.strip().lower()))

   file.close()  

   for keyword in keywords:
       print(keyword)
       endecaTopSearches(keyword)


def main():
 
    loadKeywords()

if __name__ == "__main__":
    main()