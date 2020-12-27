import re

def get_summary(content):

	# Remove all img tags
	regex = '<img[^>]+src="([^">]+)"[^>]+>'
	summary = re.sub(regex, "", content)

	# Remove empty paragraphs
	regex = '<p></p>'
	summary = re.sub(regex, "", summary)
	
	# Remove the quote of the begining of the article
	regex = '<blockquote>(.|\n)*?<\/blockquote>'
	summary = re.sub(regex, "", summary)	
		
	# Return the first 300 characters
	return summary[:300]	


def get_cover(conetnt):		
	# Find an return the first image
	regex = 'src="([^">]+)"[^>]+>'
	try:
		return re.search(regex, conetnt).group(1)
	except Exception as e:
		# lol
		return '../../static/images/logo.png'	
