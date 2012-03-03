(function(){
	
	var insert_banner = function(){
		var banner_el = document.createElement('div');
		var wrapper = document.getElementsByTagName('div')[0];
		var banner = '<div id="blog_banner"><div class="wrapper"><a href="/blog/">Shane<span class="red">Reustle</span></a><div class="right">';
		banner += '<a class="icons twitter" title="Twitter" href="http://twitter.com/reustle/"></a>';
		banner += '<a class="icons github" title="GitHub" href="http://github.com/reustle/"></a>';
		banner += '<a class="icons linkedin" title="LinkedIn" href="http://linkedin.com/in/reustle/"></a>';
		banner += '<a class="icons google" title="Google" href="http://profiles.google.com/sreustle/"></a>';
		banner += '<a class="icons email" title="Email" href="mailto:sreustle@gmail.com"></a>';
		banner += '<a class="icons rss" title="RSS" href="http://shanereustle.com/blog/rss.xml"></a>';
		banner += '</div></div></div>';
		banner_el.innerHTML = banner;
		wrapper.parentNode.insertBefore(banner_el, wrapper);
	};
	
	var insert_return_link = function(){
		var return_link = document.createElement('p');
		return_link.innerHTML = '<a href="/blog/">&laquo; View all posts</a>';
		
		document.getElementById('wrapper').appendChild(return_link.firstChild);
	};
	
	insert_banner();
	
	var url_ends_with = window.location.toString().split('.');
	url_ends_with = url_ends_with[url_ends_with.length - 1];
	if(url_ends_with && url_ends_with == 'html'){
		insert_return_link();
	}
	
})();

