from bs4 import BeautifulSoup, NavigableString
import os
import re

def remove_specific_footer_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')

    footer = soup.find('footer') or soup.find('div', class_='footer')
    if footer:
        links_to_remove = footer.find_all('a', href=["https://www.sphinx-doc.org/", "https://github.com/readthedocs/sphinx_rtd_theme", "https://readthedocs.org"])
        for link in links_to_remove:
            link.decompose()
        
        for content in footer.contents:
            if isinstance(content, NavigableString) and 'Built with Sphinx' in content:
                content.extract()

    str_soup=str(soup)
    refined_str = re.sub(r'\s*Built with\s+using a\n\s*\n \s*provided by\s*\.\s*', '', str_soup)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(refined_str)

# Removes Built with statement from all .html footers.
def remove_footer_from_all_html(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.html'):
                remove_specific_footer_text(os.path.join(root, file_name))

# Removes Developer Guide linke from generated .html files
def remove_dev_manual_link(index_html_path):
    if os.path.exists(index_html_path):
        with open(index_html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        for li in soup.find_all('li', class_='toctree-l1'):
            a = li.find('a', href='dev/developer-guide.html')
            if not a:
                a = li.find('a', href='../dev/developer-guide.html')
            if a and 'Developer Guide' in a.text:
                li.decompose()

        with open(index_html_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

def main():
    html_output_dir = './_build/html'
    remove_footer_from_all_html(html_output_dir)
    
    html_files=[html_output_dir+'/'+x for x in os.listdir(html_output_dir) if x[-5:] == '.html']
    html_files+=[html_output_dir+'/user/'+x for x in os.listdir(html_output_dir+'/user') if x[-5:] == '.html']
    
    for fname in html_files:
        print(fname)
        #remove_dev_manual_link(fname)

if __name__ == '__main__':
    main()

