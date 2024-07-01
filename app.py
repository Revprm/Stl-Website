import streamlit as st

projects = [
    {'name': 'BitCoin Time Series Forecasting', 'description': 'Bitcoin Time Series Forecasting Using RNN(Recurrent Neural Network) and LSTM RNN(Long Short Term Memory RNN)', 'source_link': 'https://colab.research.google.com/drive/1dqNIzCHhLsd-fXer0FR5_sFAAZPteAy9?usp=sharing', 'image_url': 'https://i.imgur.com/9t1UPJc.png'},
    {'name': 'Final Project Machine Learning Class', 'description': 'Final Project For Machine Learning Class (implemented XGBoost, KNN, SVM, ANN and many more)', 'source_link': 'https://github.com/Revprm/ML-Class/blob/main/Final%20Project/FP_ML_B.ipynb', 'image_url': 'https://i.imgur.com/EwXOeom.png'},
    {'name': 'Apple Stock Time Series Forecasting ', 'description': 'Apple Stock Time Series Forecasting Using LSTM RNN (Long Short Term Memory RNN)', 'source_link': 'https://colab.research.google.com/drive/1jmZixbsgLU-JwvTq0ja9EEmU9PhzdoRM?usp=sharing', 'image_url': 'https://i.imgur.com/XLit9vp.png'},
]

def main():
    st.title('Revy Pramana')
    st.markdown('---')
    st.markdown("##### Welcome to my personal website! I'm an Undergraduate Student at Institut Teknologi Sepuluh Nopember, Surabaya, Indonesia. I'm passionate about Data Science, Machine Learning, and Deep Learning. Feel free to check out my projects below!")
    st.title('Projects')
    st.markdown("---")
    
    for project in projects:
        st.write(f"## {project['name']}")
        st.image(project['image_url'], caption=f"Image for {project['name']}", use_column_width=True)
        st.write(f"*{project['description']}*")
        st.write(f"Source Code: [{project['name']}]({project['source_link']})")
        st.markdown("---")

if __name__ == '__main__':
    main()
