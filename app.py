import streamlit as st
from joblib import load

def main(): 
    st.title("Life Satisfaction Prediction")
    st.write("Enter the calue of your country's GDP per capita using the slider below:")
    st.sidebar.title("Developer's Contact")
    st.sidebar.write('[![Hritik Valluvar]'
                        '(https://img.shields.io/badge/Author-Hritik%20Valluvar-green)]'
                        '(https://www.linkedin.com/in/hritikvalluvar/)')

    input = st.slider('GDP per capita(USD)',0.0, 130000.0)
    gdp = [[input]]
    if gdp:
        output = model_output(gdp)
        st.write("Life satisfaction of a country who's GDP per capita is **${}** might be **{}**.".format(input, output))
    
@st.cache    
def model_output(gdp):
    model = load('model.joblib')
    return '{0:.3g}'.format(float(model.predict(gdp)))


if __name__ == '__main__':
    main()
