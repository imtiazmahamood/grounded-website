"""Generates public/index.html. Edit MENU below to change prices, then run: python3 build.py"""
import re, pathlib

root = pathlib.Path(__file__).parent
orig_css = (root / "base.css").read_text()

# ---------- MENU DATA (prices in USD) ----------
# item: (name, description, price or (price1, price2))
HOT_COFFEE = ("Hot Coffee", ["S", "R"], [
    ("Cappuccino", "Equal parts espresso, steamed milk and foam for a rich, frothy texture.", ("2.00", "3.00")),
    ("Coffee", "A classic, strong cup of black coffee made from freshly ground beans.", ("2.00", "3.00")),
    ("Latte", "Espresso combined with steamed milk and topped with a small amount of foam.", ("2.00", "3.00")),
    ("Cortado", "Espresso with equal parts warm, steamed milk.", ("2.00", "")),
    ("Americano", "Hot water added to a shot of espresso for a lighter, yet bold coffee.", ("2.00", "3.00")),
])
COLD_COFFEE = ("Cold Coffee", ["R", "L"], [
    ("Iced Coffee", "Chilled black coffee served over ice cubes.", ("3.00", "5.00")),
    ("Iced Latte", "Espresso and cold milk over ice.", ("3.00", "5.00")),
    ("Iced Chai Latte", "Spiced tea mixed with cold milk and chai concentrate.", ("3.00", "5.00")),
])
NOT_COFFEE_HOT = ("Not Coffee", ["S", "R"], [
    ("Hot Tea", "Five Roses, Tanganda or Rooibos.", ("2.00", "3.00")),
    ("Hot Choc", "Rich and creamy hot chocolate.", ("2.00", "3.00")),
    ("Matcha Latte", "Finely ground Japanese green tea powder, served over milk of choice. Iced or hot.", ("", "5.00")),
    ("Chai Latte", "Spiced tea latte made with steamed milk and chai spice concentrate.", ("3.00", "5.00")),
    ("Dirty Chai", "A shot of espresso added to a traditional chai latte.", ("4.00", "5.00")),
    ("Mochaccino", "A shot of espresso with steamed milk and chocolate (syrup or cocoa powder).", ("3.00", "4.00")),
])
MILKSHAKES = ("Milkshakes", ["R", "L"], [
    ("Milkshake", "Strawberry, chocolate, banana, lime, coffee, hazelnut, vanilla or bubblegum.", ("4.00", "5.00")),
])
EXTRAS = ("Extras &amp; Cold Drinks", None, [
    ("Flavoured Syrup", "Hazelnut, vanilla, caramel or salted caramel.", "+1.00"),
    ("Almond Milk", None, "+1.00"),
    ("Soft Drinks", None, "1.00"),
    ("Energade", None, "1.50"),
    ("Red Bull", None, "1.50"),
])
FOOD = ("Food", None, [
    ("Scones", None, "0.50"),
    ("Samoosas", "Chicken mince, beef mince or cheese.", "0.50"),
    ("Carrot Cake", None, "3.00"),
    ("Pies", "Chicken, pepper steak or BBQ steak.", "3.00"),
    ("Wors Roll", None, "3.00"),
    ("Russian Roll", None, "2.00"),
    ("Chips (S)", None, "1.00"),
    ("Toasted Sandwich: Spicy Chicken Mayo", None, "3.00"),
    ("Toasted Sandwich: Cheese &amp; Tomato", None, "2.00"),
])


def item(name, desc, price):
    d = f'<div class="desc">{desc}</div>' if desc else ""
    prices = price if isinstance(price, tuple) else (price,)
    p = "".join(f"<span>{x}</span>" for x in prices)
    return f'<div class="menu-item"><div><div class="name">{name}</div>{d}</div><div class="price-pair">{p}</div></div>'


def group(g):
    title, cols, items = g
    c = f'<div class="menu-cols">{"".join(f"<span>{x}</span>" for x in cols)}</div>' if cols else ""
    return f'<div class="menu-group"><h3>{title}</h3>{c}{"".join(item(*i) for i in items)}</div>'


menu_html = (
    '<div class="menu-grid"><div>' + group(HOT_COFFEE) + group(NOT_COFFEE_HOT) + group(FOOD) + "</div><div>"
    + group(COLD_COFFEE) + group(MILKSHAKES) + group(EXTRAS) + "</div></div>"
)

tpl = (root / "template.html").read_text()
html = tpl.replace("/*CSS*/", orig_css).replace("<!--MENU-->", menu_html)
(root / "public" / "index.html").write_text(html)
print("built", len(html) // 1024, "KB")
