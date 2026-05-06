import re

with open('c:/Users/panup/OneDrive/Desktop/เว็บ/index2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HR_NAV
old_hr_nav = """    const HR_NAV = [
      {
        section: 'ภารกิจของ HR', items: [
          { id: 'dashboard', icon: '🏠', label: 'หน้าหลัก' },
          { id: 'inbox', icon: '📥', label: 'รับเรื่องจากผู้บริหาร', badge: '3' },
        ]
      }
    ];"""

new_hr_nav = """    const HR_NAV = [
      {
        section: 'เมนูหลัก', items: [
          { id: 'dashboard', icon: '🏠', label: 'หน้าหลัก' },
          { id: 'inbox', icon: '✉️', label: 'กล่องรับงาน', badge: '12' },
          { id: 'my-history', icon: '🕒', label: 'ประวัติงานของฉัน' },
          { id: 'track-my-work', icon: '🔄', label: 'ติดตามงานของฉัน' },
          { id: 'approval-docs', icon: '📄', label: 'เอกสารขออนุมัติ' },
          { id: 'reports', icon: '📊', label: 'รายงาน' }
        ]
      },
      {
        section: 'เครื่องมือ', items: [
          { id: 'recommended-tools', icon: '🔗', label: 'เครื่องมือแนะนำ' }
        ]
      }
    ];"""

content = content.replace(old_hr_nav, new_hr_nav)

# 2. Replace setupSidebar
old_setup = """    function setupSidebar() {
      const nav = currentRole === 'hr' ? HR_NAV : MGR_NAV;
      const name = currentRole === 'hr' ? 'ธนพร สมใจ' : 'รศ.ดร.วีรชัย มั่นคง';
      const roleLabel = currentRole === 'hr' ? 'ผู้ดูแลระบบ' : 'ผู้บริหารหน่วยงาน';
      document.getElementById('userName').textContent = name;
      document.getElementById('userAvatar').textContent = name.charAt(0);
      document.getElementById('userRoleBadge').textContent = roleLabel;
      document.getElementById('userRoleBadge').className = 'role-badge ' + (currentRole === 'hr' ? 'hr' : 'mgr');"""

new_setup = """    function setupSidebar() {
      const nav = currentRole === 'hr' ? HR_NAV : MGR_NAV;
      const name = currentRole === 'hr' ? 'ฝ่ายทรัพยากรบุคคล' : 'รศ.ดร.วีรชัย มั่นคง';
      const roleLabel = currentRole === 'hr' ? '<span style="display:inline-block;width:8px;height:8px;background:#22c55e;border-radius:50%;margin-right:4px;"></span>ออนไลน์' : 'ผู้บริหารหน่วยงาน';
      document.getElementById('userName').textContent = name;
      document.getElementById('userAvatar').textContent = name.charAt(0);
      document.getElementById('userRoleBadge').innerHTML = roleLabel;
      document.getElementById('userRoleBadge').className = 'role-badge ' + (currentRole === 'hr' ? 'hr' : 'mgr');"""

content = content.replace(old_setup, new_setup)

# 3. Replace renderHRDashboard
# Find start and end of function
start_idx = content.find("function renderHRDashboard() {")
end_idx = content.find("function renderHRInbox() {")

if start_idx != -1 and end_idx != -1:
    # Need to keep the whitespace before function renderHRInbox
    end_idx = content.rfind("}", start_idx, end_idx) + 1
    
    new_dashboard = """function renderHRDashboard() {
      return `
  <!-- Header -->
  <div style="margin-bottom:28px;">
    <h1 style="font-size:32px; font-weight:800; color:var(--navy); margin-bottom:5px;">หน้าหลัก</h1>
    <p style="font-size:16px; color:var(--gray-600); font-weight:600;">ยินดีต้อนรับ ฝ่ายทรัพยากรบุคคล</p>
    <div style="display:inline-flex; align-items:center; gap:8px; margin-top:8px; font-size:12px; color:var(--gray-500);">
      <span style="display:inline-block; width:10px; height:10px; background:#22c55e; border-radius:50%;"></span> ศูนย์ปฏิบัติการ อัปเดตล่าสุด 6 พ.ค. 2569 11:26น.
    </div>
  </div>

  <!-- Zone A: KPI Cards -->
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-bottom:32px; align-items:stretch;">

    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; height:150px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
      <div style="display:flex; gap:16px;">
        <div style="width:60px; height:60px; background:#fee2e2; color:#ef4444; display:flex; flex-direction:column; justify-content:center; align-items:center; font-weight:bold; font-size:14px; border-radius:8px; line-height:1.2;">
          <div>ใส่</div>
        </div>
        <div style="display:flex; flex-direction:column; justify-content:flex-start;">
          <div style="color:#0284c7; font-weight:bold; font-size:16px; margin-bottom:8px;">คำร้องเสนออนุมัติใหม่</div>
          <div style="display:flex; align-items:baseline; gap:8px;">
            <span style="font-size:48px; font-weight:bold; color:#000; line-height:1;">6</span>
            <span style="font-size:14px; color:#64748b;">เรื่อง</span>
          </div>
        </div>
      </div>
      <div style="color:#0284c7; font-weight:bold; font-size:14px; margin-top:16px;">ดูรายละเอียด</div>
    </div>

    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; height:150px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
      <div style="display:flex; gap:16px;">
        <div style="width:60px; height:60px; background:#fef3c7; color:#d97706; display:flex; flex-direction:column; justify-content:center; align-items:center; font-weight:bold; font-size:14px; border-radius:8px; line-height:1.2;">
          <div>ใส่</div>
          <div>ไอคอน</div>
        </div>
        <div style="display:flex; flex-direction:column; justify-content:flex-start;">
          <div style="color:#d97706; font-weight:bold; font-size:16px; margin-bottom:8px;">รอเสนอเรื่องขออนุมัติ</div>
          <div style="display:flex; align-items:baseline; gap:8px;">
            <span style="font-size:48px; font-weight:bold; color:#000; line-height:1;">3</span>
            <span style="font-size:14px; color:#64748b;">เรื่อง</span>
          </div>
        </div>
      </div>
      <div style="color:#d97706; font-weight:bold; font-size:14px; margin-top:16px;">ดูรายละเอียด</div>
    </div>

    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; height:150px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
      <div style="display:flex; gap:16px;">
        <div style="width:60px; height:60px; background:#dcfce7; color:#16a34a; display:flex; flex-direction:column; justify-content:center; align-items:center; font-weight:bold; font-size:14px; border-radius:8px; line-height:1.2;">
          <div>ใส่</div>
          <div>ไอคอน</div>
        </div>
        <div style="display:flex; flex-direction:column; justify-content:flex-start;">
          <div style="color:#16a34a; font-weight:bold; font-size:16px; margin-bottom:8px;">อนุมัติเสร็จสิ้น</div>
          <div style="display:flex; align-items:baseline; gap:8px;">
            <span style="font-size:48px; font-weight:bold; color:#000; line-height:1;">35</span>
            <span style="font-size:14px; color:#64748b;">เรื่อง</span>
          </div>
        </div>
      </div>
      <div style="color:#16a34a; font-weight:bold; font-size:14px; margin-top:16px;">ดูรายละเอียด</div>
    </div>

  </div>

  <!-- Zone B: Tabs & Table -->
  <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; position:relative;">
    <!-- Red text annotations matching the image exactly -->
    <div style="position:absolute; right:-60px; top:130px; color:red; font-weight:bold; font-size:14px; line-height:3.5; display:flex; flex-direction:column;">
      <span>ล่าสุด</span>
      <span>วันนี้</span>
      <span>เมื่อวาน</span>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #e2e8f0; padding-bottom:10px; margin-bottom:20px;">
      <div style="display:flex; gap:30px;">
        <div style="display:flex; align-items:center; gap:8px; color:#0284c7; font-weight:bold; font-size:18px; border-bottom:3px solid #0284c7; padding-bottom:8px; margin-bottom:-13px;">
          <span style="font-size:20px; position:relative;">📁<span style="position:absolute; top:-2px; right:-2px; background:red; color:white; font-size:8px; width:12px; height:12px; display:flex; align-items:center; justify-content:center; border-radius:50%;">1</span></span> งานเข้า
        </div>
        <div style="display:flex; align-items:center; gap:8px; color:#94a3b8; font-weight:bold; font-size:18px; padding-bottom:8px; margin-bottom:-13px;">
          <span style="font-size:20px; position:relative;">📁<span style="position:absolute; top:-2px; right:-2px; background:red; color:white; font-size:8px; width:12px; height:12px; display:flex; align-items:center; justify-content:center; border-radius:50%;">1</span></span> ประวัติการทำงาน
        </div>
      </div>
      <div style="display:flex; gap:10px;">
        <button style="border:1px solid #cbd5e1; background:#fff; border-radius:6px; padding:6px 20px; font-weight:bold; color:red; font-size:14px; cursor:pointer;">ค้นหา</button>
        <button style="border:1px solid #cbd5e1; background:#fff; border-radius:6px; padding:6px 15px; font-weight:bold; color:red; font-size:14px; display:flex; align-items:center; gap:5px; cursor:pointer;">เรียง <span style="color:#000; font-size:10px;">▼</span></button>
      </div>
    </div>

    <table style="width:100%; border-collapse:collapse; text-align:left;">
      <thead>
        <tr style="background:#f1f5f9; color:#64748b; font-size:14px;">
          <th style="padding:15px; text-align:center; border-radius:8px 0 0 8px;">สถานะ</th>
          <th style="padding:15px; text-align:center;">หน่วยงาน</th>
          <th style="padding:15px;">เรื่อง/รายละเอียด</th>
          <th style="padding:15px; text-align:center;">วันที่/เวลา</th>
          <th style="padding:15px; text-align:center; border-radius:0 8px 8px 0;">การดำเนินการ</th>
        </tr>
      </thead>
      <tbody>
        <!-- Row 1 -->
        <tr style="border-bottom:1px solid #e2e8f0;">
          <td style="padding:20px; text-align:center;">
            <div style="display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#dbeafe; color:#0284c7; padding:8px 16px; border-radius:8px; font-weight:bold; min-width:100px;">
              <span style="width:12px; height:12px; background:#0284c7; border-radius:50%;"></span> ล่าสุด
            </div>
          </td>
          <td style="padding:20px; text-align:center; font-size:12px; color:#475569; font-weight:bold;">ศูนย์คอมพิวเตอร์</td>
          <td style="padding:20px;">
            <div style="font-weight:bold; font-size:14px; color:#1e293b;">ส่งร่าง "ปรับโครงสร้างภารกิจแปรรูปนม"</div>
            <div style="font-size:11px; color:#64748b; margin-top:4px;">เพิ่ม 3 ภารกิจสายสนับสนุน | ปรับอัตรากำลัง +2 อัตรา<br>| รอ HR ตรวจสอบความสอดคล้อง พ.ร.บ.</div>
          </td>
          <td style="padding:20px; font-size:12px; color:#475569; font-weight:bold; text-align:center;">12 พ.ค. 2569 10:30</td>
          <td style="padding:20px; text-align:center;">
            <span style="color:#0284c7; font-weight:bold; font-size:12px; cursor:pointer;">ตรวจสอบข้อมูล</span>
          </td>
        </tr>
        <!-- Row 2 -->
        <tr style="border-bottom:1px solid #e2e8f0;">
          <td style="padding:20px; text-align:center;">
            <div style="display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#fef3c7; color:#d97706; padding:8px 16px; border-radius:8px; font-weight:bold; min-width:100px;">
              <span style="width:12px; height:12px; background:#fcd34d; border-radius:50%;"></span> รอดำเนินการ
            </div>
          </td>
          <td style="padding:20px; text-align:center; font-size:12px; color:#475569; font-weight:bold;">ส่วนพัสดุ</td>
          <td style="padding:20px;">
            <div style="font-weight:bold; font-size:14px; color:#1e293b;">ขออนุมัติจัดซื้อ</div>
            <div style="font-size:11px; color:#64748b; margin-top:4px;">รายละเอียด</div>
          </td>
          <td style="padding:20px; font-size:12px; color:#475569; font-weight:bold; text-align:center;">12 พ.ค. 2569 10:30</td>
          <td style="padding:20px; text-align:center;">
            <span style="color:#d97706; font-weight:bold; font-size:12px; cursor:pointer;">เสนอเรื่องเข้าสภา</span>
          </td>
        </tr>
        <!-- Row 3 -->
        <tr>
          <td style="padding:20px; text-align:center;">
            <div style="display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#dcfce7; color:#16a34a; padding:8px 16px; border-radius:8px; font-weight:bold; min-width:100px;">
              <span style="width:12px; height:12px; background:#86efac; border-radius:50%;"></span> อนุมัติเสร็จสิ้น
            </div>
          </td>
          <td style="padding:20px; text-align:center; font-size:12px; color:#475569; font-weight:bold;">ศูนย์บรรณสาร</td>
          <td style="padding:20px;">
            <div style="font-weight:bold; font-size:14px; color:#1e293b;">อนุมัติเอกสารเรียบร้อย</div>
            <div style="font-size:11px; color:#64748b; margin-top:4px;">รายละเอียด</div>
          </td>
          <td style="padding:20px; font-size:12px; color:#475569; font-weight:bold; text-align:center;">12 พ.ค. 2569 10:30</td>
          <td style="padding:20px; text-align:center;">
            <span style="color:#16a34a; font-weight:bold; font-size:12px; cursor:pointer;">อนุมัติแล้ว</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
      `;
    }"""
    
    content = content[:start_idx] + new_dashboard + content[end_idx:]

with open('c:/Users/panup/OneDrive/Desktop/เว็บ/index2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
