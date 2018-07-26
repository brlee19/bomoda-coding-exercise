const express = require('express');
const axios = require('axios');
const app = express();
const path = require('path');

app.set('view engine', 'pug');
app.use(express.static(path.join(__dirname, "public")));

app.get('/', async (req, res) => {
  const url = 'http://127.0.0.1:5000/status';
  const {data} = await axios.get(url);
  console.log(data);
  res.render('index', data);
});

app.listen(3000, () => console.log('App listening on port 3000!'));