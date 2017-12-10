import axios from 'axios'
import qs from 'qs'

const instance = axios.create({
  baseURL: 'http://localhost:8000',
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
  return post("share/getDirTree");
};

export const deleteNode = function(id) {
  return post("share/deleteNode", {"id":id});
};

export const renameNode = function(id, name) {
  return post("share/renameNode", {"id":id, "name":name});
};
