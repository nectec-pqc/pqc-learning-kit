# Post-Quantum Cryptophgraphy (PQC) Learning Toolkit

# ช่องทางการเข้าถึงเอกสาร

เนื้อหาใน Learning Kit จัดเก็บอยู่ในรูปแบบ Markdown ใน git repository เป็นหลัก
เพื่อให้รองรับการปรับปรุงข้อมูลอย่างต่อเนื่องและเป็นระบบ อย่างไรก็ตาม
ผู้อ่านสามารถเลือกเข้าถึงเอกสารในรูปแบบที่อ่านสะดวกขึ้นได้ดังนี้:

## อ่าน online ผ่านเว็บเบราว์เซอร์ (แนะนำสำหรับผู้อ่านทั่วไป)

สามารถอ่านเอกสารในรูปแบบเว็บไซต์ที่จัดหน้ากระดาษให้อ่านง่ายได้ทันทีที่
https://nectec-pqc.github.io/pqc-learning-kit

## อ่านบน server ส่วนตัว

สำหรับผู้เขียนที่ต้องการตรวจสอบการจัดหน้าก่อน upload ขึ้น Github Pages
สามารถที่จะ clone repository นี้แล้วรัน
[docsify-cli](https://github.com/docsifyjs/docsify-cli)
เพื่อดูเอกสารในเครื่องส่วนตัวที่กำลังถูกแก้ไขในรูปแบบเว็บไซต์ได้
วิธีการติดตั่งและรัน server มีดังนี้

```shell
npm install -g docsify-cli

git clone git@github.com:apiwat-chantawibul/pqc-demo.git
cd pqc-demo
docsify serve . --open
```
