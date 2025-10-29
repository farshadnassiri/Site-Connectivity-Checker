import streamlit as st
import requests
import concurrent.futures


def format_url(url):
    if url.startswith("http://"):
        url=url[len("http://"):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
    if url.startswith("www."):
        url=url[len("www."):]
    formatted_url="https://www." +url    
    return formatted_url

def check_site_availability(url):
    try:
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.36'
        }    
        response=requests.get(url,timeout=5,headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def main():
    st.title(':zap: Website Availability Checker')
    if "urls" not in st.session_state:
        st.session_state.urls=[]

    new_url = st.text_input('Enter URL', value="https://www.google.com")
    new_url = format_url(new_url)  
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Add URL", use_container_width=True):
            if new_url and new_url not in st.session_state.urls:
                st.session_state.urls.append(new_url) 
            else:
                st.warning("Please enter a valid URL or URL is already added")
    with col2:
        if st.button("Clear URLs", use_container_width=True):
            st.session_state.urls=[]
    if st.button("Check Availability", use_container_width=True):
        with st.spinner("Checking websites..."):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures={
                    executor.submit(check_site_availability,url) : url for url in st.session_state.urls
                }
                for idx ,(future,url) in enumerate(zip(futures.keys(),st.session_state.urls)):
                    st.session_state[f"status_{idx}"]=future.result()



    if st.session_state.urls:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("URL")
                for url in st.session_state.urls:
                    st.write(url)
            with col2:
                st.subheader("Status")
                for idx, url in enumerate(st.session_state.urls):
                    status = st.session_state.get(f"status_{idx}")
                    if status is True:
                        st.write(":white_check_mark: Online")
                    elif status is False:
                        st.write(":x: Offline")
                    else:
                        st.write("⏳ Not checked yet")
    else:
            st.warning("Please add URLs to check availability")



if __name__ == '__main__':
    main()
