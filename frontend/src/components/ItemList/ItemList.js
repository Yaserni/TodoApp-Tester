import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ItemList.css';

const API = 'http://localhost:5000';

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState('');
  const [editId, setEditId] = useState(null);
  const [editText, setEditText] = useState('');

  const fetchItems = async () => {
    const res = await axios.get(`${API}/items`);
    setItems(res.data);
  };

  useEffect(() => {
    document.title = 'Items Page';
    fetchItems();
  }, []);

  const addItem = async () => {
    if (!newItem.trim()) return;
    const res = await axios.post(`${API}/items`, { name: newItem });
    setItems([...items, res.data]);
    setNewItem('');
  };

  const deleteItem = async (id) => {
    await axios.delete(`${API}/items/${id}`);
    setItems(items.filter(i => i.id !== id));
  };

  const updateItem = async () => {
    const res = await axios.put(`${API}/items/${editId}`, { name: editText });
    setItems(items.map(i => (i.id === editId ? res.data : i)));
    setEditId(null);
    setEditText('');
  };

  return (
    <div className="todo-container">
      <h2>Todo List</h2>
      <div className="todo-inputs">
        <input
          value={newItem}
          onChange={e => setNewItem(e.target.value)}
          placeholder="Add new item"
        />
        <button onClick={addItem}>Add</button>
      </div>
      <ul className="todo-list">
        {items.map(i => (
          <li key={i.id}>
            {editId === i.id ? (
              <>
                <input
                  value={editText}
                  onChange={e => setEditText(e.target.value)}
                />
                <button onClick={updateItem}>Save</button>
              </>
            ) : (
              <>
                <span>{i.name}</span>
                <button onClick={() => {
                  setEditId(i.id);
                  setEditText(i.name);
                }}>Edit</button>
                <button onClick={() => deleteItem(i.id)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;
