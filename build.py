"""Generates public/index.html. Edit the MENU DATA below to change items/prices, then run: python3 build.py"""
import pathlib

root = pathlib.Path(__file__).parent
css = (root / "base.css").read_text()

# ---------- MENU DATA (prices in USD) ----------
# item: (name, description or None, price | (price1, price2))   Use "" for a missing price.

# DRINKS
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
NOT_COFFEE = ("Not Coffee", ["S", "R"], [
    ("Hot Tea", "Five Roses, Tanganda, Rooibos or Ginger.", ("", "3.00")),
    ("Hot Choc", "Rich and creamy hot chocolate.", ("2.00", "3.00")),
    ("Matcha Latte", "Finely ground Japanese green tea powder, served over milk of choice. Iced or hot.", ("", "5.00")),
    ("Chai Latte", "Spiced tea latte made with steamed milk and chai spice concentrate.", ("3.00", "5.00")),
    ("Dirty Chai", "A shot of espresso added to a traditional chai latte.", ("4.00", "5.00")),
    ("Mochaccino", "A shot of espresso with steamed milk and chocolate (syrup or cocoa powder).", ("3.00", "4.00")),
])
FREEZO = ("Freezo", ["R", "L"], [
    ("Freezo", "Refreshing, ice-blended drink available in coffee, mango and raspberry.", ("3.00", "4.00")),
])
MILKSHAKES = ("Milkshakes", ["R", "L"], [
    ("Milkshake", "Strawberry, chocolate, banana, lime, coffee, hazelnut, vanilla or bubblegum.", ("4.00", "5.00")),
])
EXTRAS = ("Extras &amp; Cold Drinks", None, [
    ("Flavoured Syrups", "Hazelnut, vanilla, caramel or salted caramel.", "1.00"),
    ("Milk Alternative", "Almond milk or oat milk.", "1.00"),
    ("Soft Drinks (Bashews)", None, "1.00"),
    ("Energy Drinks", None, "1.50"),
    ("Slush", None, "3.00"),
])

# FOOD
SAVOURY_L = ("Savoury", None, [
    ("Wors Roll", "Home made pure beef farmstyle wors in a roll with sauce of your choice.", "3.50"),
    ("Russian Roll", "Beef Russian in a roll with sauce of your choice.", "3.00"),
    ("Chip Roll", "Chips on a roll with sauce and cheese.", "2.50"),
    ("Chicken Wrap", "Chicken, lettuce and melted cheese in a warm flour wrap with sweet chilli, mayo or chilli sauce.", "4.50"),
    ("Beef Burger", "Home made pure beef patty with sauce of your choice, mayo, gherkins and cheese.", "4.00"),
    ("Chicken Burger", "Crumbed chicken patty with sauce of your choice, mayo, gherkins and cheese.", "4.00"),
    ("Salad", "Garden salad.", "1.50"),
])
SAVOURY_R = (None, None, [
    ("Samoosas", "Crispy deep fried pastry pocket filled with chicken mince or beef mince.", "0.50"),
    ("Spring Roll", "Vegetable.", "0.50"),
    ("Toasted Sandwich: Spicy Chicken Mayo", "On wholewheat bread.", "3.00"),
    ("Toasted Sandwich: Cheese &amp; Tomato", None, "2.00"),
    ("Toasted Steak Special", "Saucy steak with salad, sauces, cheese and spicy chips on white bread.", "5.00"),
    ("Chips", "Thin cut chips.", "1.50"),
    ("Pies", "Chicken &amp; mushroom, pepper steak, steak curry or sausage roll.", "3.00"),
])
SWEET = ("Sweet", None, [
    ("Cake Slice", "Carrot or chocolate.", "4.00"),
    ("Scones", "Freshly baked, light and fluffy traditional scone.", "0.50"),
])


def item(name, desc, price):
    d = f'<div class="desc">{desc}</div>' if desc else ""
    prices = price if isinstance(price, tuple) else (price,)
    p = "".join(f"<span>{x}</span>" for x in prices)
    return f'<div class="menu-item"><div><div class="name">{name}</div>{d}</div><div class="price-pair">{p}</div></div>'


def group(g):
    title, cols, items = g
    h = f"<h3>{title}</h3>" if title else '<h3 class="spacer" aria-hidden="true">&nbsp;</h3>'
    c = f'<div class="menu-cols">{"".join(f"<span>{x}</span>" for x in cols)}</div>' if cols else ""
    return f'<div class="menu-group">{h}{c}{"".join(item(*i) for i in items)}</div>'


def block(title, left, right):
    return (f'<h3 class="menu-block">{title}</h3><div class="menu-grid"><div>{left}</div><div>{right}</div></div>')


menu_html = (
    block("Drinks", group(HOT_COFFEE) + group(NOT_COFFEE), group(COLD_COFFEE) + group(MILKSHAKES) + group(FREEZO) + group(EXTRAS))
    + block("Food", group(SAVOURY_L) + group(SWEET), group(SAVOURY_R))
)

tpl = (root / "template.html").read_text()
html = tpl.replace("/*CSS*/", css).replace("<!--MENU-->", menu_html)
(root / "public" / "index.html").write_text(html)
print("built", len(html) // 1024, "KB")
