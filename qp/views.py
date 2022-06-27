import json
import math
import hashlib
from django.shortcuts import render
from django.templatetags.static import static

from qp.settings import DEBUG

def app(request):
    css = []
    js = []
    stage = "dev" if DEBUG else "pro"
    print("-------------------------------")
    print(request.headers["User-Agent"])
    print(hashlib.sha1(request.headers["User-Agent"].encode()).hexdigest())
    # ===---
    print("2 147 483 647")
    points = 32767
    print(math.floor((math.sqrt(((points / 1024) * 8) + 1) - 1) / 2))
    # ===---
    try:
        with open("frontend/webpack-%s.json" % (stage), "r") as f:
            wp = json.load(f)
            for chunk in wp["chunks"]["app"]:
                if chunk.startswith("css"):
                    css.append(
                        static("vue/%s/%s" % (stage, chunk))
                    )
                elif chunk.startswith("js"):
                    js.append(
                        static("vue/%s/%s" % (stage, chunk))
                    )
    except Exception as e:
        print("Error on app : ", e)
    # ===---
    context = {
        "css": css,
        "js": js
    }
    return render(request, "app.html", context)