---
title: Newsletter
layout: base
tab: newsletter
photos:
  -
    url: photo14.jpg
    title: Bagan, Myanmar
  -
    url: photo3.jpg
    title: Machu Picchu, Peru
  -
    url: photo2.jpg
    title: Flam, Norway
---

# Biannual Updates

Every 6 months, I send out a newsletter to recap my thoughts, projects, and adventures. I find this update style much easier to digest than the information overload that is social media. I'll also include a couple photos I've taken along the way.

<form action='https://tinyletter.com/reustle' method='post' target='_blank'>
	<div class='input-group'>
		<input type='email' value='' name='email' class='form-control' id='tlemail' placeholder='Email Address'/>
		<span class='input-group-btn'>
			<input type='submit' value='Subscribe' class='button btn btn-primary'>
		</span>
	</div>
</form>

<br/>

<div class='newsletter-photos'>
	{% for photo in page.photos %}
		<div class='col-md-4'>
			<a href='/#about'>
				<img src='/static/images/photos/{{ photo.url }}' title='{{ photo.title }}' class='img-responsive'>
			</a>
		</div>
	{% endfor %}
</div>

