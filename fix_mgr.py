import re

with open('index2.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_content = """    function renderMGRDashboard() {
      return `
  <style>
    /* Base & Typography */
    .mgr-container { font-family: 'Sarabun', sans-serif; background: transparent; color: var(--navy); }
    
    /* 0. Top Navigation */
    .top-nav { display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e2e8f0; }
    .top-nav-left { display: flex; align-items: center; gap: 15px; }
    .top-nav-center { display: flex; gap: 10px; }
    .top-nav-right { display: flex; align-items: center; gap: 15px; }
    .select-box { padding: 8px 12px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 13px; background: #f8fafc; outline: none; cursor:pointer; }
    .select-box:hover { border-color: var(--navy); }
    
    /* Section Header */
    .section-title { font-size: 16px; font-weight: 800; display: flex; align-items: center; gap: 8px; margin-bottom: 15px; margin-top: 25px; border-left: 4px solid var(--gold); padding-left: 10px; }

    /* 2. Smart Recommendation + Compare */
    .grid-2-smart { display: grid; grid-template-columns: 1.2fr 2fr; gap: 20px; margin-bottom: 25px; }
    .panel { background: #fff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 20px; }
    
    .ai-list { list-style: none; padding: 0; margin: 0; }
    .ai-item { padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: flex-start; }
    .ai-badge { font-size: 10px; padding: 3px 8px; border-radius: 4px; font-weight: bold; }
    .ai-badge.high { background: #fee2e2; color: #991b1b; }
    .ai-badge.med { background: #fef3c7; color: #92400e; }
    
    .compare-split { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
    .tree-box { background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 8px; padding: 15px; min-height: 200px; font-size: 13px; }
    .tree-node-item { padding: 8px 12px; background: #fff; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 8px; position: relative; font-weight: bold; font-size: 12px; }
    .tree-node-item.added { border-color: #22c55e; background: #f0fdf4; color: #166534; }
    .tree-node-item.removed { border-color: #ef4444; background: #fef2f2; text-decoration: line-through; opacity: 0.7; color: #991b1b; }
    .tree-node-item.modified { border-color: #eab308; background: #fefce8; color: #854d0e; }
    
    /* 3. Structure Workspace */
    .workspace-grid { display: grid; grid-template-columns: 240px 1fr 240px; gap: 15px; min-height: 400px; margin-bottom: 25px; }
    .workspace-panel { background: #fff; border-radius: 12px; border: 1px solid #e2e8f0; display: flex; flex-direction: column; overflow: hidden; }
    .workspace-header { background: #f8fafc; padding: 12px 15px; font-weight: 700; border-bottom: 1px solid #e2e8f0; font-size: 13px; }
    .workspace-body { padding: 15px; flex: 1; overflow-y: auto; font-size: 12px; }
    .func-item { padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 8px; cursor: grab; background: #fff; transition: 0.2s; font-weight: 600; display:flex; align-items:center; gap:8px; }
    .func-item:hover { border-color: var(--navy); transform: translateX(2px); }
    
    .canvas-area { background: #f1f5f9; position: relative; display: flex; align-items: center; justify-content: center; background-image: radial-gradient(#cbd5e1 1px, transparent 1px); background-size: 20px 20px; }
    .node-card { background: #fff; border: 2px solid var(--navy); padding: 10px 15px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); width: 180px; text-align: center; position: relative; z-index: 2; }
    
    /* 4. Validation & Submission */
    .validation-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px; }
    .check-item { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; font-size: 13px; background: #f8fafc; padding: 10px; border-radius: 8px; border: 1px solid #e2e8f0; }
  </style>

  <div class="mgr-container fade-in">
    <!-- 0. Top Navigation -->
    <div class="top-nav">
      <div class="top-nav-left">
        <div style="width:40px;height:40px;background:var(--navy);border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;">🏛️</div>
        <div>
          <h2 style="margin:0;font-size:16px;font-weight:800;color:var(--navy);">Support Function Structure Management</h2>
          <div style="font-size:11px;color:var(--gray-500);font-weight:600;">Control Center สำหรับโครงสร้างภารกิจ (ผู้บริหารหน่วยงาน)</div>
        </div>
      </div>
      <div class="top-nav-center">
        <select class="select-box"><option>มหาวิทยาลัยเทคโนโลยีสุรนารี</option><option>สำนักงานอธิการบดี</option></select>
        <select class="select-box"><option>ร่างโครงสร้าง v2.1 (กำลังแก้ไข)</option><option>โครงสร้าง v1.0 (ใช้งานจริง)</option></select>
      </div>
      <div class="top-nav-right">
        <div style="position:relative;cursor:pointer;font-size:20px;margin-right:10px;">🔔<span style="position:absolute;top:-5px;right:-5px;background:#ef4444;color:#fff;font-size:9px;padding:2px 6px;border-radius:10px;font-weight:bold;">3</span></div>
        <div style="display:flex;align-items:center;gap:10px;">
          <div style="text-align:right;">
            <div style="font-size:12px;font-weight:800;color:var(--navy);">รศ.ดร.วีรชัย มั่นคง</div>
            <div style="font-size:10px;color:var(--gray-500);font-weight:600;">รองอธิการบดีฝ่ายยุทธศาสตร์</div>
          </div>
          <div style="width:38px;height:38px;background:var(--gold);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:bold;font-size:16px;">ว</div>
        </div>
      </div>
    </div>

    <!-- 1. Approval Status Overview (Hero Section) -->
    <h2 class="section-title" style="margin-top:0;">📊 1. Approval Status Overview</h2>
    <div class="panel" style="margin-bottom:25px; padding:25px; border: 2px solid #e2e8f0; position:relative; overflow:hidden;">
      <!-- Background subtle gradient -->
      <div style="position:absolute; top:0; right:0; width:300px; height:100%; background:linear-gradient(90deg, transparent, #fef3c7); z-index:0; opacity:0.5;"></div>
      
      <div style="position:relative; z-index:1; display:flex; justify-content:space-between; align-items:flex-start;">
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <h2 style="margin:0; font-size:22px; font-weight:900; color:var(--navy);">โครงสร้างฝ่ายบริหารทั่วไป</h2>
            <span style="font-size:12px; font-weight:bold; color:var(--gray-500); background:#f1f5f9; padding:4px 8px; border-radius:6px;">Version: v2.1 (กำลังปรับปรุง)</span>
          </div>
          
          <div style="display:flex; align-items:center; gap:15px; margin-bottom:20px;">
            <div style="background:#fffbeb; color:#d97706; padding:6px 12px; border-radius:8px; font-weight:800; font-size:13px; border:1px solid #fde68a; display:flex; align-items:center; gap:6px;">
              <span style="font-size:16px;">🟠</span> อยู่ระหว่าง HR Review
            </div>
            <div style="font-size:12px; color:var(--gray-500); font-weight:600;">
              อัปเดตล่าสุด: 5 พ.ค. 2026 | โดย: รศ.ดร.วีรชัย มั่นคง
            </div>
          </div>
          
          <!-- Progress Bar -->
          <div style="margin-bottom:25px; max-width:600px;">
            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold; margin-bottom:5px;">
              <span style="color:var(--navy);">ความคืบหน้า (Progress)</span>
              <span style="color:var(--gold);">80% (อยู่ขั้น HR Review)</span>
            </div>
            <div style="height:8px; background:#e2e8f0; border-radius:4px;"><div style="width:80%; height:100%; background:var(--gold); border-radius:4px;"></div></div>
          </div>
          
          <!-- Timeline (Step) -->
          <div style="display:flex; align-items:center; gap:10px; font-size:12px; font-weight:800; color:var(--gray-500); max-width:600px;">
            <div style="display:flex; align-items:center; gap:5px; color:#16a34a;"><span>✔</span> Draft</div>
            <div style="flex:1; height:2px; background:#16a34a;"></div>
            <div style="display:flex; align-items:center; gap:5px; color:#16a34a;"><span>✔</span> HR Review</div>
            <div style="flex:1; height:2px; background:var(--gold);"></div>
            <div style="display:flex; align-items:center; gap:5px; color:var(--gold);"><span>●</span> Council Approval</div>
            <div style="flex:1; height:2px; background:#e2e8f0;"></div>
            <div style="display:flex; align-items:center; gap:5px;"><span>○</span> Completed</div>
          </div>
        </div>
        
        <!-- Action Buttons -->
        <div style="display:flex; flex-direction:column; gap:10px; min-width:180px; text-align:right;">
          <button class="btn btn-primary" style="padding:12px; font-weight:800; box-shadow:0 4px 10px rgba(30, 58, 138, 0.2);">👁 ดูรายละเอียด</button>
          <button class="btn btn-outline" style="padding:12px; font-weight:800;">💬 ดู Feedback จาก HR</button>
          
          <div style="background:#fefce8; border:1px solid #fef08a; padding:10px; border-radius:8px; margin-top:5px; text-align:left;">
            <div style="font-size:11px; font-weight:bold; color:#a16207; margin-bottom:4px;">📌 Quick Insight:</div>
            <div style="font-size:11px; color:#a16207;">- งานซ้ำซ้อน: 2 จุด</div>
            <div style="font-size:11px; color:#a16207;">- โครงสร้างขาด: 1 จุด</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. Smart Recommendation + Compare -->
    <h2 class="section-title">💡 2. Smart Recommendation + Compare (วิเคราะห์อัจฉริยะ)</h2>
    <div class="grid-2-smart">
      <!-- 2.1 AI Panel -->
      <div class="panel">
        <h3 style="font-size:14px; margin-bottom:15px; display:flex; align-items:center; gap:8px;"><span style="font-size:18px;">🤖</span> ระบบแนะนำให้ปรับปรุง 3 จุด</h3>
        <ul class="ai-list">
          <li class="ai-item">
            <div style="flex:1;">
              <div style="font-weight:800; font-size:12px; color:var(--navy); margin-bottom:3px;">งานซ้ำซ้อน (Duplicate)</div>
              <div style="font-size:11px; color:var(--gray-500); line-height:1.4;">"งานธุรการและสารบรรณ" มีบทบาทซ้ำซ้อนระหว่างกองคลังและกองพัสดุ</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px; align-items:flex-end; margin-left:10px;">
              <span class="ai-badge high">High Impact</span>
              <button class="btn btn-outline" style="padding:4px 10px; font-size:10px;">✔ Apply Fix</button>
            </div>
          </li>
          <li class="ai-item">
            <div style="flex:1;">
              <div style="font-weight:800; font-size:12px; color:var(--navy); margin-bottom:3px;">โครงสร้างไม่สมดุล (Unbalanced)</div>
              <div style="font-size:11px; color:var(--gray-500); line-height:1.4;">ปริมาณงาน IT ล้นในสำนักวิชาการ แนะนำตั้งหน่วยงานใหม่รองรับ</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px; align-items:flex-end; margin-left:10px;">
              <span class="ai-badge med">Medium Impact</span>
              <button class="btn btn-outline" style="padding:4px 10px; font-size:10px;">👁 Preview</button>
            </div>
          </li>
        </ul>
      </div>
      
      <!-- 2.2 Compare Mode -->
      <div class="panel">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
          <h3 style="font-size:14px; margin:0;">⚖️ Compare Mode: สำนักเทคโนโลยีสารสนเทศ</h3>
          <div style="font-size:11px; display:flex; gap:12px; font-weight:bold;">
            <span style="color:#16a34a;">🟢 เพิ่ม (Added)</span>
            <span style="color:#dc2626;">🔴 ลบ (Removed)</span>
            <span style="color:#d97706;">🟡 แก้ไข (Modified)</span>
          </div>
        </div>
        <div class="compare-split">
          <div class="tree-box">
            <div style="font-weight:800; margin-bottom:12px; color:var(--gray-500); border-bottom:1px solid #e2e8f0; padding-bottom:5px;">Tree A (โครงสร้างเดิม)</div>
            <div class="tree-node-item">ฝ่ายพัฒนาระบบเครือข่าย</div>
            <div class="tree-node-item removed">ฝ่ายซ่อมบำรุงคอมพิวเตอร์</div>
            <div class="tree-node-item">ฝ่ายบริการวิชาการ IT</div>
          </div>
          <div class="tree-box" style="background:#f0f9ff; border-color:#bae6fd;">
            <div style="font-weight:800; margin-bottom:12px; color:var(--navy); border-bottom:1px solid #bae6fd; padding-bottom:5px;">Tree B (โครงสร้างแนะนำ)</div>
            <div class="tree-node-item modified">ฝ่ายนวัตกรรมดิจิทัล (ยุบรวม)</div>
            <div class="tree-node-item added">ศูนย์ความมั่นคงปลอดภัยไซเบอร์</div>
            <div class="tree-node-item">ฝ่ายบริการวิชาการ IT</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. Structure Workspace -->
    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:15px; margin-top:25px;">
      <h2 class="section-title" style="margin:0;">🏗️ 3. Structure Workspace (พื้นที่จัดการโครงสร้าง)</h2>
    </div>
    
    <div class="workspace-grid">
      <!-- 3.1 Left Panel: Function Library -->
      <div class="workspace-panel">
        <div class="workspace-header" style="display:flex; justify-content:space-between;">
          <span>🗂️ Function Library</span>
          <span style="cursor:pointer;">⚙️</span>
        </div>
        <div style="padding:10px; border-bottom:1px solid #e2e8f0; background:#f8fafc;">
          <input type="text" placeholder="🔍 ค้นหาภารกิจ (เช่น ไอที, การเงิน)" style="width:100%; padding:8px; font-size:11px; border:1px solid #cbd5e1; border-radius:6px; outline:none;">
          <div style="display:flex; gap:5px; margin-top:8px;">
            <span style="font-size:9px; background:#e2e8f0; padding:3px 6px; border-radius:4px; font-weight:bold;">ทั้งหมด</span>
            <span style="font-size:9px; background:#fff; border:1px solid #e2e8f0; padding:3px 6px; border-radius:4px;">วิชาชีพเฉพาะ</span>
          </div>
        </div>
        <div class="workspace-body">
          <div class="func-item"><span>📄</span> งานสารบรรณ (สนับสนุนทั่วไป)</div>
          <div class="func-item"><span>💰</span> งานการเงินและบัญชี (วิชาชีพเฉพาะ)</div>
          <div class="func-item"><span>🎓</span> งานทะเบียนนักศึกษา (วิชาการ)</div>
          <div class="func-item" style="opacity:0.5; border-style:dashed;"><span>🛡️</span> บริหารความเสี่ยง (อยู่ระหว่างร่าง)</div>
        </div>
      </div>
      
      <!-- 3.2 Main Canvas -->
      <div class="workspace-panel canvas-area">
        <div style="position:absolute; top:12px; left:12px; font-weight:800; color:var(--navy); background:#fff; padding:5px 10px; border-radius:6px; box-shadow:0 2px 4px rgba(0,0,0,0.05); font-size:12px;">
          📍 โครงสร้าง: สำนักเทคโนโลยีสารสนเทศ
        </div>
        <div style="position:absolute; top:12px; right:12px; display:flex; gap:8px;">
          <button class="btn btn-outline" style="padding:6px 12px; font-size:11px; background:#fff;">➕ Add Node</button>
          <button class="btn btn-outline" style="padding:6px 12px; font-size:11px; background:#fff;">↩️ Undo</button>
        </div>
        
        <div style="display:flex; flex-direction:column; align-items:center; gap:25px; margin-top:40px;">
          <!-- Parent -->
          <div class="node-card" style="background:var(--navy); color:#fff; border:none;">
            <div style="font-weight:800; font-size:13px; margin-bottom:2px;">ผู้อำนวยการสำนัก</div>
            <div style="font-size:10px; opacity:0.8;">สำนักเทคโนโลยีสารสนเทศ</div>
          </div>
          
          <div style="width:2px; height:25px; background:var(--navy); position:relative; margin-top:-25px; margin-bottom:-25px; z-index:1;"></div>
          
          <!-- Children row -->
          <div style="display:flex; gap:40px; position:relative;">
            <!-- Connector line across -->
            <div style="position:absolute; top:-12px; left:90px; right:90px; height:2px; background:var(--navy); z-index:1;"></div>
            
            <div style="display:flex; flex-direction:column; align-items:center; position:relative;">
               <div style="width:2px; height:12px; background:var(--navy); position:absolute; top:-12px;"></div>
               <div class="node-card" style="cursor:pointer; box-shadow:0 0 0 2px rgba(234, 179, 8, 0.4);">
                 <div style="font-weight:800; font-size:12px; color:var(--navy); margin-bottom:2px;">ฝ่ายนวัตกรรมดิจิทัล</div>
                 <div style="font-size:10px; color:var(--gray-500); background:#f1f5f9; padding:2px 5px; border-radius:4px; display:inline-block;">วิชาชีพเฉพาะ</div>
               </div>
            </div>
            
            <div style="display:flex; flex-direction:column; align-items:center; position:relative;">
               <div style="width:2px; height:12px; background:var(--navy); position:absolute; top:-12px;"></div>
               <div class="node-card" style="border-color:#22c55e; background:#f0fdf4; cursor:pointer;">
                 <div style="font-weight:800; font-size:12px; color:#166534; margin-bottom:2px;">ศูนย์ความมั่นคงไซเบอร์</div>
                 <div style="font-size:10px; color:#15803d; background:#dcfce7; padding:2px 5px; border-radius:4px; display:inline-block;">งานใหม่ ✨</div>
               </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 3.3 Right Panel: Properties -->
      <div class="workspace-panel">
        <div class="workspace-header">⚙️ Node Properties</div>
        <div class="workspace-body" style="background:#f8fafc;">
          <div style="background:#fff; padding:12px; border-radius:8px; border:1px solid #e2e8f0; margin-bottom:15px;">
            <label style="font-weight:800; display:block; margin-bottom:6px; color:var(--navy);">ชื่อภารกิจ/หน่วยงาน</label>
            <input type="text" value="ฝ่ายนวัตกรรมดิจิทัล" style="width:100%; padding:8px; font-size:12px; border:1px solid #cbd5e1; border-radius:6px; outline:none; font-family:'Sarabun';">
          </div>
          
          <div style="background:#fff; padding:12px; border-radius:8px; border:1px solid #e2e8f0; margin-bottom:15px;">
            <label style="font-weight:800; display:block; margin-bottom:6px; color:var(--navy);">ประเภทกลุ่มงาน</label>
            <select style="width:100%; padding:8px; font-size:12px; border:1px solid #cbd5e1; border-radius:6px; outline:none; font-family:'Sarabun';">
              <option>กลุ่มวิชาชีพเฉพาะ</option>
              <option>กลุ่มสนับสนุนวิชาการ</option>
              <option>กลุ่มสนับสนุนทั่วไป</option>
            </select>
          </div>
          
          <div style="background:#fff; padding:12px; border-radius:8px; border:1px solid #e2e8f0;">
            <label style="font-weight:800; display:block; margin-bottom:6px; color:var(--navy);">ความสัมพันธ์ (Relations)</label>
            <div style="font-size:11px; padding:8px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px;">
              <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                <span style="color:var(--gray-500);">⬆️ Parent:</span>
                <span style="font-weight:bold;">ผู้อำนวยการสำนัก</span>
              </div>
              <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                <span style="color:var(--gray-500);">⬇️ Child:</span>
                <span style="font-weight:bold;">-</span>
              </div>
              <div style="display:flex; justify-content:space-between;">
                <span style="color:var(--gray-500);">🔗 Dependency:</span>
                <span style="font-weight:bold; color:#0369a1;">IT Support</span>
              </div>
            </div>
          </div>
          
          <button class="btn btn-outline" style="width:100%; margin-top:15px; border-color:#ef4444; color:#ef4444;">🗑️ Delete Node</button>
        </div>
      </div>
    </div>

    <!-- 4. Validation & Submission -->
    <h2 class="section-title">✅ 4. Validation & Submission (ตรวจสอบและส่งมอบ)</h2>
    <div class="validation-grid">
      <!-- 4.1 Validation Panel -->
      <div class="panel">
        <h3 style="font-size:14px; margin-bottom:15px; font-weight:800; display:flex; justify-content:space-between; align-items:center;">
          <span>🔍 Pre-flight Checklist</span>
          <span style="font-size:10px; background:#fefce8; color:#a16207; padding:3px 8px; border-radius:10px; border:1px solid #fef08a;">พบข้อผิดพลาด 1 จุด</span>
        </h3>
        <div class="check-item" style="border-left: 3px solid #22c55e;">
          <span style="color:#22c55e; font-size:16px;">✅</span> 
          <span style="flex:1;">โครงสร้างมีข้อมูลครบถ้วน (ไม่มี Node ว่าง)</span>
        </div>
        <div class="check-item" style="border-left: 3px solid #ef4444; background:#fef2f2;">
          <span style="color:#ef4444; font-size:16px;">❌</span> 
          <div style="flex:1;">
            <div style="font-weight:bold; color:#991b1b;">พบงานทับซ้อน (Overlap)</div>
            <div style="font-size:11px; color:#b91c1c; margin-top:2px;">"ศูนย์ไซเบอร์" มีหน้าที่ซ้ำซ้อนกับ "ฝ่ายนวัตกรรม"</div>
          </div>
          <button class="btn btn-outline" style="padding:2px 8px; font-size:10px; background:#fff;">🔎 Highlight</button>
        </div>
        <div class="check-item" style="border-left: 3px solid #eab308;">
          <span style="color:#eab308; font-size:16px;">⚠️</span> 
          <span style="flex:1;">มาตรฐานภาระงานรวมเกินเกณฑ์กำหนด 5%</span>
        </div>
        <button class="btn btn-outline" style="width:100%; margin-top:10px; font-weight:bold;">↻ สั่งตรวจสอบอัตโนมัติอีกครั้ง</button>
      </div>
      
      <!-- 4.2 Submission Panel -->
      <div class="panel" style="background:#f8fafc; border:2px solid #e2e8f0;">
        <h3 style="font-size:14px; margin-bottom:15px; font-weight:800;">📤 Submission Form (แบบฟอร์มขออนุมัติ)</h3>
        <div style="margin-bottom:15px;">
          <label style="font-size:12px; font-weight:800; display:block; margin-bottom:6px;">เหตุผลการปรับปรุงโครงสร้าง (Justification)</label>
          <textarea rows="3" style="width:100%; padding:10px; font-size:12px; border:1px solid #cbd5e1; border-radius:8px; outline:none; font-family:'Sarabun';" placeholder="โปรดระบุเหตุผลความจำเป็นในการปรับโครงสร้าง เพื่อประกอบการพิจารณาของสภาฯ..."></textarea>
        </div>
        <div style="display:flex; gap:15px; margin-bottom:20px; background:#fff; padding:10px; border-radius:8px; border:1px solid #e2e8f0;">
          <label style="font-size:12px; font-weight:bold; display:flex; align-items:center; gap:5px; cursor:pointer;">
            <input type="radio" name="type" checked style="accent-color:var(--navy);"> Minor Change (ปรับเล็กน้อย)
          </label>
          <label style="font-size:12px; font-weight:bold; display:flex; align-items:center; gap:5px; cursor:pointer;">
            <input type="radio" name="type" style="accent-color:var(--navy);"> Major Change (รื้อโครงสร้างใหญ่)
          </label>
        </div>
        <div style="display:flex; gap:12px;">
          <button class="btn btn-outline" style="flex:1; padding:12px; font-weight:800;">💾 Save Draft</button>
          <button class="btn btn-primary" style="flex:2; padding:12px; font-weight:800; font-size:14px; box-shadow:0 4px 10px rgba(30, 58, 138, 0.3);" onclick="showToast('ส่งเรื่องให้ HR ตรวจสอบแล้วเรียบร้อย','success')">🚀 Submit to HR (ส่งให้ HR)</button>
        </div>
      </div>
    </div>

  </div>`;
    }
"""

text = re.sub(r'function renderMGRDashboard\(\) \{.*?\n    \}\n', new_content, text, flags=re.DOTALL)

with open('index2.html', 'w', encoding='utf-8') as f:
    f.write(text)
