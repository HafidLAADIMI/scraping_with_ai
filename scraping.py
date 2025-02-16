import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = input("please enter the link of the website : ")
def scrape_web(url):
    try:
        driver.get(url)
        html = driver.page_source
        print(html)
        return html
    except Exception as e:
        print(e)
        return e


def extracting_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body
    if body_content:
        print(str(body_content))
        return str(body_content)
    return ''


def cleaned_contend(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["style", "script"]):
        script_or_style.extract()

    content_text = soup.get_text(separator="\n")
    content_text = [line.split() for line in content_text.splitlines() if line.split()]
    # print(split_lines)
    # print(len(split_lines))
    # clean_content="\n".join(split_lines)
    # print(clean_content)
    clean_content = " ".join([word for sublist in content_text for word in sublist])
    print(clean_content)
    return clean_content


def split_dom_content(dom_content, max_length=600):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]


#url = input(print("please enter the link of the website : "))
#url = "https://hafid-laadimi.vercel.app/"
print(cleaned_contend(extracting_content(scrape_web(url))))
