const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

let items = [];
let users = [{ username: 'admin', password: '1234' }];

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username && u.password === password);
  user ? res.json({ success: true }) : res.status(401).json({ error: 'Invalid credentials' });
});

app.get('/items', (req, res) => res.json(items));

app.post('/items', (req, res) => {
  const { name } = req.body;
  if (!name) return res.status(400).json({ error: 'Name is required' });
  const newItem = { id: Date.now(), name };
  items.push(newItem);
  res.status(201).json(newItem);
});

app.put('/items/:id', (req, res) => {
  const { id } = req.params;
  const { name } = req.body;
  const item = items.find(i => i.id == id);
  if (!item) return res.status(404).json({ error: 'Item not found' });
  item.name = name;
  res.json(item);
});

app.delete('/items/:id', (req, res) => {
  const { id } = req.params;
  const index = items.findIndex(i => i.id == id);
  if (index === -1) return res.status(404).json({ error: 'Item not found' });
  items.splice(index, 1);
  res.json({ success: true });
});

if (require.main === module) {
  app.listen(PORT, () => console.log(`🚀 Backend running on http://localhost:${PORT}`));
} else {
  module.exports = app; // for testing
}
