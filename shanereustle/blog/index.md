---
layout: blog-index
---

# Articles

{% for post in site.posts %}* [{{ post.title }}]({{ post.url | prepend: site.baseurl }}) _{{ post.date | date: '%b %-d, %Y' }}_
{% endfor %}

<a href='http://twitter.com/reustle' class='btn btn-default footer-action'>Follow on Twitter</a>

