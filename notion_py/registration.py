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
            return add_table(client, child)

    project_page = page.children.add_new(PageBlock, title=name)
    return add_table(client, project_page)

def add_table(client, page):
    title = str(datetime.now().strftime("%Y-%m-%d"))
    i = 1
    for child in page.children:
        if title == child.title:
            title = str(datetime.now().strftime("%Y-%m-%d"))
            title = title+"("+str(i)+")"
            i+=1
    try:
        print(page)
        schema = {
            "title": {"name": "이름", "type": "title"},
            "text": {"name": "비고", "type": "text"},
            "date": {"name": "date", "type": "date"}
            }
        child = page.children.add_new(CollectionViewBlock)
        child.collection = client.get_collection(client.create_record("collection", parent=child, schema=schema))
        child.title = title
        child.views.add_new(view_type="table")
        return 0
    except:
        print("add table error")
        return -1