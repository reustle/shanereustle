---
title: Simple Site Scraping With NodeJS And JSDom
---

I've been playing with Node on and off over the past couple of weeks and it's really starting to grow on me. I initially looked into it because I'm intrigued by the thought of using one language for both client and server side coding. Turns out, as people have pointed out, it's fast too. Really fast. I spent some time messing around with the hello world examples, built some simple APIs, and even gave a talk at [BarCamp Boston](http://barcampboston.org) about the basics of Node, but I want to do something that takes advantage of the JS nature of Node. Let's start off with a simple site scraping example where we pull the current temperature. As the examples get more complex, we'll be able to leverage libraries like jQuery to do more complex scraping in an already familiar syntax.

For this first example, you're going to need the Node packages Request and [JSDOM](https://github.com/tmpvar/jsdom). You can get both of these using [npm](http://npmjs.org/) (npm install request jsdom). This is a pretty short example (9 lines), so I'll skip right to the code.

{% highlight javascript %}
var request = require('request');
var jsdom = require('jsdom');

var req_url = 'http://www.localweather.com/weather/?pands=10001';

request({uri: req_url}, function(error, response, body){
	if(!error && response.statusCode == 200){
		var window = jsdom.jsdom(body).createWindow();
		
		var temp = window.document.getElementsByClassName('u-eng')[0].innerHTML;
		console.log(temp);
	}
});
{% endhighlight %}

We started off by requiring **Request** and **JSDOM**. We then made the request to the site we're going to scrape and set a callback function to handle the response. Inside that callback, we make sure the request was successful by checking the HTTP status code. If the request was successful, we pipe the response into JSDOM to render a duplicate version of the DOM locally so that we can interact with it. Now that we have a local copy of the webpage, we can do whatever we want with it. We only need 1 line of code to extract the current temperature from the page, which we send back to the console for the user to see.

After playing around with this script for awhile, you may have noticed this method works well but often throws strange JS errors depending on what site you try to scrape. Let's take a step back and think about what we're doing. We make a request to a page and parse a copy of its response html locally. The problem with this method is that there are usually resources requested using relative links (/static/jquery.js) and not absolute links (http://example.com/static/jquery.js). Since these resources do not exist locally, they cannot be loaded, which ends up causing errors later on in the page. We can manually go in and patch up these broken links by either modifying the links in the response before parsing it, or including the scripts in your new DOM before parsing the response. Keep in mind, there may be AJAX requests that use relative links as well, so keep an eye on the network traffic.

This should give you a good head start on scraping sites with NodeJS and JSDOM. JSDOM does a great job with this task, but doesn't seem to be built for this type of work. If you need to scrape some JS generated content, you may need to do some work. If you have a large site scraping project, you may want to check out [NodeIO](http://node.io) and [PhantomJS](http://phantomjs.org). NodeIO is a screen scraping framekwork built on top of Node and PhantomJS is a headless implementation of WebKit with a JS API. I would use PhantomJS if I needed to do any large scraping projects because it lets you interact with a real browser which renders all of the JS content. Keep an eye out for a review of PhantomJS in the future.

