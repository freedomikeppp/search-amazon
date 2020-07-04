from bs4 import BeautifulSoup
import requests
import traceback
from time import sleep
from common import Common

urls = [
    # exp). Nintendo Switch Lite ターコイズ
    #"https://www.amazon.co.jp/%E4%BB%BB%E5%A4%A9%E5%A0%82-Nintendo-Switch-%E3%82%BF%E3%83%BC%E3%82%B3%E3%82%A4%E3%82%BA/dp/B07X779ZK5/ref=sr_1_10?dchild=1&keywords=%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81+%E6%9C%AC%E4%BD%93&qid=1591368858&sr=8-10",
    # Nintendo Switch 本体 (ニンテンドースイッチ) Joy-Con(L) ネオンブルー/(R) ネオンレッド(バッテリー持続時間が長くなったモデル)
    "https://www.amazon.co.jp/%E4%BB%BB%E5%A4%A9%E5%A0%82-Nintendo-Switch-Lite-%E3%82%A4%E3%82%A8%E3%83%AD%E3%83%BC/dp/B07WS7BZYF/ref=sr_1_9?dchild=1&keywords=%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%2B%E6%9C%AC%E4%BD%93&qid=1591368858&sr=8-9&th=1",
    # Nintendo Switch 本体 (ニンテンドースイッチ) Joy-Con(L)/(R) グレー(バッテリー持続時間が長くなったモデル)
    "https://www.amazon.co.jp/Nintendo-Switch-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81-Joy-%E3%83%90%E3%83%83%E3%83%86%E3%83%AA%E3%83%BC%E6%8C%81%E7%B6%9A%E6%99%82%E9%96%93%E3%81%8C%E9%95%B7%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%83%A2%E3%83%87%E3%83%AB/dp/B07WS7BZYF/ref=sr_1_2?dchild=1&keywords=%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81+%E6%9C%AC%E4%BD%93&qid=1591368858&sr=8-2"
]

try:
    for url in urls:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        bs = BeautifulSoup(response.text, 'html.parser')
        price_span = bs.find(id='priceblock_ourprice')

        # 価格タグ存在チェック
        if price_span is not None:
            price = int(price_span.text[1:].replace(',', ''))
            # メール送信
            if price is not None:
                Common.send_mail(
                    'to_example_address@gmail.com',
                    'ニンテンドースイッチが購入可能',
                    f'URL： {url}'
                )
                Common.info('メールを送信しました。')
        sleep(3)
    Common.info('正常処理完了')
except:
    Common.error(traceback.print_exc())
