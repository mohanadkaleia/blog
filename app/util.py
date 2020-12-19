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
