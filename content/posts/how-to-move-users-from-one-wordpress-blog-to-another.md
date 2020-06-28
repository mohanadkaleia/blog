Title: How to Move Users From One WordPress Blog to Another
Date: 2012-11-04 17:20
Author: admin
Category: Website
Slug: how-to-move-users-from-one-wordpress-blog-to-another
Status: published

Today, while moving a WordPress built site from one domain to another I ran into a snag. Import/Export for blog posts and pages worked great for moving the content from one site to the other but what do I do with the 79 users on the website? WordPress, sadly, doesn’t have an Import/Export function for users. For a minute, I panicked and thought “Am I going to have to manually enter all of these users into the site for a second time?” The answer is no.

Here’s the math:

### Step 1: Export Original

[Users to CSV](http://yoast.com/wordpress/users-to-csv/ "Users to CSV") is a useful plugin by Joost that lets you export your user list as a CSV file. Install the plugin to your site and run the program via the Users tab in the navigation of your back end. From here you’ll get a nice, neat CSV file with a table of your users – complete with IDs, email addresses, URLs, display names, first names, last names, nicknames, and registration dates.

### Step 2: Install Importer

Now that you’ve got your CSV file exported you’re obviously going to need to get it installed on the new site. A great tool for this is Rode Works’ tweek of Dagon Design’s [Import User](http://rodeworks.com/technology/wordpress-batch-import-users/ "Import User") plugin. The original automatically sent out notification emails to the new users saying that their new account was set up. Since their accounts are already supposed to be set up, you don’t wan to be sending out new notifications, this is where Rode Works’ tweek of the original code comes into play.

### Step 3: Adjust CSV and Import

You’ll need to adjust your CSV file using Excel (or similar software) and move some cells around to meet the requirements of the Import User plugin but for the most part it’s pretty straight forward. You can either import the CSV file via the plugin or copy and paste the content into the back end.

There’s a bit of playing around involved but it in the end it should only really take about 10 minutes to do all of this – which is far better than the hours it would take to do it by hand, or worse, force the users to do it themselves.
