'use strict'

var express = require('express');
var url = require('url');
var bodyParser = require('body-parser')

var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}))

//Helloworld
app.get('/', function (req, res) {
  res.send('Hello world');
});

//GET name
app.get('/:name', function (req, res) {
  var name = req.params['name'];
  console.log('Name: ' + name);

  res.send('Hello ' + name + '\n')
});


app.get('/add', function (req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;

  var a = parseInt(query['a']);
  var b = parseInt(query['b']);
  var result = a + b;

  console.log(a, b);
  console.log(query);

  res.send(result.toString() + '\n');
})

app.post('/add', function (req, res) {
  console.log(req.body);
  res.send(204).end();
});


app.listen(3000);
