(function(){
	
	var banner_el = document.createElement('div');
	var wrapper = document.getElementsByTagName('div')[0];
	var banner = '<div id="blog_banner"><div class="wrapper"><a href="/blog/">Shane <span class="red">Reustle</span></a><div class="right">';
	banner += '<a class="icons tumblr" title="Blog Index" href="/blog/"></a>';
	banner += '<a class="icons twitter" title="Twitter" href="http://twitter.com/reustle/"></a>';
	banner += '<a class="icons github" title="GitHub" href="http://github.com/reustle/"></a>';
	banner += '<a class="icons linkedin" title="LinkedIn" href="http://linkedin.com/in/reustle/"></a>';
	banner += '<a class="icons google" title="Google" href="http://profiles.google.com/sreustle/"></a>';
	banner += '<a class="icons forrst" title="Forrst" href="http://forrst.com/people/reustle/"></a>';
	banner += '<a class="icons stackoverflow" title="Stack Overflow" href="http://stackoverflow.com/users/206506/shane-reustle"></a>';
	banner += '<a class="icons email" title="Email" href="mailto:sreustle@gmail.com"></a>';
	banner += '<a class="icons rss" title="RSS" href="http://shanereustle.com/blog/rss.xml"></a>';
	banner += '</div></div></div>';
	banner_el.innerHTML = banner;
	wrapper.parentNode.insertBefore(banner_el, wrapper);

})();

