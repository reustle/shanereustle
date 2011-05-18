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

http.createServer(function(req, res){
	
	var url = req.url.split('/');
	
	// TODO: Match urls with regex
	if(req.url == '/'){
		// Match URL: /
		load_template('templates/index.html', function(err, template){
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.end(template + '\n');
		});
		
	}else if(url[1] == 'blog'){
		if(url.length == 2 || url[2].length < 1){
			// Match URL: /blog/
			
			function callback(){
				console.log('callme');
			}
			
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
			
		}else{
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
				// TODO: This is ugly. Regex maybe?
				var entry_title = response.entry.split('\n')[0].replace('<h1>', '').replace('</h1>', '');
				
				var template = response.template;
				template = template.replace('{{title}}', entry_title + ' &#124; Shane Reustle');
				template = template.replace('{{body}}', response.entry);
				
				res.writeHead(200, {'Content-Type': 'text/html'});
				res.end(template + '\n');
				
			});
			
		}
		
	}else if(url[1] == 'favicon.ico'){
		// Match URL: /favicon.ico
		res.writeHead(200, {'Content-Type': 'image/gif'});
		// EmptyGif
		res.end('\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\xf0\x01\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b', 'binary');
		
	}else{
		// Error: 404
		res.writeHead(404, {'Content-Type': 'text/plain'});
		res.end();

	}
	
}).listen(1337, '127.0.0.1');
console.log('ShaneReustle.com app listening on 127.0.0.1:1337');

