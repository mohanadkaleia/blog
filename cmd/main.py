import re
import os
import shutil
import sys


SRC_DIR = '/Users/mohanad/Downloads/mycodee/'
DEST_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../app/static/images/'
CONTENT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../content/posts/'
RELATIVE_DEST = '../../static/images/'

def migrate_article_images(name):
    img_regex = '(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)'
    content = ""

    print(":::::::::::::::::::::::::::::::")
    print(f"Migrage images for article {name}")
    
    with open(CONTENT_DIR + name ,'r') as file:
        content = file.read()
        try:
            # Extract images
            images = set([x.group() for x in re.finditer(img_regex, content)])   
            destination = DEST_DIR + '/' + name.split('.')[0]
            if not os.path.exists(destination):
                os.makedirs(destination)

            # Copy images src -> dest
            for img in images:
                if img.startswith('http://mycodee.com'):                    
                    print(img.replace('http://mycodee.com/', SRC_DIR))
                    shutil.copy2(img.replace('http://mycodee.com/', SRC_DIR), destination)

                    # Update the article with the new img directory
                    print("new image name")
                    print(RELATIVE_DEST + name.split('.')[0] + '/' + os.path.basename(img))

                    content = re.sub(img, RELATIVE_DEST + name.split('.')[0] + '/' + os.path.basename(img), content)	   
            
        except Exception as e:
            print("oops")
            print(e)
            pass
        
    with open(CONTENT_DIR + name, 'w') as file:
        try:
            # Write back the new cleansed content
            file.write(content)
        except Exception as e:
            print("failed to write :(")
            print(e)
    


def main():
    count = 0
    for filename in os.listdir(CONTENT_DIR):        
        migrate_article_images(filename)
        count += 1
        if count >= 10:
            return


if __name__ == '__main__':
    main()
