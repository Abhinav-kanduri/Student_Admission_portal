import streamlit as st
import pickle
import sklearn
import pandas as pd


lin_reg_model= pickle.load(open('linear_reg_model.pkl','rb'))
random_forest_reg_model = pickle.load(open('randomforest_reg_model.pkl','rb'))
gb_reg_model = pickle.load(open('gb_reg_model.pkl','rb'))

st.set_page_config(page_title="Student Admission Portal using Machine Learning", page_icon=":bar_chart:", layout="wide")
st.header('NewYork Institute of Technology')
st.subheader('DTSC 610: Programming For Data Science - Final Project')
st.markdown('**Under the guidance of Professor Taoufik Ennoure**.')
st.text('Team members:\n 1.School ID: 1303749 - Abhinav Sai Kanduri \n 2.School ID: 1303464 - Meda Yashwanth Varma ')

st.header('Please choose your specialization code from the data shown below :')
df = pd.read_csv("courses.csv")
st.dataframe(df)
def result(num):
    num1 = num*100
    if num1<50:
        print('You have less than 50% of chances to admission in your dream school')
        return '{} is the percentage of chances you get admission'.format(num1)
    elif num1>=50  and num1<=100:
        print('You have more than 50% of chances to admission in your dream school')
        return '{} is the percentage of chances you get admission'.format(num1)
    elif num1>100:
        num1 = 99
        print('You have excellent profile 99.9% of chances to admission in your dream school')
        return '{} is the percentage of chances you get admission'.format(99.9)
    else:
        return 'please give the correct input'
def main():
    st.title("Student Admission portal using Machine Learning")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">DTSC-610 Final Project</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Linear Regression','Random Forest Regressor','Gradient Boosting Regressor']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    # Specialization Code, University Rank, GRE Score	TOEFL Score	University Rating	SOP	LOR	CGPA	Research
    sp_code =st.slider('Select Specialization Code in integer value', 1100, 6403)
    university_rank =st.slider('Select University Rank', 1, 173)
    GRE_Score =st.slider('Select GRE Score', 290, 340)
    TOEFL_Score =st.slider('Select TOEFL Score', 92, 120)
    University_Rating = st.slider('Select University Rating',1,5)
    SOP = st.slider('Select SOP',1.0,5.0)
    LOR = st.slider('Select LOR',1.0,5.0)
    CGPA = st.slider('Select CGPA',6.5 , 10.0)
    Research = st.slider('Select Research yes : 1 and No : 0',1,0)
    inputs=[[sp_code,university_rank,GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]]
    if st.button('Predict using the selected model'):
        if option=='Linear Regression':
            st.success(result(lin_reg_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(result(random_forest_reg_model.predict(inputs)))
        else:
           st.success(result(gb_reg_model.predict(inputs)))


if __name__=='__main__':
    main()