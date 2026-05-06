import os
import re

file_path = r"c:\Users\panup\OneDrive\Desktop\เว็บ\index2.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    (r'<div style="font-size:17px; font-weight:800; margin-bottom:5px; color:#fff;">', r'<div style="font-size:17px; font-weight:800; margin-bottom:5px; color:var(--navy);">'),
    (r'<div style="font-size:11px; color:rgba\(255,255,255,0\.5\);', r'<div style="font-size:11px; color:var(--gray-500);'),
    (r'color:rgba\(255,255,255,0\.2\);', r'color:var(--gray-400);'),
    (r'<span style="color:#fff;">1', r'<span style="color:var(--navy);">1'),
    (r'<span style="color:#fff; font-weight:800;">', r'<span style="color:var(--navy); font-weight:800;">'),
    (r'<h2 style="font-size:20px; font-weight:900; margin:0; color:#fff;">', r'<h2 style="font-size:20px; font-weight:900; margin:0; color:var(--navy);">'),
    (r'color:#f1f5f9;', r'color:#1e293b;'),
    (r'color:#fff;">ประสิทธิภาพเพิ่มขึ้น', r'color:#1e293b;">ประสิทธิภาพเพิ่มขึ้น'),
    (r'color:#fff;">การลดภารกิจซ้ำซ้อน', r'color:#1e293b;">การลดภารกิจซ้ำซ้อน'),
    (r'color:#fff;">ประหยัดงบประมาณ', r'color:#1e293b;">ประหยัดงบประมาณ'),
    (r'color:#fff;">ความสอดคล้องยุทธศาสตร์', r'color:#1e293b;">ความสอดคล้องยุทธศาสตร์'),
    (r'color:#fff; margin-bottom:15px;', r'color:var(--navy); margin-bottom:15px;'),
    (r'color:#e2e8f0;">🏢 โครงสร้างปัจจุบัน', r'color:var(--navy);">🏢 โครงสร้างปัจจุบัน'),
    (r'color:#e2e8f0;">📈 ข้อมูลสถิติปัจจุบัน', r'color:var(--navy);">📈 ข้อมูลสถิติปัจจุบัน'),
    (r'color:#fff;">ยืนยันการเลือก:', r'color:var(--navy);">ยืนยันการเลือก:'),
    (r'<td style="color:#fff; font-weight:800;">', r'<td style="color:var(--navy); font-weight:800;">'),
    (r'color:#fff; font-size:15px;">แก้ไขข้อผิดพลาดให้ครบก่อนส่งเรื่อง', r'color:#ef4444; font-size:15px;">แก้ไขข้อผิดพลาดให้ครบก่อนส่งเรื่อง'),
    (r'<div style="font-size:20px;font-weight:900;color:#fff;">สถานะปัจจุบัน:', r'<div style="font-size:20px;font-weight:900;color:var(--navy);">สถานะปัจจุบัน:'),
    (r'<td style="padding:15px 0; color:#fff; font-weight:800;">', r'<td style="padding:15px 0; color:var(--navy); font-weight:800;">')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing colors")