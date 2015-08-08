var express = require('express');
//var session = require('cookie-session');
//var bodyParser = require('body-parser');
//var urlencodedParser = bodyParser.urlencoded({ extended: false });

var app = express();

var PythonShell = require('python-shell');

app.get('/Test', function(req, res) { 

	PythonShell.run('interface.py', {args: [1]}, function (err,result) {
		if (err) {
			console.log(err);
		}
		res.render('page.ejs', {msg: result});
		console.log(result);
	});
})
.listen(8080);