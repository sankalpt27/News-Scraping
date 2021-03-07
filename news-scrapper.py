
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
from urllib.request import Request

app = Flask(__name__)
j=0

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:

            import requests
            from bs4 import BeautifulSoup

            image=[]
            url = request.form["fname"]
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            news = []
            urls = []
            for link in soup.find_all('a'):
                print(link.get('href'))
                urls.append(link.get('href'))
            res = []
            for val in urls:
                if val != None:
                    res.append(val)

            for u in res:
                u = u.replace("'", "")

            lol = []
            for i in res:
                if i.startswith('https://www.nytimes'):
                    lol.append(i)

            from newspaper import Article
            texts = []
            titles = []
            # url = "https://timesofindia.indiatimes.com/india/governments-2022-jk-plan-resettlement-of-kashmiri-pandits-25k-jobs-train-link/articleshow/80899281.cms"
            # download and parse article
            for i in range(len(lol)):
                j=i
                r = lol[i]
                article = Article(r)
                article.download()
                article.parse()
                titles.append(article.title)
                #image.append(article.top_image)
                #texts.append(article.text)
                mydict = {"Titles": article.title, "Text":article.text , "Image" : article.top_img}
                news.append(mydict)
                news.append("\n")




            return render_template('Scrapped.html', news=news, url= url)
        except:


            return render_template('Scrapped.html', news =news,url =url)

if __name__ == "__main__":
    app.run(debug=True)