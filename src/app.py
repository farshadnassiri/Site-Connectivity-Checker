import streamlit as st
import requests
import concurrent.futures


def foramt_url(url):
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
            



