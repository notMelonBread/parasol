from flask import Flask, render_template, request, redirect, url_for
import os
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",data="ここに読み上げられるテキストがきます")

@app.route("/upload_photo", methods=['GET','POST'])
def upload_photo():
    if request.method == 'POST':
        if "photo" in request.json:
            photo_data = request.json['photo']
            save_photo(photo_data, 'static/photos', 'snapshot.png')
            return "写真が送信されました"
        else:
            return "写真が見つかりません"
    else:
        return render_template("index.html", data="お茶は上からn番目、左からm番目の位置にあります")

def save_photo(photo_data, save_dir, file_name):
    # base64エンコードされた写真データをデコード
    photo_bytes = photo_data.split(',')[1].encode('utf-8')

    # ファイルの保存先ディレクトリを作成
    os.makedirs(save_dir, exist_ok=True)

    # ファイルパスを結合
    file_path = os.path.join(save_dir, file_name)

    # 写真をファイルとして保存
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(photo_bytes))

if __name__ == "__main__":
    app.run(debug=True)
