# 概要
 Amazonの特定品目の価格が安くなった際にメールを自動送信するプログラムです。

具体的には、URLとHTMLタグを指定し、タグの内部の数値を取り出し、設定した金額より低くなればメールで通知します。

本プログラムではAmazonを対象にしてますが、URLや取得するHTMLタグを書き換えればその他サイトでも使えそうです。

# 準備

## リポジトリのクローンとpipenvで仮想環境設定

```
git clone https://github.com/freedomikeppp/search-amazon.git
cd search-amazon
pipenv shell
pipenv install
```

## GmailでSMTPを使う
本プログラムでは、GmailのSMTPサーバからメールを送信します。

よって、送信に利用するGmailアカウント上で、以下の『「安全性の低いアプリの許可」を有効にする』必要があります。
https://support.google.com/accounts/answer/6010255?hl=ja

送信元として、common.pyの以下を書き換えます。

```
    # SMTPメール設定
    __smtp_addr = "from_example_address@gmail.com"
    __smtp_addr_pass = "your_pass"
```

送信先として、search.pyの以下を書き換えます。

```
Common.send_mail(
   'to_example_address@gmail.com',
   ...
```

社内のSMTPサーバを使う場合は、common.pyの以下を書き換えます。

```
smtplib.SMTP('smtp.gmail.com', 587)
```

## 実行方法
```
pipenv shell
python search.py
```

## ログの取得
ログはデフォルトで、search-amazon/search.logに出力されます。

## cronでの実行
Linuxサーバや適当なRaspberryPi(Raspbian)でcronから定期実行することが可能です。
例えば２分おきなどで実行しましょう。

以下、cron.txtの例。

```
*/2 * * * * cd /to/your/repsitory/path/search-amazon; . /your/local/virtualenvs/bin/activate;python generator.py
```

