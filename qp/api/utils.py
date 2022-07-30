import json
from django.core import serializers
from django.http import HttpResponse, Http404
from django.utils.text import slugify

from qp.settings import BASE_DIR

from qp.world.models import qpWorldStyle

def download_style(request, pk):
    try:
        styleobj = qpWorldStyle.objects.filter(
            pk=int(pk)
        )
        filename = "style_%s_%s.json" % (
            str(slugify(styleobj.first().world.name)),
            str(slugify(styleobj.first().name))
        )
        serialized = serializers.serialize("json", styleobj)
        jsoned = json.loads(serialized)
        jsoned[0].pop("pk", None)
        jsoned[0].pop("model", None)
        jsoned[0]["fields"].pop("name", None)
        jsoned[0]["fields"].pop("world", None)
        jsoned[0]["fields"].pop("is_active", None)
        stringed = json.dumps(jsoned[0])
        response = HttpResponse(stringed, content_type="application/json,charset=utf8")
        response["Content-Disposition"] = "attachment; filename={0}".format(filename)
        return response
    except Exception as e:
        print("Error on download_style : ", e)
        raise Http404