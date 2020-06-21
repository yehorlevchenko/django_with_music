# Music with Django

### How to run
1. Git clone https://github.com/yehorlevchenko/django_with_music.git
2. docker-compose build
3. docker-compose up


### Works Single View
This is a view showing all stored works and capable of uploading new entries.
* URL - 0.0.0.0:8000/music/


### Works Single View API
This is a REST API endpoint representing works and capable of searching for certain compositions.
* URL - 0.0.0.0:8000/api/music/works/ - will return 10 latest works as a JSON.
* URL - 0.0.0.0:8000/api/music/works/ - with body {"iswc": "T9204649558,T0101974597"} will return search results.


### Q&A
> Describe briefly the matching and reconciling method chosen.

Matching and reconciling is done by overriden create method in Work model:
1. Attempt to create an object from a new work data;
2. Either get a new object or an old one from DB (from an overriden create model method);
3.1. New object will be saved, updated it with contributors data, saved again;
3.2. Duplicated object will be updated with ISWC (if missing) and contributors.

> We constantly receive metadata from our providers, how would you automatize the process?

Seems automated with the approach described above: search for duplicates before createing new records.

> Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?

Response time will grow up with:
1. Bigger queries (more ISWC per request)
2. Bigger table

> If not, what would you do to improve it?

Might speed up searching by using index for ISWC lookup.


### Side notes
1. Contributors are another entity with many-to-many relation to works. Looks more optimal in current context.
2. Had fun.

