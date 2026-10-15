import base64, datetime, pathlib, subprocess

root = pathlib.Path(__file__).resolve().parent.parent
b64 = lambda p: base64.b64encode((root / p).read_bytes()).decode()
try:
    n = int(subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip() or 0) + 1
except Exception:
    n = 0
version = f"1.{n} · {datetime.date.today().strftime('%d.%m.%Y')}"


def baue(quelle, ziel, icon):
    html = (root / quelle).read_text(encoding="utf-8")
    html = html.replace("<!--JSPDF-->", (root / "vendor/jspdf.umd.min.js").read_text(encoding="utf-8"))
    html = html.replace("<!--MSAL-->", (root / "vendor/msal-browser-3.28.1.min.js").read_text(encoding="utf-8"))
    html = html.replace("<!--EHANDWERK-->", "data:image/jpeg;base64," + b64("brand/e-handwerk.jpg"))
    html = html.replace("<!--VERSION-->", version)
    html = html.replace("<!--ICON-->", "data:image/png;base64," + b64(icon))
    html = html.replace("<!--ICON_EVSE-->", "data:image/png;base64," + b64("evse/icon-180.png"))
    html = html.replace("<!--ICON_BAU-->", "data:image/png;base64," + b64("baustelle/icon-180.png"))
    html = html.replace("<!--LOGO_HELL-->", "data:image/png;base64," + b64("brand/logo-hell.png"))
    html = html.replace("<!--LOGO_DUNKEL-->", "data:image/png;base64," + b64("brand/logo-dunkel.png"))
    for w in (400, 600, 700, 800):
        html = html.replace(f"<!--F{w}-->", b64(f"vendor/fonts/manrope-latin-{w}-normal.woff2"))
    (root / ziel).write_text(html, encoding="utf-8")
    print(f"{ziel}: {len(html)} Zeichen")


baue("src/start.html", "index.html", "icon-180.png")
baue("src/app.html", "evse/index.html", "evse/icon-180.png")
baue("src/baustelle.html", "baustelle/index.html", "baustelle/icon-180.png")
