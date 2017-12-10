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
    parent["children"].sort(key=lambda child: child["name"])


def getDirTree(request):
    nodes = FileNode.objects.filter(parent=None)
    dirTree = {
        "id": -1,
        "name": u"共享目录（点击下载）",
        "isParent": True,
        "open": True,
        "children": []
    }

    getTreeNodes(nodes, dirTree, request.get_host())
    return HttpResponse(json.dumps([dirTree]))


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


def deleteTree(node):
    if not node.isDir:
        node.file.delete()
        node.delete()

    for node in node.dir.all():
        deleteTree(node)


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


def downloadFile(request, nodeId):
    print "download", nodeId
    def fileIter(fileNode, chunkSize=512):
        fileNode.file.open("r")
        chunk = fileNode.file.read(chunkSize)
        while chunk:
            print(chunk)
            yield chunk
            chunk = fileNode.file.read(chunkSize)
        fileNode.file.close()

    try:
        node = FileNode.objects.get(id=nodeId)
        response = StreamingHttpResponse(fileIter(node))
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment;filename='%s'" % node.name
        return response
    except ObjectDoesNotExist:
        return HttpResponse()
