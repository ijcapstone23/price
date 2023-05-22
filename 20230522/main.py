from flask import Flask, render_template, redirect, request, url_for
import csv
import pandas as pd
# import learn
import os

os.system('chcp 65001')
os.system('dir/w')

f = open('productDataEx.csv', 'r', encoding='utf-8')
data = pd.read_csv('productDataEx.csv', encoding='utf-8', sep=",", error_bad_lines=False)
data.set_index('id', inplace=True)
cart = []  # 전역 변수 '장바구니 내용'

'''
def proceed2payment():  # 결제 진행창
    if len(cart) == 0:
        message = '카트가 비었습니다.'
    else:
        message = ['고객님의 상품 ']
        for i in range(len(cart)):
            message.append(Product(cart[i]).getname)
            if i+1 >= len(cart):
                message.append(' 정상 결제되었습니다.')
            else:
                message.append(', ')
        message = ''.join(message)
    cart.clear()
    return message

def mycart():  # 카트 확인
    if len(cart) == 0:
        message = '카트가 비었습니다.'
    else:
        message = ['현재 카트에는 상품 ']
        for i in range(len(cart)):
            message.append(Product(cart[i]).getname)
            if i+1 >= len(cart):
                message.append(' 이(가) 있습니다.')
            else:
                message.append(', ')
        message = ''.join(message)
    return message


class Product:  # '제품' 클래스
    id: object

    def __init__(self, id):  # '제품'은 제품 고유의 ID로 호출됨
        self.id = id

    def add2cart(self):  # 제품을 장바구니에 담음
        cart.append(self.id)

    @property
    def getname(self):
        return data.loc[self.id]['name']

    @property
    def getid(self):
        return str(self.id)


def recommend(prom):
    return '추천 시스템은 아직 구현되지 않았습니다.'


def basket(prom):
    bask = []
    message = ['']
    
    rd = csv.reader(f)  # CSV 리더
    for line in rd:
        print(line)
        if line[1] in prom:
            bask.append(int(line[0]))
    
    dict = data['name'].to_dict()
    for key in dict:
        if dict[key] in prom:
            bask.append(key)
    if len(bask) == 0:
        message.append('물건을 찾을 수 없었습니다.')
    else:
        message.append('상품 ')
        i = 0
        for item in bask:
            i += 1
            itemclass = Product(item)
            message.append(itemclass.getname)
            itemclass.add2cart()
            if i >= len(bask):
                message.append(' 장바구니에 담겼습니다.')
            else:
                message.append(', ')
    return ''.join(message)

'''
app = Flask(__name__)

print('__name__', __name__)
print('DEBUG', app.config['DEBUG'])


@app.route('/')

def index():
    inputdata = request.args.get("query")
    if inputdata == None:
        result = ""
    else:
        result = resultPrint(inputdata)
    return ('<h1>웹버전 쇼핑 프로그램</h1><br>현재 200 개의 사무용품 데이터가 등록되어 있습니다.<br><a href="/basket">장바구니 가기</a><br><h2>상품 검색</h2><br><form action="" method="SEARCH" class="form-example"><input type="text" name="query" id="query" required> <input type="submit" value="검색"></form><br>'
            + result
    )


def resultPrint(inputdata):
    series = data.loc[(data['productName'].str.contains(inputdata)) | (data['productTitle'].str.contains(inputdata)) | (data['productTitleOrg'].str.contains(inputdata))]
    return ('검색 결과에는 다음이 있습니다: <br>') + result(series)

def result(series):
    message = []
    for idx in series.iterrows():
        message.append(idx[1]['productName'] + ' (' +str(idx[1]['lowPrice']) + '원)' + '<br>')
    return ''.join(message)

@app.route('/basket')
def _():
    return 0

if __name__ == "__main__":
    print('run')
    app.run(debug=True, port=7548, host='localhost')
