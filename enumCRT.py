import requests, argparse
from bs4 import BeautifulSoup

urls = []

def doQuery(query):
    resp = requests.get(query)
    try:
        if resp.status_code == 200:
            return resp
        else:
            return False

    except requests.exceptions.RequestException as e:
        print("[!] Maybe the host is offline :", e)
        exit()

def extractSubs(resp):
    soup = BeautifulSoup(resp.content, "html.parser")
    for i in soup.select("table tr td:nth-of-type(5)"):
        if not "*" in i.text:
            urls.append(i.text)
    
def sliptUniqueDomains():
    for i in sorted(set(urls)):
        print(i)

def main(url):
    query = "https://crt.sh?q="+ url 
    result = doQuery(query)
    extractSubs(result)
    sliptUniqueDomains()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', action='store', dest='url', required=True, help='Target url.')
    arguments = parser.parse_args()
    main(arguments.url)