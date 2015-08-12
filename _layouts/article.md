---
layout: base
tab: articles
---

{% if page.draft %}
<div class='alert alert-warning text-center'>
	<strong>DRAFT POST</strong>
</div>
{% endif %}

<h1>{{ page.title }}</h1>

{{ content }}

<div class='row'>
	
	<div class='col-md-4'>
		<a href='/blog/' class='btn btn-default footer-action'><span class='glyphicon glyphicon-chevron-left'></span> Back to Article List</a>
	</div>
	
	<div class='col-md-4 article-date text-center'>
		{{ page.date | date: "%b %-d, %Y" }}
	</div>
	
	<div class='col-md-4 text-right'>
		<a href='http://twitter.com/reustle' class='btn btn-default footer-action'>Follow on Twitter</a>
	</div>

</div>

