import os, sys, requests
from dotenv import load_dotenv
load_dotenv('C:/Users/emily/StagingComplete/staging-tool/.env')

auth = (os.environ['WP_APP_USERNAME'], os.environ['WP_APP_PASSWORD'])
headers = {'User-Agent': 'ParentData-StagingTool/1.0'}

for slug in [
    'whats-the-data-behind-waiting-a-year-to-check-fertility',
    'should-i-get-genetic-carrier-screening-prior-ttc',
]:
    resp = requests.get(
        'https://parentdata.org/wp-json/wp/v2/posts',
        params={'slug': slug, 'status': 'publish'},
        headers=headers,
        auth=auth,
        timeout=30,
    )
    posts = resp.json()
    if not posts:
        print(f'{slug}: NO POST FOUND')
        continue
    post = posts[0]
    content = post.get('content', {}).get('rendered', '')
    print(f'--- {slug} ---')
    print(f'Content length: {len(content)} chars')
    print(f'First 300 chars: {content[:300]}')
    print(f'Last 300 chars: {content[-300:]}')
    print()
