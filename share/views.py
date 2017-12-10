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
# Create your views here.


def getTreeNodes(nodes, parent):
    for node in nodes:
        treeNode = {
            "id": node.id,
            "name": node.name,
            "isParent": False,
            "open": False,
            "children": []
        }
        if node.isDir:
            treeNode["isParent"] = True
            getTreeNodes(node.dir.all(), treeNode)

        parent["children"].append(treeNode)
    parent["children"].sort(key=lambda child: child["name"])


def getDirTree(request):
    nodes = FileNode.objects.filter(parent=None)
    dirTree = {
        "id": -1,
        "name": u"共享目录",
        "isParent": True,
        "open": True,
        "children": []
    }

    getTreeNodes(nodes, dirTree)
    return HttpResponse(json.dumps([dirTree]))


def renameNode(request):
    nodeId = request.POST.get("id", -1)
    nodeName = request.POST.get("name", "")
    print nodeId, nodeName
    try:
        node = FileNode.objects.get(id=nodeId)
        node.name = nodeName
        node.save()
    except ObjectDoesNotExist:
        pass

    return HttpResponse()


def deleteTree(node):
    if not node.isDir:
        # 删除文件
        pass

    for node in node.dir.all():
        node.file.delete()


def deleteNode(request):
    nodeId = request.POST.get("id", -1)
    try:
        node = FileNode.objects.get(id=nodeId)
        deleteTree(node)
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

    return HttpResponse()


def addFile(request):
    nodeFile = request.FILES.get("uploadFile", "")
    name = nodeFile.name

    node = FileNode(name=name, file=File(nodeFile))
    node.save()

    return HttpResponse(json.dumps(node.id))
