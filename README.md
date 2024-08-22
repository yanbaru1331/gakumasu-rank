# gakumasu-rank

## How to Use
```
docker compose build
docker compose up -d
```
アタッチ後

## poetryの構築にcargoが必要(???)なので
その準備とpoetryのインストール
```
curl https://sh.rustup.rs -sSf | sh
curl -sSL https://install.python-poetry.org | python3 -
```

`.env`ファイルを作成し
discordのトークンとギルドIDを記載する
(サンプルは掲載してあります。サンプルを使用する場合は`.sample`を削除してください)

```
poetry install
python ./gakumasu/__init__.py
```
で登録したギルド(サーバ上)でスラッシュコマンドで計算することができます。

## その他
この機能がほしい、バグを抱えている等ございましたらお手数ですが以下の連絡先までご連絡をお願いたします。
## 問い合わせ先
discord: `yanbaru_popo`
x: `kaito_tippu`

## 参考文献
[スプレッドシート](https://docs.google.com/spreadsheets/d/1eEdzfHGi7iXpohR-UHr5-W1z7PcYBqQr8OAV7gcvhR8/edit#gid=0)
[WEB版計算機](https://x.com/nok0714/status/179814844641693705)
