import json
from django.shortcuts import render
from django.templatetags.static import static

from qp.settings import DEBUG

def app(request):
    css = []
    js = []
    stage = "dev" if DEBUG else "pro"
    # ===---
    with open("frontend/webpack-%s.json" % (stage), "r") as f:
        wp = json.load(f)
        for chunk in wp["chunks"]["app"]:
            if chunk.startswith("css"):
                css.append(
                    static("/vue/%s/%s" % (stage, chunk))
                )
            elif chunk.startswith("js"):
                js.append(
                    static("/vue/%s/%s" % (stage, chunk))
                )
    # ===---
    context = {
        "css": css,
        "js": js
    }
    return render(request, "app.html", context)