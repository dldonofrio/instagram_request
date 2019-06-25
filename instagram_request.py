import requests
# Allows us to make HTTP requests
import json
# Allows us to parse JSON data

def instagram_pull(username, number_of_posts):
	insta_posts = []
	r = requests.get('https://instagram.com/' + username + '?__a=1')
	# Concatenates the user-defined username into the request URL
	if r.status_code == requests.codes.ok:
		# Checks to make sure response code is 200
		for x in range(0, number_of_posts):
			# Loops through the user-defined number of posts
			insta_JSON = r.json()
			post = {
				'url_img': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['display_url'],
				# Fetches the URL of the image
				'url_post': 'https://www.instagram.com/p/' + insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['shortcode'],
				# Fetches the URL of the post itself
				'text': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['edge_media_to_caption']['edges'][0]['node']['text'],
				# Fetches the text content of the post
				'likes': insta_JSON['graphql']['user']['edge_owner_to_timeline_media']['edges'][x]['node']['edge_liked_by']['count']
				# Fetches the number of likes
			}
			insta_posts.append(post)	
	else:
		print(r.status_code)
		r.raise_for_status()
	return insta_posts

instagram_pull('dan_donofrio_official', 3)
# Follow me on instagram if you want
