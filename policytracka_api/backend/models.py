from django.db import models

# Create your models here.
# Create your models here. ฐานข้อมูล
class Policydata(models.Model):
    title=models.CharField(max_length=255,unique=True) #การบรรจุข้อความได้สูงสุดประมาณ 255ตัวอักษร และตรวจจับชื่อและรหัสที่ซ้ำกัน
    detail=models.SlugField(max_length=5000,unique=False)
    policy_owner=models.CharField(max_length=255,unique=False)
    
    def __str__(self): #บ่งบอกหมวดหมู่ Category
        return self.name 
    
    # class Meta : #การตั้งค่าภาษาไทยหน้า admin 
    #     ordering=('name',) #การเรียงตัวอักษร
    #     verbose_name='หมวดหมู่สินค้า'
    #     verbose_name_plural="ข้อมูลประเภทสินค้า"