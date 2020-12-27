import re
import os
import shutil
import sys


SRC_DIR = '/Users/mohanad/Downloads/mycodee/'
DEST_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../app/static/images/'
CONTENT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../content/posts/'
RELATIVE_DEST = '../../static/images/'


class ErrWritingFile(Exception):
    pass

class ErrMigratingImages(Exception):
    pass

def migrate_article_images(name):  
    print(":::::::::::::::::::::::::::::::")
    print(f"Migrage images for article {name}")
    
    with open(CONTENT_DIR + name ,'r+') as file:
        content = file.read()
        file.seek(0)
        
        try:
            # Extract images
            img_regex = '(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)'   
            images = set([x.group() for x in re.finditer(img_regex, content)])   
            destination = DEST_DIR + '/' + name.split('.')[0]
            if not os.path.exists(destination):
                os.makedirs(destination)

            # Copy images src -> dest and update the content
            for img in images:
                if img.startswith('http://mycodee.com'):                                                            
                    shutil.copy2(img.replace('http://mycodee.com/', SRC_DIR), destination)                                
                    content = re.sub(img, RELATIVE_DEST + name.split('.')[0] + '/' + os.path.basename(img), content)	   
            
            file.write(content)
            file.truncate()
        except Exception as e:            
            print(e)            
        
def main():  
    # filename = 'create-windows-service-from-an-application.md'
    # migrate_article_images(filename)        

    for filename in os.listdir(CONTENT_DIR):        
        migrate_article_images(filename)        

if __name__ == '__main__':
    main()
