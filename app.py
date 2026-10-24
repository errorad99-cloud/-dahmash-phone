
from flask import Flask, render_template_string

app = Flask(__name__)

PRODUCTS = [
    {
        "name": "iPhone",
        "price": 15000,
        "emoji": "📱",
        "description": "ايفون بتصميم مميز"
    },
    {
        "name": "Samsung",
        "price": 12000,
        "emoji": "📲",
        "description": "موبايل سامسونج"
    },
    {
        "name": "Headphones",
        "price": 500,
        "emoji": "🎧",
        "description": "سماعة بجودة ممتازة"
    },
    {
        "name": "Smart Watch",
        "price": 800,
        "emoji": "⌚",
        "description": "ساعة ذكية عصرية"
    },
]

# حط رقم واتساب المتجر بصيغة دولية من غير +
# مثال لمصر: 201XXXXXXXXX
WHATSAPP_NUMBER = "201XXXXXXXXX"

PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dahmash Phone</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f4f6fa;
    color: #172033;
}
header {
    background: linear-gradient(135deg, #102b46, #087f8c);
    color: white;
    padding: 30px 15px;
    text-align: center;
}
header h1 { margin: 0 0 10px; font-size: 32px; }
header p { margin: 0; }
nav {
    background: #ffffff;
    padding: 14px;
    text-align: center;
    border-bottom: 1px solid #ddd;
}
nav a {
    color: #087f8c;
    text-decoration: none;
    font-weight: bold;
}
main {
    max-width: 1000px;
    margin: 25px auto;
    padding: 0 14px;
}
h2 { text-align: center; }
.products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
}
.card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 5px 18px #102b4612;
}
.emoji { font-size: 58px; }
.card h3 { margin: 12px 0; }
.description { color: #667085; }
.price {
    color: #087f5b;
    font-size: 21px;
    font-weight: bold;
}
.buy {
    display: block;
    background: #087f5b;
    color: white;
    padding: 12px;
    border-radius: 9px;
    text-decoration: none;
    margin-top: 14px;
}
.buy:hover { background: #066947; }
footer {
    margin-top: 35px;
    background: #102b46;
    color: white;
    padding: 22px;
    text-align: center;
}
</style>
</head>
<body>
<header>
    <h1>📱 Dahmash Phone</h1>
    <p>كل اللي تحتاجه من عالم الموبايلات والإكسسوارات</p>
</header>
<nav>
    <a href="/">الرئيسية</a> |
    <a href="#products">المنتجات</a>
</nav>
<main id="products">
    <h2>🛍️ منتجاتنا</h2>
    <div class="products">
    {% for p in products %}
        <article class="card">
            <div class="emoji">{{ p.emoji }}</div>
            <h3>{{ p.name }}</h3>
            <p class="description">{{ p.description }}</p>
            <p class="price">{{ p.price }} جنيه</p>
            <a class="buy"
               href="{{ wa }}?text={{ ('السلام عليكم، عايز أستفسر عن ' ~ p.name)|urlencode }}"
               target="_blank" rel="noopener">
               اطلب على واتساب
            </a>
        </article>
    {% endfor %}
    </div>
</main>
<footer>
    <p>Dahmash Phone © 2026</p>
    <p>شكراً لزيارتكم ❤️</p>
</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        PAGE,
        products=PRODUCTS,
        wa="https://wa.me/" + WHATSAPP_NUMBER
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
