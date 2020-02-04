from flask import Flask, render_template, request
from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("marathon.html")

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/run')
def run():
    return render_template("run.html")

@app.route('/bookname', methods=['POST'])
def post():
    value = request.form['test']

    driver = webdriver.Chrome('C:\\Users\ssb38\Desktop\chromedriver_win32\chromedriver.exe')
    url = 'https://book.naver.com/'
    driver.implicitly_wait(3)
    driver.get(url)

    driver.find_element_by_id("nx_query").send_keys(value)
    driver.find_element_by_id("search_btn").click()


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.select("#container > div.spot > div.book_info > div.book_info_inner > div:nth-child(4)")
          )
    return render_template("run.html")




if __name__ == '__main__':
    app.run()