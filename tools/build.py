"""Baut index.html aus src/app.html: bettet jsPDF und das App-Icon ein (eine Datei, offline lauffähig)."""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "src/app.html").read_text(encoding="utf-8")
jspdf = (root / "vendor/jspdf.umd.min.js").read_text(encoding="utf-8")
icon = "data:image/png;base64," + base64.b64encode((root / "icon-180.png").read_bytes()).decode()
html = html.replace("<!--JSPDF-->", jspdf).replace("<!--ICON-->", icon)
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html:", len(html), "Zeichen")
