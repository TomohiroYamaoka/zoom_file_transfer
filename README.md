# zoom_file_transfer

Test transferring recording files from zoomcloud to box when zoom finishes recording

## 取得手順

1. zoom から POST された JSON ファイルを受け取る
2. 受け取った JSON ファイルから、zoom レコーディングファイル(URL)を取り出す
3. zoom レコーディングファイルを box に転送する。

## zoom アカウント

https://marketplace.zoom.us/develop/create?source=devdocs

## BOX アカウント

https://www.box.com/ja-jp/pricing/individual

## 参考

1.  https://www.wantedly.com/companies/serverworks/post_articles/162674

2.  https://qiita.com/Hiroyama-Yutaka/items/3aba71fe6e465e6a3388

## dotenv について

https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9

## boxAPI の認証について

https://medium.com/box-developer-blog/box-api-understanding-security-ja-b95725d8aaf0

## 課題

・zoomCloud の機能はビジネス版しかないため、zoomAPI の受け取り確認ができない  
・boxJWT 認証の期限  
