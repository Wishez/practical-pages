// 1. Open cache
// 2. Cache files
// 3. Confirm whether all the requored assets are cached or not

const CACHE_NAME = 'filipp-zhuravlev-cache-v1';
function _createUrl(url) {
	return `${current_static_url}url`

}
const urlsToCache = [
	_createUrl('/'),
	_createUrl('css/main.css'),
	_createUrl('js/main.js')
];

self.addEventListener('install', e => {
	e.waitUntil(
		caches
			.open(CACHE_NAME)
			.then(cache => {
				return cache.addAll(urlsToCache);
			})
	);	
});

self.addEventListener('fetch', e => {
	e.respondWith(
		caches.match(e.request)
			.then(resp => {
				if (resp) 
					return resp;

				const fetchRequest = e.request.clone();

				return fetch(fetchRequest)
					.then(resp => {
						if(!resp || resp.status !== 200 || resp.type !== 'basic') {
			              return resp;
			            }
			            var responseToCache = resp.clone();
			            
						caches.open(CACHE_NAME)
							.then(cache => {
								cache.put(e.request, responseToCache);
							});

						return resp;
					});


			})
	);
});