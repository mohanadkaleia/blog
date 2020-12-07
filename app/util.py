import re



# This function is forked from here: https://github.com/MinchinWeb/minchin.pelican.plugins.summary
def get_summary(content):
	# Summary will take the first paragraph of the content
	begin_marker, end_marker = '<p>', '</p>'
	remove_markers = False
	begin_summary = content.find(begin_marker)
	end_summary = content.find(end_marker)

	summary = content[begin_summary:end_summary]
	summary = re.sub(r"<div.*>", "", summary)
	summary = re.sub(r"</div>", "", summary)

	return summary

