# **Life-Satisfaction-Prediction**
Life Satisfaction Index can be predicted by using GDP per capita as the features. This ML project was wrapped with streamlit and deployed on heroku.

**Note:** It's important for data scientist or ML practioners to be able to deploy their model.

## Simple Linear Model


life_satisfaction = &theta;<sub>o</sub> + &theta;<sub>1</sub> * GDP_percapita

where &theta;<sub>o</sub> and &theta;<sub>1</sub> are model features.

---

<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>

---

## **Demo** 

Click [here](https://hritikvalluvar-life-satisfaction-prediction-app-32rwt6.streamlit.app/) to see the demo.

![demo](https://github.com/hritikvalluvar/Life-Satisfaction-Prediction/blob/main/demo.png)

## **Usage**

Clone the repository


`git clone https://github.com/hritikvalluvar/Life-Satisfaction-Prediction`


Change working directory

`cd Life-Satisfaction-Prediction`

Create virtual environement

`python3 -m pip virtualenv .env`

Activate virtual environment

`source .env/bin/activate`

Install dependencies

`python3 -m pip install -r requirements.txt`

Run app.py on streamlit

`streamlit run app.py`


## License
[MIT](https://github.com/hritikvalluvar/Life-Satisfaction-Prediction/blob/main/LICENSE)
