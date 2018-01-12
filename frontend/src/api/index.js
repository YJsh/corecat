import axios from 'axios'
import qs from 'qs'

const instance = axios.create({
  withCredentials: true,
});

const post = function(url, data=null) {
  if (data) {
    return instance.post(url, qs.stringify(data));
  }
  else {
    return instance.post(url);
  }
};

export const getDirTree = function() {
  return post("/api/share/getDirTree");
};

export const dropNode = function(ids, parentId) {
  return post("/api/share/dropNode", {"ids":JSON.stringify(ids), "parentId":parentId});
};

export const removeNode = function(id) {
  return post("/api/share/removeNode", {"id":id});
};

export const renameNode = function(id, name) {
  return post("/api/share/renameNode", {"id":id, "name":name});
};

export const downloadFile = function(id) {
  return post("/api/share/downloadFile", {"id":id});
};

export const addDir = function(parentId, name) {
  return post("/api/share/addDir", {"parentId":parentId, "name":name});
};

export const login = function(password) {
  return post("/api/login", {"password":password});
};
