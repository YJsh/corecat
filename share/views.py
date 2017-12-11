# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from models import FileNode

import json
import operator
import urllib
# Create your views here.


def getTreeNodes(nodes, parent, host):
    for node in nodes:
        treeNode = {
            "id": node.id,
            "name": node.name,
            "open": False,
        }
        if node.isDir:
            treeNode["isParent"] = True
            treeNode["children"] = []
            getTreeNodes(node.dir.all(), treeNode, host)
        else:
            treeNode["isParent"] = False
            treeNode["fileUrl"] = "http://%s/share/downloadFile/%s" \
                                  % (host, node.id)

        parent["children"].append(treeNode)
    parent["children"].sort(key=operator.itemgetter("isParent", "name"),
                            reverse=True)


def getDirTree(request):
    nodes = FileNode.objects.filter(parent=None)
    dirTree = {
        "id": -1,
        "name": u"共享目录（点击预览）",
        "isParent": True,
        "open": True,
        "children": []
    }

    getTreeNodes(nodes, dirTree, request.get_host())
    return HttpResponse(json.dumps([dirTree]))


def dropNode(request):
    nodeIds = json.loads(request.POST.get("ids", []))
    parentId = request.POST.get("parentId", -1)
    try:
        parent = None
        if int(parentId) != -1:
            parent = FileNode.objects.get(id=parentId)
        for nodeId in nodeIds:
            node = FileNode.objects.get(id=nodeId)
            node.parent = parent
            node.save()
    except ObjectDoesNotExist:
        pass
    return HttpResponse()


def renameNode(request):
    nodeId = request.POST.get("id", -1)
    nodeName = request.POST.get("name", "")
    try:
        node = FileNode.objects.get(id=nodeId)
        node.name = nodeName
        node.save()
    except ObjectDoesNotExist:
        pass

    return HttpResponse()


def removeTree(node):
    for node in node.dir.all():
        removeTree(node)

    if not node.isDir:
        node.file.delete()
    node.delete()


def removeNode(request):
    nodeId = request.POST.get("id", -1)
    try:
        node = FileNode.objects.get(id=nodeId)
        removeTree(node)
    except ObjectDoesNotExist:
        pass

    return HttpResponse()


def addDir(request):
    parentId = request.POST.get("parentId", -1)
    nodeName = request.POST.get("name", "")
    parent = None
    try:
        parent = FileNode.objects.get(id=parentId)
    except ObjectDoesNotExist:
        pass

    node = FileNode(isDir=True, name=nodeName, parent=parent)
    node.save()

    return HttpResponse(json.dumps(node.id))


def addFile(request):
    nodeFile = request.FILES.get("uploadFile", "")
    name = nodeFile.name

    node = FileNode(name=name, file=File(nodeFile))
    node.save()

    url = "http://%s/share/downloadFile/%s" % (request.get_host(), node.id)
    return HttpResponse(json.dumps({"id": node.id, "fileUrl": url}))


def downloadFile(request, nodeId):
    def fileIter(fileNode, chunkSize=512):
        fileNode.file.open("rb")
        chunk = fileNode.file.read(chunkSize)
        while chunk:
            yield chunk
            chunk = fileNode.file.read(chunkSize)
        fileNode.file.close()

    try:
        node = FileNode.objects.get(id=nodeId)
        response = StreamingHttpResponse(fileIter(node))
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment;filename='%s'" \
                                          % urllib.quote(node.name.encode("utf-8"))
        return response
    except ObjectDoesNotExist:
        return HttpResponse()
