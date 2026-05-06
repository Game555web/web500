import re

files = ['/Users/jidarat/Downloads/เว็บ/index.html', '/Users/jidarat/Downloads/เว็บ/index2.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert incorrect code replacements
    reverts = [
        (".การเชื่อมโยงข้อมูล-row", ".mapping-row"),
        (".การเชื่อมโยงข้อมูล-box", ".mapping-box"),
        (".การเชื่อมโยงข้อมูล-arrow", ".mapping-arrow"),
        (".การเชื่อมโยงข้อมูล-tag", ".mapping-tag"),
        ("DATA.การเชื่อมโยงข้อมูลs", "DATA.mappings"),
        ("การเชื่อมโยงข้อมูลs: [", "mappings: ["),
        ("{ id: 'การเชื่อมโยงข้อมูล', icon: '🔗', label: 'ผูกตำแหน่ง-ภารกิจ' }", "{ id: 'mapping', icon: '🔗', label: 'ผูกตำแหน่ง-ภารกิจ' }"),
        ("'การเชื่อมโยงข้อมูล': renderMapping", "'mapping': renderMapping"),
        ("การเชื่อมโยงข้อมูล: 'ผูกตำแหน่ง-ภารกิจ', notifications: 'การแจ้งเตือน',", "mapping: 'ผูกตำแหน่ง-ภารกิจ', notifications: 'การแจ้งเตือน',"),
        ("onclick=\"showPage('การเชื่อมโยงข้อมูล')\"", "onclick=\"showPage('mapping')\""),
        ("['7.0', 'Mapping', DATA.mappings]", "['7.0', 'Mapping', DATA.mappings]"), # just in case
        ("<div class=\"การเชื่อมโยงข้อมูล-row\"", "<div class=\"mapping-row\""),
        ("<div class=\"การเชื่อมโยงข้อมูล-box\"", "<div class=\"mapping-box\""),
        ("<div class=\"การเชื่อมโยงข้อมูล-arrow\"", "<div class=\"mapping-arrow\""),
        ("<div class=\"การเชื่อมโยงข้อมูล-tag\"", "<div class=\"mapping-tag\""),
    ]

    for old, new in reverts:
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done fixing code identifiers")
