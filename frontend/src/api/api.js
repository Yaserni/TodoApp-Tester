import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

// Login
export const loginUser = (username, password) =>
  axios.post(`${BASE_URL}/login`, { username, password });

// Items
export const fetchItems = () =>
  axios.get(`${BASE_URL}/items`);

export const createItem = (name) =>
  axios.post(`${BASE_URL}/items`, { name });

export const updateItem = (id, name) =>
  axios.put(`${BASE_URL}/items/${id}`, { name });

export const deleteItem = (id) =>
  axios.delete(`${BASE_URL}/items/${id}`);
