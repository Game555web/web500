import re

files = ['/Users/jidarat/Downloads/เว็บ/index.html', '/Users/jidarat/Downloads/เว็บ/index2.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We only want to replace words outside of HTML tags and JS code.
    # A safer approach for this specific file:
    # Let's list the known exact phrases to replace:
    
    replacements = [
        # Mapping
        ("การ Mapping", "การเชื่อมโยงข้อมูล"),
        ("Mapping ตำแหน่งและภารกิจ", "การเชื่อมโยงข้อมูล ตำแหน่งและภารกิจ"),
        ("Mapping ตำแหน่งงานกับภารกิจ", "การเชื่อมโยงข้อมูลตำแหน่งงานกับภารกิจ"),
        ("Mapping ทั้งหมด", "การเชื่อมโยงข้อมูลทั้งหมด"),
        ("Mapping ล่าสุด", "การเชื่อมโยงข้อมูลล่าสุด"),
        ("แผนผัง Mapping", "แผนผังการเชื่อมโยงข้อมูล"),
        ("ตาราง Mapping", "ตารางการเชื่อมโยงข้อมูล"),
        ("ค้นหา Mapping...", "ค้นหาการเชื่อมโยงข้อมูล..."),
        ("mapping", "การเชื่อมโยงข้อมูล"), # this might be tricky, let's target specific cases
        ("} mapping<", "} การเชื่อมโยงข้อมูล<"),
        
        # Validate
        ("✅ Validate พ.ร.บ. ทั้งหมด", "✅ การตรวจสอบความถูกต้อง พ.ร.บ. ทั้งหมด"),
        ("✅ Validate พ.ร.บ.", "✅ การตรวจสอบความถูกต้อง พ.ร.บ."),
        ("✅ Validate Mapping", "✅ การตรวจสอบความถูกต้อง การเชื่อมโยงข้อมูล"),
        ("✅ Validate", "✅ การตรวจสอบความถูกต้อง"),
        ("ผ่าน Validate", "ผ่านการตรวจสอบความถูกต้อง"),
        ("พร้อม validate พ.ร.บ.", "พร้อมการตรวจสอบความถูกต้อง พ.ร.บ.")
    ]

    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
