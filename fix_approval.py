import re

with open('index2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace the entire approval section (lines 4947-5210)
old_approval = '''    // ══════════════════════════════════════════════
    // PROCESS 9: APPROVAL SUBMISSION
    // ══════════════════════════════════════════════
    let currentApprovalView = 'list';
    let currentApprovalTab = 'all';
    let selectedApprovalId = null;

    function switchApprovalTab(tab) {
      currentApprovalTab = tab;
      showPage('approval');
    }

    function switchApprovalView(view, id = null) {
      currentApprovalView = view;
      selectedApprovalId = id;
      showPage('approval');
    }

    function renderApproval() {
      if (currentApprovalView === 'detail') {
        return renderApprovalDetail();
      }

      const requests = [
        { id: 'ORG-003', name: 'กองคลัง', type: 'จัดตั้งหน่วยงาน', parent: 'สำนักงานอธิการบดี', status: 'pending_check', requester: 'นายนพคุณ ใจดี', date: '12 พ.ค. 2569 10:30', icon: '🏛️' },
        { id: 'MIS-002', name: 'งานบริหารและประสานงานองค์กร', type: 'จัดทำภารกิจใหม่', parent: 'กองแผนงาน', status: 'pending_action', requester: 'นางมรกต รุ่งโรจน์', date: '11 พ.ค. 2569 09:15', icon: '📋' },
        { id: 'ID-1', name: 'งานบุคคล', type: 'ปรับโครงสร้างหน่วยงาน', parent: 'สำนักอธิการบดี', status: 'approved', requester: 'นายสมชาย ใจดี', date: '10 พ.ค. 2569 14:00', icon: '👥' },
        { id: 'ID-4', name: 'งานธุรการ', type: 'ขอยุบหน่วยงาน', parent: 'กองคลัง', status: 'rejected', requester: 'นางมรกต รุ่งโรจน์', date: '09 พ.ค. 2569 16:30', icon: '📂' },
      ];'''

new_approval = '''    // ══════════════════════════════════════════════
    // PROCESS 9: APPROVAL SUBMISSION
    // ══════════════════════════════════════════════
    let currentApprovalView = 'list';
    let currentApprovalTab = 'all';
    let selectedApprovalId = null;

    const APPROVAL_REQUESTS = [
      { id: 'ORG-003', name: 'กองคลัง', type: 'จัดตั้งหน่วยงาน', parent: 'สำนักงานอธิการบดี', status: 'pending_check', requester: 'นายนพคุณ ใจดี', date: '12 พ.ค. 2569 10:30', icon: '🏛️' },
      { id: 'MIS-002', name: 'งานบริหารและประสานงานองค์กร', type: 'จัดทำภารกิจใหม่', parent: 'กองแผนงาน', status: 'pending_action', requester: 'นางมรกต รุ่งโรจน์', date: '11 พ.ค. 2569 09:15', icon: '📋' },
      { id: 'ID-1', name: 'งานบุคคล', type: 'ปรับโครงสร้างหน่วยงาน', parent: 'สำนักอธิการบดี', status: 'approved', requester: 'นายสมชาย ใจดี', date: '10 พ.ค. 2569 14:00', icon: '👥' },
      { id: 'ID-4', name: 'งานธุรการ', type: 'ขอยุบหน่วยงาน', parent: 'กองคลัง', status: 'rejected', requester: 'นางมรกต รุ่งโรจน์', date: '09 พ.ค. 2569 16:30', icon: '📂' },
    ];

    function switchApprovalTab(tab) {
      currentApprovalTab = tab;
      currentApprovalView = 'list';
      showPage('approval');
    }

    function switchApprovalView(view, id = null) {
      currentApprovalView = view;
      selectedApprovalId = id;
      showPage('approval');
    }

    function renderApproval() {
      if (currentApprovalView === 'detail') {
        return renderApprovalDetail();
      }

      const requests = APPROVAL_REQUESTS;'''

html = html.replace(old_approval, new_approval, 1)

# Now fix the tabs to be clickable and filtered
old_tabs_section = '''      <div class="app-tabs">
      <div class="app-tab active">ทั้งหมด <span class="count">8</span></div>
      <div class="app-tab">รอดำเนินการ <span class="count">2</span></div>
      <div class="app-tab">รอตรวจสอบ <span class="count">1</span></div>
      <div class="app-tab">อนุมัติแล้ว <span class="count">4</span></div>
      <div class="app-tab">ไม่อนุมัติ <span class="count">1</span></div>
    </div>

    <div class="req-list">
      ${requests.map(r => `
      <div class="req-card" onclick="switchApprovalView('detail', '${r.id}')">
        <div class="req-icon">${r.icon}</div>
        <div class="req-title">
          <h3>${r.id} ${r.name}</h3>
          <p>${r.type} • ${r.parent}</p>
        </div>
        <div class="req-info">
          <b>วันที่ยื่นคำขอ</b>
          ${r.date}
        </div>
        <div class="req-info">
          <b>ผู้ยื่นคำขอ</b>
          ${r.requester}
        </div>
        <div>
          ${r.status === 'pending_check' ? `<span class="status-badge s-pending-check">⌛ รอตรวจสอบ</span>` :
          r.status === 'pending_action' ? `<span class="status-badge s-pending-action">⚙️ รอดำเนินการ</span>` :
            r.status === 'approved' ? `<span class="status-badge s-approved">✓ อนุมัติแล้ว</span>` :
              `<span class="status-badge s-rejected">✕ ไม่อนุมัติ</span>`}
        </div>
        <div style="text-align:right;">
          <button class="btn-track ${r.status === 'rejected' ? 'btn-err' : ''}">
            ${r.status === 'approved' ? 'ดูรายละเอียด' : r.status === 'rejected' ? 'ดูเหตุผล' : 'ติดตามสถานะ'}
          </button>
        </div>
      </div>
      `).join('')}
    </div>
  </div>
      `;
    }'''

new_tabs_section = '''      <div class="app-tabs">
      <div class="app-tab ${currentApprovalTab==='all'?'active':''}" onclick="switchApprovalTab('all')">ทั้งหมด <span class="count">${requests.length}</span></div>
      <div class="app-tab ${currentApprovalTab==='pending_action'?'active':''}" onclick="switchApprovalTab('pending_action')">รอดำเนินการ <span class="count">${requests.filter(x=>x.status==='pending_action').length}</span></div>
      <div class="app-tab ${currentApprovalTab==='pending_check'?'active':''}" onclick="switchApprovalTab('pending_check')">รอตรวจสอบ <span class="count">${requests.filter(x=>x.status==='pending_check').length}</span></div>
      <div class="app-tab ${currentApprovalTab==='approved'?'active':''}" onclick="switchApprovalTab('approved')">อนุมัติแล้ว <span class="count">${requests.filter(x=>x.status==='approved').length}</span></div>
      <div class="app-tab ${currentApprovalTab==='rejected'?'active':''}" onclick="switchApprovalTab('rejected')">ไม่อนุมัติ <span class="count">${requests.filter(x=>x.status==='rejected').length}</span></div>
    </div>

    <div class="req-list">
      ${(currentApprovalTab==='all'?requests:requests.filter(x=>x.status===currentApprovalTab)).map(r => `
      <div class="req-card" onclick="switchApprovalView('detail','${r.id}')">
        <div class="req-icon">${r.icon}</div>
        <div class="req-title">
          <h3>${r.id} ${r.name}</h3>
          <p>${r.type} • ${r.parent}</p>
        </div>
        <div class="req-info">
          <b>วันที่ยื่นคำขอ</b>
          ${r.date}
        </div>
        <div class="req-info">
          <b>ผู้ยื่นคำขอ</b>
          ${r.requester}
        </div>
        <div>
          ${r.status==='pending_check'?'<span class="status-badge s-pending-check">⌛ รอตรวจสอบ</span>':r.status==='pending_action'?'<span class="status-badge s-pending-action">⚙️ รอดำเนินการ</span>':r.status==='approved'?'<span class="status-badge s-approved">✓ อนุมัติแล้ว</span>':'<span class="status-badge s-rejected">✕ ไม่อนุมัติ</span>'}
        </div>
        <div style="text-align:right;" onclick="event.stopPropagation()">
          <button class="btn-track ${r.status==='rejected'?'btn-err':''}" onclick="switchApprovalView('detail','${r.id}')">
            ${r.status==='approved'?'ดูรายละเอียด':r.status==='rejected'?'ดูเหตุผล':'ติดตามสถานะ'}
          </button>
        </div>
      </div>
      `).join('')}
    </div>
  </div>
      `;
    }'''

html = html.replace(old_tabs_section, new_tabs_section, 1)

# Replace renderApprovalDetail to support all statuses
old_detail_start = '''    function renderApprovalDetail() {
      const data = { id: 'ORG-003', name: 'กองคลัง', type: 'จัดตั้งหน่วยงาน', parent: 'สำนักงานอธิการบดี', status: 'pending_check' };'''

new_detail_start = '''    function renderApprovalDetail() {
      const found = APPROVAL_REQUESTS.find(x => x.id === selectedApprovalId);
      const data = found || { id: 'ORG-003', name: 'กองคลัง', type: 'จัดตั้งหน่วยงาน', parent: 'สำนักงานอธิการบดี', status: 'pending_check', icon: '🏛️', requester: 'นายนพคุณ ใจดี', date: '12 พ.ค. 2569 10:30' };
      const statusLabel = data.status==='pending_check'?'รอตรวจสอบ':data.status==='pending_action'?'รอดำเนินการ':data.status==='approved'?'อนุมัติแล้ว':'ไม่อนุมัติ';
      const statusColor = data.status==='pending_check'?'#f59e0b':data.status==='pending_action'?'#0ea5e9':data.status==='approved'?'#22c55e':'#ef4444';
      const step3class = data.status==='pending_check'?'active':['pending_action','approved','rejected'].includes(data.status)?'done':'';
      const step4class = data.status==='pending_action'?'active':['approved','rejected'].includes(data.status)?'done':'';
      const step5class = data.status==='approved'?'done':data.status==='rejected'?'done':'';
      const activeWidth = data.status==='pending_check'?'40%':data.status==='pending_action'?'60%':data.status==='approved'?'100%':'80%';'''

html = html.replace(old_detail_start, new_detail_start, 1)

# Replace the static header in detail view
old_det_header_inner = '''        <div style="width:60px; height:60px; background:rgba(255,255,255,0.05); border-radius:15px; display:flex; align-items:center; justify-content:center; font-size:32px;">🏛️</div>
        <div>
          <h2>${data.id} ${data.name}</h2>
          <p style="color:#94a3b8; margin:5px 0 0 0; font-weight:700;">${data.type} • สำนักงานอธิการบดี <span style="background:#f59e0b; color:#fff; font-size:10px; padding:2px 10px; border-radius:10px; margin-left:10px;">รอตรวจสอบ</span></p>
        </div>'''

new_det_header_inner = '''        <div style="width:60px; height:60px; background:rgba(255,255,255,0.05); border-radius:15px; display:flex; align-items:center; justify-content:center; font-size:32px;">${data.icon||'🏛️'}</div>
        <div>
          <h2>${data.id} ${data.name}</h2>
          <p style="color:#94a3b8; margin:5px 0 0 0; font-weight:700;">${data.type} • ${data.parent} <span style="background:${statusColor}; color:#fff; font-size:10px; padding:2px 10px; border-radius:10px; margin-left:10px;">${statusLabel}</span></p>
        </div>'''

html = html.replace(old_det_header_inner, new_det_header_inner, 1)

# Replace static process line width
old_procline = '      <div class="process-line-active"></div>'
new_procline = '      <div class="process-line-active" style="width:${activeWidth}"></div>'
html = html.replace(old_procline, new_procline, 1)

# Replace static proc-steps
old_steps = '''      <div class="proc-step done">
        <div class="proc-circle">1</div>
        <div class="proc-label">ส่งคำขอเข้าสู่ระบบ</div>
      </div>
      <div class="proc-step done">
        <div class="proc-circle">2</div>
        <div class="proc-label">ตรวจสอบองค์ประกอบ</div>
      </div>
      <div class="proc-step active">
        <div class="proc-circle">3</div>
        <div class="proc-label">รอพิจารณา</div>
      </div>
      <div class="proc-step">
        <div class="proc-circle">4</div>
        <div class="proc-label">มหาวิทยาลัยอนุมัติ</div>
      </div>
      <div class="proc-step">
        <div class="proc-circle">5</div>
        <div class="proc-label">อนุมัติเสร็จสิ้น</div>
      </div>'''

new_steps = '''      <div class="proc-step done">
        <div class="proc-circle">✓</div>
        <div class="proc-label">ส่งคำขอเข้าสู่ระบบ</div>
      </div>
      <div class="proc-step done">
        <div class="proc-circle">✓</div>
        <div class="proc-label">ตรวจสอบองค์ประกอบ</div>
      </div>
      <div class="proc-step ${step3class}">
        <div class="proc-circle">3</div>
        <div class="proc-label">รอพิจารณา</div>
      </div>
      <div class="proc-step ${step4class}">
        <div class="proc-circle">4</div>
        <div class="proc-label">มหาวิทยาลัยอนุมัติ</div>
      </div>
      <div class="proc-step ${step5class}">
        <div class="proc-circle">5</div>
        <div class="proc-label">อนุมัติเสร็จสิ้น</div>
      </div>'''

html = html.replace(old_steps, new_steps, 1)

# Replace static status banner
old_banner = '''    <div class="status-banner banner-wait">
      <div class="banner-icon" style="background:rgba(245, 158, 11, 0.2); color:#f59e0b;">⌛</div>
      <div>
        <div style="font-size:20px; font-weight:900; color:#fff;">สถานะปัจจุบัน: <span style="color:#f59e0b;">รอตรวจสอบ</span></div>
        <div style="font-size:14px; color:#94a3b8; margin-top:5px;">คำขอของคุณกำลังอยู่ระหว่างการตรวจสอบความครบถ้วนของข้อมูลโดยฝ่ายบุคคล</div>
      </div>
    </div>'''

new_banner = '''    ${data.status==='rejected'?`
    <div class="status-banner" style="background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);">
      <div class="banner-icon" style="background:rgba(239,68,68,0.2);color:#ef4444;font-size:34px;">✕</div>
      <div style="flex:1">
        <div style="font-size:20px;font-weight:900;color:#fff;">สถานะปัจจุบัน: <span style="color:#ef4444;">ไม่อนุมัติ</span></div>
        <div style="font-size:14px;color:#94a3b8;margin-top:5px;">คำขอนี้ไม่ผ่านการอนุมัติ กรุณาตรวจสอบเหตุผลและดำเนินการแก้ไข</div>
        <div style="margin-top:12px;padding:12px 16px;background:rgba(239,68,68,0.08);border-radius:10px;">
          <div style="font-weight:700;color:#ef4444;font-size:13px;margin-bottom:8px;">เหตุผลที่ไม่อนุมัติ</div>
          <ul style="color:#cbd5e1;font-size:13px;padding-left:18px;line-height:2;">
            <li>เอกสารประกอบไม่ครบถ้วนตามที่กำหนด</li>
            <li>เอกสารประกอบไม่ผ่านตามเกณฑ์ที่ระบุ</li>
            <li>เอกสารประกอบไม่ตรงตามข้อกำหนด</li>
          </ul>
          <button class="btn-track" style="margin-top:10px;background:#ef4444;border:none;" onclick="showToast('กรุณายื่นคำขอใหม่พร้อมเอกสารที่ถูกต้อง','warning')">ยื่นใหม่อีกครั้ง</button>
        </div>
      </div>
    </div>`
    :data.status==='approved'?`
    <div class="status-banner" style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);">
      <div class="banner-icon" style="background:rgba(34,197,94,0.2);color:#22c55e;font-size:34px;">✓</div>
      <div style="flex:1">
        <div style="font-size:20px;font-weight:900;color:#fff;">สถานะปัจจุบัน: <span style="color:#22c55e;">อนุมัติแล้ว</span></div>
        <div style="font-size:14px;color:#94a3b8;margin-top:5px;">คำขอได้รับการอนุมัติเรียบร้อยแล้ว</div>
        <div style="margin-top:12px;display:flex;gap:10px;">
          <button class="btn-track" style="background:#22c55e;border:none;" onclick="showToast('ดาวน์โหลดหนังสืออนุมัติเรียบร้อย ✅')">📄 ดาวน์โหลดหนังสืออนุมัติ</button>
          <button class="btn-track" onclick="showToast('พิมพ์เอกสาร...','info')">🖨️ พิมพ์เอกสาร</button>
        </div>
      </div>
    </div>`
    :data.status==='pending_action'?`
    <div class="status-banner" style="background:rgba(14,165,233,0.08);border:1px solid rgba(14,165,233,0.2);">
      <div class="banner-icon" style="background:rgba(14,165,233,0.2);color:#0ea5e9;">⚙️</div>
      <div>
        <div style="font-size:20px;font-weight:900;color:#fff;">สถานะปัจจุบัน: <span style="color:#0ea5e9;">รอดำเนินการ</span></div>
        <div style="font-size:14px;color:#94a3b8;margin-top:5px;">คำขออยู่ระหว่างการดำเนินการโดยเจ้าหน้าที่ที่เกี่ยวข้อง กรุณารอการยืนยัน</div>
      </div>
    </div>`
    :`
    <div class="status-banner banner-wait">
      <div class="banner-icon" style="background:rgba(245,158,11,0.2);color:#f59e0b;">⌛</div>
      <div>
        <div style="font-size:20px;font-weight:900;color:#fff;">สถานะปัจจุบัน: <span style="color:#f59e0b;">รอตรวจสอบ</span></div>
        <div style="font-size:14px;color:#94a3b8;margin-top:5px;">คำขอของคุณกำลังอยู่ระหว่างการตรวจสอบความครบถ้วนของข้อมูลโดยฝ่ายบุคคล</div>
      </div>
    </div>`}'''

html = html.replace(old_banner, new_banner, 1)

# Fix the detail table to use data fields
old_detail_table = '''          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">ประเภทการขอ</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">จัดตั้งหน่วยงาน</td>
          </tr>
          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">ชื่อหน่วยงาน</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">กองคลัง</td>
          </tr>
          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">หน่วยงานต้นสังกัด</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">สำนักงานอธิการบดี</td>
          </tr>'''

new_detail_table = '''          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">ประเภทการขอ</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">${data.type}</td>
          </tr>
          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">ชื่อหน่วยงาน</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">${data.name}</td>
          </tr>
          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">หน่วยงานต้นสังกัด</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">${data.parent}</td>
          </tr>
          <tr style="border-bottom:1px solid #334155;">
            <td style="padding:15px 0; color:#64748b; font-weight:700;">ผู้ยื่นคำขอ</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">${data.requester}</td>
          </tr>
          <tr>
            <td style="padding:15px 0; color:#64748b; font-weight:700;">วันที่ยื่นคำขอ</td>
            <td style="padding:15px 0; color:#fff; font-weight:800;">${data.date}</td>
          </tr>'''

html = html.replace(old_detail_table, new_detail_table, 1)

with open('index2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! All approval page buttons are now functional.")
