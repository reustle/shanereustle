---
layout: blog-index
---

# Articles

{% for post in site.posts %}{% unless post.draft %}* [{{ post.title }}]({{ post.url | prepend: site.baseurl }}) _{{ post.date | date: '%b %-d, %Y' }}_
{% endunless %}{% endfor %}

<a href='http://twitter.com/reustle' class='btn btn-default footer-action'>Follow on Twitter</a>

