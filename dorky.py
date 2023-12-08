import webbrowser, sys

if len(sys.argv) >1:
    adress = ' '.join(sys.argv[1:])

else:
    print('Not provided any domain')

dork = [f'site:{adress} ext:php inurl:?',
        f'site:{adress} inurl:reports intext:"{adress}"',
        f'site:"{adress}" ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess',
        f'inurl:config | inurl:env | inurl:setting | inurl:backup | inurl:admin | inurl:php site:{adress}',
        f'inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:& site:{adress}',
        f'inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:"{adress}"',
        f'site:s3.amazonaws.com "{adress}"',
        f'site:blob.core.windows.net "{adress}"',
        f'site:googleapis.com "{adress}"',
        f'site:drive.google.com "{adress}"',
        f'site:dev.azure.com "{adress}"',
        f'site:onedrive.live.com "{adress}"',
        f'site:digitaloceanspaces.com "{adress}"']


browser = webbrowser.get('firefox')

first = True
for i in dork:
    if first:
        browser.open_new('https://www.google.com/search?client=firefox-b-d&q=' + i)
        first = False
    else:
        browser.open_new_tab('https://www.google.com/search?client=firefox-b-d&q=' + i)
