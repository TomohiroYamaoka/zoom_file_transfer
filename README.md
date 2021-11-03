# zoom_file_transfer

Test transferring recording files from zoomcloud to box when zoom finishes recording

## 取得手順

1. zoom から POST された JSON ファイルを受け取る
2. 受け取った JSON ファイルから、zoom レコーディングファイル(URL)を取り出す
3. zoom レコーディングファイルを box に転送する。
