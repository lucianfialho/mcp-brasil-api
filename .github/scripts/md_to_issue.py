import os
import glob
from github import Github
import re

REPO = os.environ.get('GITHUB_REPOSITORY')
TOKEN = os.environ.get('GITHUB_TOKEN')
ISSUES_PATH = 'docs/issues/*.md'

if not TOKEN or not REPO:
    print('GITHUB_TOKEN ou GITHUB_REPOSITORY não definidos.')
    exit(1)

g = Github(TOKEN)
repo = g.get_repo(REPO)

for md_file in glob.glob(ISSUES_PATH):
    with open(md_file, encoding='utf-8') as f:
        content = f.read()
    # O título será a primeira linha não vazia, sem markdown
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    if not lines:
        continue
    title = lines[0].replace('#', '').strip()
    # Extrair labels se houver linha '**Labels:** ...'
    labels = []
    for l in lines:
        m = re.match(r'\*\*Labels:\*\*\s*(.+)', l)
        if m:
            labels = [x.strip() for x in m.group(1).split(',') if x.strip()]
            break
    # Fechar issues abertas com o mesmo título
    for issue in repo.get_issues(state='open'):
        if issue.title == title:
            issue.edit(state='closed')
            print(f'Issue fechada: {title}')
    # Criar nova issue
    repo.create_issue(title=title, body=content, labels=labels)
    print(f'Issue criada: {title} (labels: {labels})')
