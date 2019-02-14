from random import randint


from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(
    __name__, static_folder="../dist/static", template_folder="../dist"
)
CORS(app)


@app.route("/api/random")
def random_number():
    response = {"randomNumber": randint(1, 100)}
    return jsonify(response)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


@app.route("/api/population/<pref_code>")
def population(pref_code):
    if pref_code == "all":
        return jsonify(dict(population=all_data))
    return jsonify(dict(population=dic[pref_code]))

dic = {
    "北海道": 5381733,
    "青森県": 1308265,
    "岩手県": 1279594,
    "宮城県": 2333899,
    "秋田県": 1023119,
    "山形県": 1123891,
    "福島県": 1914039,
    "茨城県": 2916976,
    "栃木県": 1974255,
    "群馬県": 1973115,
    "埼玉県": 7266534,
    "千葉県": 6222666,
    "東京都": 13515271,
    "神奈川県": 9126214,
    "新潟県": 2304264,
    "富山県": 1066328,
    "石川県": 1154008,
    "福井県": 786740,
    "山梨県": 834930,
    "長野県": 2098804,
    "岐阜県": 2031903,
    "静岡県": 3700305,
    "愛知県": 7483128,
    "三重県": 1815865,
    "滋賀県": 1412916,
    "京都府": 2610353,
    "大阪府": 8839469,
    "兵庫県": 5534800,
    "奈良県": 1364316,
    "和歌山県": 963579,
    "鳥取県": 573441,
    "島根県": 694352,
    "岡山県": 1921525,
    "広島県": 2843990,
    "山口県": 1404729,
    "徳島県": 755733,
    "香川県": 976263,
    "愛媛県": 1385262,
    "高知県": 728276,
    "福岡県": 5101556,
    "佐賀県": 832832,
    "長崎県": 1377187,
    "熊本県": 1786170,
    "大分県": 1166338,
    "宮崎県": 1104069,
    "鹿児島県": 1648177,
    "沖縄県": 1433566,
}
all_data = [[x, y] for x,y in dic.items()]
