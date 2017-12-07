# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from models import FileNode
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


def getDirTree(request):
    nodes = FileNode.objects.fileter(parent=None)
    dirTree = [{
        "id": -1,
        "name": u"共享目录",
        "isParent": True,
        "open": True,
        "children": []
    }]

    getTreeNodes(nodes, dirTree)


def renameNode(request):
    nodeId = request.POST.get("id", -1)
    nodeName = request.POST.get("name", "")
    try:
        node = FileNode.objects.get(id=nodeId)
        node.name = nodeName
        node.save()
    except ObjectDoesNotExist:
        return


def deleteTree(node):
    if not node.isDir:
        # 删除文件
        pass

    for node in node.dir.all():
        deleteTree(node)


def deleteNode(request):
    nodeId = request.POST.get("id", -1)
    try:
        node = FileNode.objects.get(id=nodeId)
        deleteTree(node)
    except ObjectDoesNotExist:
        return


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


def addFile(request):
    nodeName = ""
    nodeFile = ""
    node = FileNode(name=nodeName, file=nodeFile)
    node.save()
