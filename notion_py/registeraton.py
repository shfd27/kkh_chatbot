from .configs import configs
from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import CollectionViewBlock
from datetime import datetime 

def make_page(name):
    client = NotionClient(configs.token_v2)
    page = client.get_block(configs.page_url)
    for child in page.children:
        if name == child.title:
            project_page = child
            return add_table(project_page)
    project_page = page.children.add_new(PageBlock, title=name)
    return add_table(project_page)

def add_table(page):
    client = NotionClient(configs.token_v2)
    print(page)
    schema = {
        "title": {"name": "이름", "type": "title"},
        "text": {"name": "비고", "type": "text"},
        "date": {"name": "date", "type": "date"}
        }
    child = page.children.add_new(CollectionViewBlock)
    child.collection = client.get_collection(client.create_record("collection", parent=child, schema=schema))
    child.title = str(datetime.now().strftime("%Y-%m-%d"))
    child.views.add_new(view_type="table")