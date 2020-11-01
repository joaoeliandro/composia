const express = require("express");
const cors = require("cors");

const api = require("./services/api");

const app = express();

app.use(cors());
app.use(express.json());

app.get('/', async (request, response) => {

  //const { data } = await api.get("/"); 

  return response.json({oi:123});
});

app.get('/estrofe/:input?', async (request, response) => {
  const {input} = request.query;  
  console.log(input)
  const { data } = await api.get(`/estrofe?input=${input}`); 

  return response.json(data);
});

app.listen(3333, () => {
  console.log('🚀 Server started!');
});
