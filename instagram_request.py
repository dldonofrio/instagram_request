import requests
# Allows us to make HTTP requests
import json
# Allows us to parse JSON data

def instagram_pull(username, number_of_posts):
	insta_posts = []
	r = requests.get('https://instagram.com/' + username + '?__a=1')
	if r.status_code == requests.codes.ok:
		for x in range(0, number_of_posts):
			insta_JSON = r.json()
			post = {
				'url_img': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['display_url'],
				'url_post': 'https://www.instagram.com/p/' + insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['shortcode'],
				'text': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['edge_media_to_caption']['edges'][0]['node']['text'],
				'likes': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['edge_liked_by']['count']
			}
			insta_posts.append(post)	
	else:
		print(r.status_code)
		r.raise_for_status()
	print(insta_posts)
	return insta_posts

instagram_pull('doner_agency', 3)
