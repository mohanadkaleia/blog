import re

def get_summary(content):

	# Remove all img tags
	regex = '<img[^>]+src="([^">]+)"[^>]+>'
	summary = re.sub(regex, "", content)

	# Remove empty paragraphs
	regex = '<p></p>'
	summary = re.sub(regex, "", summary)
	summary = re.sub(r"<div.*>", "", summary)
	summary = re.sub(r"</div>", "", summary)

	# Return the first 300 characters
	return summary[:300]	
