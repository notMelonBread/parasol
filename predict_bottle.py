from keras.utils import load_img, img_to_array
from keras.models import model_from_json
import numpy as np


# 画像が保存されているルートディレクトリのパス
root_dir = (".\\")
# 商品名
categories = ["water", "tea"]
# 保存したモデルの読み込み
model = model_from_json(
    open(root_dir + "\\tea_predict.json").read())
# 保存した重みの読み込み
model.load_weights(root_dir + "\\tea_predict.hdf5")


# 画像を読み込む
img_path = str(input("画像ファイル名を入力してください："))
img = load_img(img_path, target_size=(250, 250, 3))
x = img_to_array(img)
x = np.expand_dims(x, axis=0)

# 予測
features = model.predict(x)

# 予測結果によって処理を分ける
if features[0, 0] == 1:
    print("選ばれたのは、waterでした。")

elif features[0, 1] == 1:
    print("選ばれたのは、teaでした。")

else:
    for i in range(0, 10):
        if features[0, i] == 1:
            cat = categories[i]
    message = "綾鷹を選んでください。（もしかして：あなたが選んでいるのは「" + cat + "」ではありませんか？）"
    print(message)