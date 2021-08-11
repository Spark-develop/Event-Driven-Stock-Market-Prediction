# Event-Driven-Stock-Market-Prediction 1.0

## Description

-  Project is all about a system that predicts stock prices using the events occurring day by day. Events have been extracted from the archives section of the newspapers            available online. Then the extracted headlines are been divided into three parts i. e. actor, relation, and object. After some preprocessing and generation of the word          vectors, these texts are sent for calculating entity relation representation to the novel neural tensor network. Further, they are processed using a deep convolutional neural    network with a max-pooling layer, and the result is been concluded into two classes positive and negative.

## Badges

![Sparx Develop](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white) 
![social](https://img.shields.io/github/followers/Spark-develop?style=social) 
![Prototype-Website](https://img.shields.io/website?down_color=blue&up_color=orange&up_message=Predictor.&url=https%3A%2F%2Fportfolios-work.web.app%2F%23%2F)

## Visuals
1. Dataset --> Triplet Extraction --> Word-Embeddings(FastText model) 


   ![Model1](images/part-1.png)
   
2. Word-Embeddings --> NTN model --> convolutional model


   ![Model2](images/part-2.PNG)

## Setup

-  This repository contains Backend-side code for front-end and its installations process click [here](https://github.com/Spark-develop/Predictor.)

-  For setting up the backend, I had used [Google-Firebase](https://firebase.google.com/) on both the sides, pushing predicted Data of news and tweets to the firebase, using        [firebase admin] https://firebase.google.com/docs/database/admin/start#python package, the hyperlink contains setup documentation about the firebase admin and its queries.

-  If you are new you need to first Register/Sign up @ [Google-Firebase](https://firebase.google.com/) with email you want, go to console build a project and start.
   Follow the follwing structure and flow ofo database, for the code to work easily,
   ![struct](images/database_structure.PNG)

**Imports needed**
```
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
```

**Fetch the service account key JSON file contents**
```
cred = credentials.Certificate('path/to/serviceAccountKey.json')
```

**Initialize the app with a service account, granting admin privileges**
```
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com'
})
```

**As an admin, the app has access to read and write all data, regradless of Security Rules**
```
ref = db.reference('restricted_access/secret_document')
print(ref.get())
```
## Frameworks/Methods used
- Beautiful soup(bs4) - web scraping tool


- <img src="https://github.com/Spark-develop/Event-Driven-Stock-Market-Prediction/blob/aa51bbebc7ecaafe677dae36878072f4e11be504/images/fasttext.png" width="200" height="50">  -  gettings word vectors.

- NTN model for action - for getting entity relationship representation

- Convolution model - for training the representation and using it for predicting sentiments
- 
## Usage

- Firstly run [top_stocks.ipynb](topstocks.ipynb) file to get names of top stocks(Indian) which are established in BSE and NSE 
  ```
  link = "https://money.rediff.com/companies/market-capitalisation"
  dayres = requests.get(link)
  daysoup1 = bs4.BeautifulSoup(dayres.text, 'html.parser')
  ```
  the snippet in from the file, denoting that web scraping is been performed on the link given above.
- a new file will be created named [topL.csv](topL.csv), containing the web scraped names of top stocks.
  [topL](images/top_table_img.PNG)
  
- Further, execute the [extract_news.py](Utils/extract_news.py) for extracting the news of the top List.
- or run directly the [analysis.ipynb](analysis.ipynb) for processing the tweets for prediction.
- at last run the [predicted.ipynb](predicted.ipynb) for passing data to the firebase.(Please make changes in firebase_admin before running this file)

  ![results](images/results.PNG)

## Support

- tell users how they can get a hold of you

Contact: [email me](trevor.tomesh@gmail.com)

## Road-map

- List your panned future developments
- This is a good way to keep track of what it is that you want to do in the future!


## License

- Depending on what kind of project you are doing, you might have a specific copyright. 
- Usually on github, everything is open source!
- You can find license info here: [license](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/licensing-a-repository)

## Project Status

- A lot of the time people will abandon projects. You should always at least let people know if you aren't interested in working on a project anymore!
- Someone might want to pick it up on your behalf!

