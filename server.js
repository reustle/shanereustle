var http = require('http');
var fs = require('fs');
require.paths.unshift('.');
var async = require('lib/async');

var template_cache = {};
function load_template(path, callback){
	if(typeof(template_cache[path]) === 'undefined'){
		fs.readFile(path, 'utf8', function(err, data){
			template_cache[path] = data;
			callback(err, data);
		});
	}else{
		callback(null, template_cache[path]);
	}
}

function error_handler(err, res){
	//TODO: Handle Errors
	if(err){
		res.end('ERROR');
		return true;
	}
}

http.createServer(function(req, res){
	
	var url = req.url.split('/');
	
	if(req.url == '/'){
		// Match URL: /
		load_template('templates/index.html', function(err, template){
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.end(template + '\n');
		});
	
	}else if( /\/static\//.test(req.url)){
		// Match URL: /static/
		
		types = {
			'css' : 'text/css',
			'gif' : 'image/gif',
			'jpeg' : 'image/jpeg',
			'jpg' : 'image/jpeg',
			'js' : 'application/javascript',
			'png' : 'image/png'
		}
		
		var filename = req.url.replace(/\//, '');
		var filetype = filename.split('.');
		filetype = types[filetype[filetype.length -1]];
		
		fs.readFile(filename, 'binary', function(err, data){
			if(err){
				res.writeHead(404, {'Content-Type': 'plain/text'});
				res.end();
			}else{
				res.writeHead(200, {'Content-Type': filetype});
				res.write(data, 'binary');
				res.end();
			}
		});
	
	}else if( /^\/blog\/?$/.test(req.url)){
		// Match URL: /blog/
		
		async.parallel({
			'template': function(callback){
				load_template('templates/blog.html', callback);
			},
			'blog_index': function(callback){
				load_template('templates/blog_index.html', callback);
			}
		}, function(err, response){
			var template = response.template;
			template = template.replace('{{title}}', 'Blog &#124; Shane Reustle');
			template = template.replace('{{body}}', response.blog_index);
			
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.end(template + '\n');
			
		});
		
	}else if( /^\/blog\//.test(req.url)){
		// Match URL: /blog/{article}/
		
		if(url[2] == 'purge'){
			template_cache = {};
			res.writeHead(200, {'Content-Type': 'text/plain'});
			res.end('Purged Cache\n');
			return false;
		}
		
		async.parallel({
			'template': function(callback){
				load_template('templates/blog.html', callback);
			},
			'entry': function(callback){
				var entry_filename = 'templates/blog_entries/' + url[2] + '.html';
				load_template(entry_filename, callback);
			}
		}, function(err, response){
			if(error_handler(err, res)){return}
			
			var entry_title = response.entry.split('\n')[0];
			entry_title = /<h1>(.+)<\/h1>/.exec(entry_title)[1];
			
			var template = response.template;
			template = template.replace('{{title}}', entry_title + ' &#124; Shane Reustle');
			template = template.replace('{{body}}', response.entry);
			
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.end(template + '\n');
			
		});
	
	}else if( /favicon\.ico/.test(req.url)){
		// Match URL: /favicon.ico
		
		// Return empty_gif
		res.writeHead(200, {'Content-Type': 'image/gif'});
		res.end('\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\xf0\x01\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b', 'binary');
		
	}else{
		// Error: 404
		res.writeHead(404, {'Content-Type': 'text/plain'});
		res.end();

	}
	
}).listen(8001, '127.0.0.1');
console.log('ShaneReustle.com app listening on 127.0.0.1:8001');

