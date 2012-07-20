var _vrq = _vrq || [];

(function(){
	
	var insert_banner = function(){
		var banner_el = document.createElement('div');
		var wrapper = document.getElementsByTagName('div')[0];
		var banner = [
			'<div id="banner"><div class="wrapper">',
			'<a href="/">Shane<span class="red">Reustle</span></a>',
			'<span class="soft"> is <a href="/blog/freelance-software-engineer.html">available for hire</a>!</span>',
			'<div class="right">',
			'<a class="icons twitter" title="Twitter" href="http://twitter.com/reustle/"></a>',
			'<a class="icons github" title="GitHub" href="http://github.com/reustle/"></a>',
			'<a class="icons forrst" title="Forrst" href="http://forrst.com/people/reustle"></a>',
			'<a class="icons linkedin" title="LinkedIn" href="http://linkedin.com/in/reustle/"></a>',
			'<a class="icons email" title="Email" href="mailto:me@shanereustle.com"></a>',
			'</div></div></div>'
		].join('');
		banner_el.innerHTML = banner;
		wrapper.parentNode.insertBefore(banner_el, wrapper);
	};
	
	var insert_return_link = function(){
		var return_link = document.createElement('p');
		return_link.innerHTML = '<a href="/">&laquo; View all posts</a>';
		
		document.getElementById('wrapper').appendChild(return_link.firstChild);
	};

	var load_google_analytics = function(){
		var new_script = document.createElement('script');
		var first_script = document.getElementsByTagName('script')[0];
		new_script.async = true;
		new_script.src = '../static/js/ga.js';
		first_script.parentNode.insertBefore(new_script, first_script);
	};
	
	// Insert the page header
	insert_banner();
	
	// Call GA
	load_google_analytics();
	
	// Add a return link if we're on a post
	var url_pieces = window.location.toString().split('.');
	var url_ends_with = url_pieces[url_pieces.length - 1];
	if(url_ends_with && url_ends_with == 'html'){
		insert_return_link();
	}
	
})();

