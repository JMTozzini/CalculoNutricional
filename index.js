var express = require('express');
var session = require('cookie-session');
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

var app = express();

var PythonShell = require('python-shell');
var pyshell = new PythonShell('test.py');



app.get('/Test', function(req, res) { 

	PythonShell.run('test.py', {args: ['Bonjour', ' JM']}, function (err,result) {
		if (err) {
			console.log(err);
		}
		res.render('page.ejs', {msg: result[0] + ' ' + result[1]});
		console.log(result);
	});
})
.listen(8080);