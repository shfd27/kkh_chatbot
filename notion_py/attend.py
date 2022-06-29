from .configs import configs
import notion
from notion.client import NotionClient
from datetime import datetime

def attend(project, stu_name):
    client = NotionClient(configs.token_v2)
    page = client.get_block(configs.page_url)
    try:
        for child in page.children:
            if project == child.title:
                project_page = child
                break

        child = project_page.children[-1]

        row = child.collection.add_row()
        row.이름 = stu_name    # row.set_property("이름", stu_name)
        row.set_property("비고", "출석")
        row.비고 = "출석"
        row.date = notion.collection.NotionDate(datetime.now())
        return 0
    except:
        print("attend error")
        return -1