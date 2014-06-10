# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AbpAdfront(models.Model):
    frontid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)1111
    cont = models.TextField(blank=True)
    order = models.IntegerField(blank=True, null=True)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_adfront'

class AbpAdmin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=32) # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=50)
    lasttime = models.IntegerField()
    addtime = models.IntegerField()
    salt = models.CharField(max_length=4)
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    depart = models.CharField(max_length=200)
    memo = models.CharField(max_length=255)
    issuper = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_admin'

class AbpAdminLog(models.Model):
    logid = models.IntegerField(primary_key=True)
    addtime = models.IntegerField()
    adminid = models.IntegerField()
    uname = models.CharField(max_length=50)
    oper = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'abp_admin_log'

class AbpAdpic(models.Model):
    picid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_adpic'

class AbpAdword(models.Model):
    wordid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_adword'

class AbpAftersale(models.Model):
    afterid = models.IntegerField(primary_key=True)
    tradeid = models.BigIntegerField()
    orderid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    way = models.CharField(max_length=10)
    chgproductid = models.IntegerField()
    chgspec = models.CharField(max_length=50)
    problem = models.CharField(max_length=500)
    receiver_name = models.CharField(max_length=60)
    receiver_province = models.CharField(max_length=6)
    receiver_city = models.CharField(max_length=6)
    receiver_district = models.CharField(max_length=6)
    receiver_address = models.CharField(max_length=100)
    receiver_zip = models.CharField(max_length=6)
    receiver_link = models.CharField(max_length=20)
    addtime = models.IntegerField()
    isdeal = models.IntegerField()
    dealtime = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_aftersale'

class AbpBrand(models.Model):
    brandid = models.IntegerField(primary_key=True)
    brandname = models.CharField(max_length=100)
    brandurl = models.CharField(max_length=100)
    brandlogo = models.CharField(max_length=100)
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_brand'

class AbpCat(models.Model):
    catid = models.IntegerField(primary_key=True)
    catname = models.CharField(max_length=50)
    pid = models.IntegerField()
    typeid = models.IntegerField()
    unitid = models.IntegerField()
    order = models.IntegerField()
    pagetitle = models.CharField(max_length=100)
    pagekeywords = models.CharField(max_length=100)
    pagedesc = models.CharField(max_length=255)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_cat'

class AbpConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=20)
    val = models.TextField()
    type = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'abp_config'

class AbpContent(models.Model):
    contentid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    link = models.CharField(max_length=255)
    sortid = models.IntegerField()
    modifytime = models.IntegerField()
    addtime = models.IntegerField()
    contenttype = models.CharField(max_length=4)
    pagetitle = models.CharField(max_length=100)
    pagekeywords = models.CharField(max_length=100)
    pagedesc = models.CharField(max_length=255)
    order = models.IntegerField()
    ispublish = models.IntegerField()
    isdel = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_content'

class AbpContentSort(models.Model):
    sortid = models.IntegerField(primary_key=True)
    sortname = models.CharField(max_length=100)
    order = models.IntegerField()
    type = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_content_sort'

class AbpCoupon(models.Model):
    couponid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    endtime = models.IntegerField()
    deno = models.IntegerField()
    total = models.IntegerField()
    num = models.IntegerField()
    require = models.IntegerField()
    restrict = models.IntegerField()
    ispublish = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_coupon'

class AbpDiscount(models.Model):
    discountid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    begintime = models.IntegerField()
    endtime = models.IntegerField()
    ispublish = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_discount'

class AbpDiscountItem(models.Model):
    discountid = models.IntegerField()
    itemid = models.IntegerField()
    discount = models.IntegerField()
    limit = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_discount_item'

class AbpDistrict(models.Model):
    districtid = models.IntegerField(primary_key=True)
    district = models.CharField(max_length=50)
    order = models.IntegerField()
    pid = models.IntegerField()
    zipcode = models.CharField(max_length=6)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_district'

class AbpErpAdmin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=50, blank=True)
    pass_field = models.CharField(db_column='pass', max_length=32, blank=True) # Field renamed because it was a Python reserved word.
    salt = models.CharField(max_length=4, blank=True)
    role = models.CharField(max_length=50, blank=True)
    real_name = models.CharField(max_length=50, blank=True)
    depart = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=10, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    is_quit = models.IntegerField(blank=True, null=True)
    is_super = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    last_time = models.IntegerField(blank=True, null=True)
    create_ip = models.CharField(max_length=15, blank=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_admin'

class AbpErpAdminLog(models.Model):
    logid = models.IntegerField(primary_key=True)
    addtime = models.IntegerField()
    userid = models.IntegerField()
    uname = models.CharField(max_length=50)
    oper = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'abp_erp_admin_log'

class AbpErpDistribution(models.Model):
    distributionid = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=255, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    transferid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_distribution'

class AbpErpFinance(models.Model):
    financeid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_finance'

class AbpErpGroup(models.Model):
    groupid = models.IntegerField(blank=True, null=True)
    warehouseid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_group'

class AbpErpInventory(models.Model):
    inventoryid = models.IntegerField(primary_key=True)
    qty = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    warehouseid = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_inventory'

class AbpErpPaymode(models.Model):
    paymodeid = models.IntegerField(primary_key=True)
    paymodename = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_paymode'

class AbpErpPic(models.Model):
    picid = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=100, blank=True)
    addtime = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    spic = models.IntegerField(blank=True, null=True)
    mpic = models.IntegerField(blank=True, null=True)
    bpic = models.IntegerField(blank=True, null=True)
    isdel = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_pic'

class AbpErpPurchase(models.Model):
    purchaseid = models.IntegerField(primary_key=True)
    batch = models.CharField(max_length=50, blank=True)
    dates = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    supplierid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_purchase'

class AbpErpPurchaseData(models.Model):
    purchaseid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_purchase_data'

class AbpErpPurchaseImg(models.Model):
    purchaseid = models.IntegerField(blank=True, null=True)
    imgpath = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_purchase_img'

class AbpErpRecycle(models.Model):
    recycleid = models.IntegerField(primary_key=True)
    tableid = models.IntegerField()
    tablefield = models.CharField(max_length=255)
    table = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_erp_recycle'

class AbpErpReport(models.Model):
    reportid = models.IntegerField(primary_key=True)
    qty = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    adminid = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=50, blank=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_report'

class AbpErpRequest(models.Model):
    requestid = models.IntegerField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    dates = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    statusid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_request'

class AbpErpRequestData(models.Model):
    requestdataid = models.IntegerField(primary_key=True)
    requestid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    pronum = models.CharField(max_length=255, blank=True)
    proweight = models.CharField(max_length=255, blank=True)
    is_over = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_request_data'

class AbpErpRetail(models.Model):
    retailid = models.IntegerField(primary_key=True)
    sn = models.CharField(max_length=50, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    give = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    paymodeid = models.IntegerField(blank=True, null=True)
    iscoupon = models.IntegerField(blank=True, null=True)
    couponnum = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_retail'

class AbpErpRetailData(models.Model):
    retaildataid = models.IntegerField(primary_key=True)
    retailid = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True)
    qty = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    is_cancel = models.IntegerField(blank=True, null=True)
    is_return = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_retail_data'

class AbpErpReturns(models.Model):
    returnsid = models.IntegerField(primary_key=True)
    qty = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    returns_time = models.IntegerField(blank=True, null=True)
    retaildataid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_returns'

class AbpErpRole(models.Model):
    roleid = models.IntegerField(primary_key=True)
    rolename = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    privilege = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_role'

class AbpErpSell(models.Model):
    sellid = models.IntegerField(primary_key=True)
    setname = models.CharField(max_length=255, blank=True)
    setvalue = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_sell'

class AbpErpSetup(models.Model):
    setupid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=255, blank=True)
    is_open = models.TextField(blank=True) # This field type is a guess.
    create_time = models.DateTimeField(blank=True, null=True)
    modity_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_setup'

class AbpErpShop(models.Model):
    shopid = models.IntegerField(primary_key=True)
    shopname = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(blank=True, null=True)
    is_use = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_shop'

class AbpErpShopStock(models.Model):
    stockid = models.IntegerField(primary_key=True)
    qty = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_shop_stock'

class AbpErpShopType(models.Model):
    typeid = models.IntegerField(primary_key=True)
    typename = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_shop_type'

class AbpErpStatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    statusname = models.CharField(max_length=50, blank=True)
    statustype = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    is_del = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_status'

class AbpErpStockin(models.Model):
    stockinid = models.IntegerField(primary_key=True)
    batch = models.CharField(max_length=50, blank=True)
    barcode = models.CharField(max_length=50, blank=True)
    qty = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    warehouseid = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_stockin'

class AbpErpStockout(models.Model):
    responseid = models.IntegerField(primary_key=True)
    kind = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    warehouseid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_stockout'

class AbpErpSupplier(models.Model):
    supplierid = models.IntegerField(primary_key=True)
    suppliername = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bank_name = models.CharField(max_length=50, blank=True)
    bank_accounts = models.CharField(max_length=50, blank=True)
    bank_account_name = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(blank=True, null=True)
    is_use = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_supplier'

class AbpErpSystem(models.Model):
    key = models.CharField(primary_key=True, max_length=20)
    val = models.TextField()
    type = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'abp_erp_system'

class AbpErpTransfer(models.Model):
    transferid = models.IntegerField(primary_key=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    verifier = models.IntegerField(blank=True, null=True)
    requestid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_transfer'

class AbpErpTransferData(models.Model):
    transferdataid = models.IntegerField(primary_key=True)
    transferid = models.IntegerField(blank=True, null=True)
    warehouseid = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_transfer_data'

class AbpErpTransferItem(models.Model):
    transferdataid = models.IntegerField(blank=True, null=True)
    stockinid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_transfer_item'

class AbpErpWarehouse(models.Model):
    warehouseid = models.IntegerField(primary_key=True)
    warehousename = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bank_name = models.CharField(max_length=50, blank=True)
    bank_accounts = models.CharField(max_length=50, blank=True)
    bank_account_name = models.CharField(max_length=50, blank=True)
    license = models.CharField(max_length=255, blank=True)
    tax = models.CharField(max_length=255, blank=True)
    acreage = models.CharField(max_length=50, blank=True)
    caps = models.CharField(max_length=50, blank=True)
    limit = models.CharField(max_length=50, blank=True)
    is_use = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    modity_time = models.IntegerField(blank=True, null=True)
    adminid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_erp_warehouse'

class AbpExpressAddr(models.Model):
    addrid = models.IntegerField(primary_key=True)
    linkman = models.CharField(max_length=50)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=6)
    address = models.CharField(max_length=255)
    link = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    getdefault = models.IntegerField()
    backdefault = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_express_addr'

class AbpExpressCompany(models.Model):
    companyid = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=10)
    kuaidi = models.CharField(max_length=50)
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_express_company'

class AbpExpressOpt(models.Model):
    tplid = models.IntegerField()
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    width = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    left = models.CharField(max_length=20)
    top = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_express_opt'

class AbpExpressPic(models.Model):
    picid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    companyid = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    tplpic = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'abp_express_pic'

class AbpExpressProv(models.Model):
    wayid = models.IntegerField()
    price = models.IntegerField()
    province = models.TextField()
    class Meta:
        managed = False
        db_table = 'abp_express_prov'

class AbpExpressTpl(models.Model):
    tplid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    companyid = models.IntegerField()
    tplpic = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    isdefault = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_express_tpl'

class AbpExpressWay(models.Model):
    wayid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    feetype = models.CharField(max_length=5)
    defaultfee = models.IntegerField()
    price = models.IntegerField()
    status = models.IntegerField()
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_express_way'

class AbpGifts(models.Model):
    giftid = models.IntegerField(primary_key=True)
    itemid = models.IntegerField()
    subject = models.CharField(max_length=100)
    gift = models.TextField()
    begintime = models.IntegerField()
    endtime = models.IntegerField()
    ispublish = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_gifts'

class AbpItem(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=255, blank=True)
    barcode = models.CharField(max_length=255, blank=True)
    bn = models.CharField(max_length=100, blank=True)
    price = models.BigIntegerField(blank=True, null=True)
    mkprice = models.BigIntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    itemimg = models.CharField(max_length=255, blank=True)
    inventory = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    favors = models.IntegerField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    brandid = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    modified = models.IntegerField(blank=True, null=True)
    view = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    outer = models.CharField(max_length=10, blank=True)
    outerid = models.CharField(max_length=20, blank=True)
    isdel = models.IntegerField(blank=True, null=True)
    pnotify = models.IntegerField(blank=True, null=True)
    comprice = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_item'

class AbpItemCat(models.Model):
    itemid = models.IntegerField()
    catid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_item_cat'

class AbpItemCorrelation(models.Model):
    itemid = models.IntegerField()
    fitemid = models.IntegerField()
    linktype = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_item_correlation'

class AbpItemDesc(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemdesc = models.TextField()
    pagetitle = models.CharField(max_length=100)
    pagekeywords = models.CharField(max_length=100)
    pagedesc = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'abp_item_desc'

class AbpItemImg(models.Model):
    imgid = models.IntegerField(primary_key=True)
    itemid = models.IntegerField()
    imgpath = models.CharField(max_length=100)
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_item_img'

class AbpItemProperty(models.Model):
    itemid = models.IntegerField()
    propertyid = models.IntegerField()
    propertyvalueid = models.IntegerField()
    self = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_item_property'

class AbpItemSpec(models.Model):
    itemid = models.IntegerField()
    specid = models.IntegerField()
    self = models.TextField()
    class Meta:
        managed = False
        db_table = 'abp_item_spec'

class AbpItemTag(models.Model):
    itemid = models.IntegerField()
    tagid = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_item_tag'

class AbpLetter(models.Model):
    letterid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=11)
    content = models.CharField(max_length=255)
    uid = models.IntegerField()
    uname = models.CharField(max_length=50)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_letter'

class AbpLink(models.Model):
    linkid = models.IntegerField(primary_key=True)
    linkname = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    linkpic = models.CharField(max_length=200)
    order = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_link'

class AbpMan(models.Model):
    manid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    begintime = models.IntegerField()
    endtime = models.IntegerField()
    ispublish = models.IntegerField()
    method = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_man'

class AbpManRule(models.Model):
    ruleid = models.IntegerField(primary_key=True)
    manid = models.IntegerField()
    manorder = models.IntegerField()
    minus = models.IntegerField()
    giftname = models.CharField(max_length=50)
    gifturl = models.CharField(max_length=200)
    nofreight = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_man_rule'

class AbpMeal(models.Model):
    mealid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=255)
    itemimg = models.CharField(max_length=255)
    begintime = models.IntegerField()
    endtime = models.IntegerField()
    oldprice = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    order = models.IntegerField()
    volume = models.IntegerField()
    ispublish = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_meal'

class AbpMealItem(models.Model):
    mealid = models.IntegerField()
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=255)
    itemimg = models.CharField(max_length=255)
    price = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_meal_item'

class AbpMessageSet(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    text = models.CharField(max_length=10)
    email = models.IntegerField()
    mobile = models.IntegerField()
    letter = models.IntegerField()
    mobilecont = models.CharField(max_length=255)
    emailcont = models.TextField(blank=True)
    lettercont = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'abp_message_set'

class AbpNavi(models.Model):
    naviid = models.IntegerField(primary_key=True)
    naviname = models.CharField(max_length=50)
    naviurl = models.CharField(max_length=255)
    tableid = models.IntegerField()
    tabletype = models.IntegerField()
    isdel = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_navi'

class AbpNotifyContent(models.Model):
    contentid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=5)
    issend = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_notify_content'

class AbpNotifyQueue(models.Model):
    contentid = models.IntegerField()
    notify = models.CharField(max_length=60)
    type = models.CharField(max_length=5)
    addtime = models.IntegerField()
    msg = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'abp_notify_queue'

class AbpNotifySender(models.Model):
    contentid = models.IntegerField(primary_key=True)
    receiver = models.CharField(max_length=60)
    type = models.CharField(max_length=5)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_notify_sender'

class AbpOrder(models.Model):
    orderid = models.IntegerField(primary_key=True)
    tradeid = models.BigIntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=255)
    ibn = models.CharField(max_length=50)
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    itemimg = models.CharField(max_length=100)
    pbn = models.CharField(max_length=50)
    productid = models.IntegerField()
    num = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()
    tuan = models.IntegerField()
    mealtitle = models.CharField(max_length=100)
    addtime = models.IntegerField()
    applied = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_order'

class AbpPage(models.Model):
    pageid = models.IntegerField(primary_key=True)
    pagetitle = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    addtime = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_page'

class AbpPayment(models.Model):
    paymentid = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    paykey = models.CharField(max_length=50)
    paysecret = models.CharField(max_length=50)
    account = models.CharField(max_length=100)
    weburl = models.CharField(max_length=255)
    order = models.IntegerField()
    ispublish = models.IntegerField()
    memo = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'abp_payment'

class AbpPic(models.Model):
    picid = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    addtime = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    size = models.IntegerField()
    spic = models.IntegerField()
    mpic = models.IntegerField()
    bpic = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_pic'

class AbpProduct(models.Model):
    productid = models.IntegerField(primary_key=True)
    itemid = models.IntegerField()
    bn = models.CharField(max_length=100)
    inventory = models.IntegerField()
    price = models.IntegerField()
    volume = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_product'

class AbpProductSpec(models.Model):
    productid = models.IntegerField()
    itemid = models.IntegerField()
    specid = models.IntegerField()
    specvalid = models.IntegerField()
    typeid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_product_spec'

class AbpRecycle(models.Model):
    recycleid = models.IntegerField(primary_key=True)
    tableid = models.IntegerField()
    tablefield = models.CharField(max_length=255)
    table = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_recycle'

class AbpRole(models.Model):
    roleid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    privilege = models.CharField(max_length=50)
    lasttime = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_role'

class AbpSales(models.Model):
    saleid = models.IntegerField(primary_key=True)
    tradeid = models.BigIntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    itemid = models.IntegerField()
    productid = models.IntegerField()
    ibn = models.CharField(max_length=50)
    pbn = models.CharField(max_length=50)
    itemname = models.CharField(max_length=255)
    itemimg = models.CharField(max_length=255)
    price = models.IntegerField()
    num = models.IntegerField()
    saletime = models.IntegerField()
    finishtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_sales'

class AbpSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=32)
    session_data = models.TextField()
    time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_session'

class AbpSpec(models.Model):
    specid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    memo = models.CharField(max_length=50)
    type = models.CharField(max_length=5)
    tbpid = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_spec'

class AbpSpecpic(models.Model):
    picid = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=100)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_specpic'

class AbpSpecval(models.Model):
    specvalid = models.IntegerField(primary_key=True)
    specid = models.IntegerField()
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    order = models.IntegerField()
    tbvid = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_specval'

class AbpTag(models.Model):
    tagid = models.IntegerField(primary_key=True)
    tagname = models.CharField(max_length=50)
    pic = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    ismore = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_tag'

class AbpTlogin(models.Model):
    tloginid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    host = models.CharField(max_length=10)
    appkey = models.CharField(max_length=100)
    appsecret = models.CharField(max_length=100)
    ispublish = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_tlogin'

class AbpTrade(models.Model):
    tradeid = models.BigIntegerField(primary_key=True)
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    addtime = models.IntegerField()
    modified = models.IntegerField()
    endtime = models.IntegerField()
    status = models.CharField(max_length=10)
    totalfee = models.IntegerField()
    postfee = models.IntegerField()
    itemfee = models.IntegerField()
    editfeetime = models.IntegerField()
    editfeememo = models.CharField(max_length=50)
    man = models.CharField(max_length=50)
    coupon = models.IntegerField()
    posttype = models.IntegerField()
    expresswayid = models.IntegerField()
    receiver_name = models.CharField(max_length=20)
    receiver_province = models.CharField(max_length=30)
    receiver_city = models.CharField(max_length=30)
    receiver_district = models.CharField(max_length=30)
    receiver_address = models.CharField(max_length=255)
    receiver_zip = models.CharField(max_length=6)
    receiver_link = models.CharField(max_length=15)
    send = models.CharField(max_length=50)
    sendtime = models.IntegerField()
    consign_time = models.IntegerField()
    memo = models.CharField(max_length=100)
    payment = models.CharField(max_length=10)
    outtradeid = models.CharField(max_length=40)
    paytime = models.IntegerField()
    istax = models.IntegerField()
    tax_company = models.CharField(max_length=100)
    isfinish = models.IntegerField()
    iscancel = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_trade'

class AbpTradeGift(models.Model):
    tradeid = models.BigIntegerField()
    orderid = models.IntegerField()
    itemid = models.IntegerField()
    productid = models.IntegerField()
    gift = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'abp_trade_gift'

class AbpTradePromotion(models.Model):
    tradeid = models.BigIntegerField()
    typeid = models.IntegerField()
    type = models.CharField(max_length=20)
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_trade_promotion'

class AbpTradeSend(models.Model):
    tradeid = models.BigIntegerField(primary_key=True)
    sendno = models.CharField(max_length=50)
    companyid = models.IntegerField()
    sendtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_trade_send'

class AbpTuan(models.Model):
    tuanid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100)
    itemid = models.IntegerField()
    begintime = models.IntegerField()
    endtime = models.IntegerField()
    price = models.IntegerField()
    buynum = models.IntegerField()
    ispublish = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_tuan'

class AbpTuanDesc(models.Model):
    tuanid = models.IntegerField(primary_key=True)
    desc = models.TextField()
    class Meta:
        managed = False
        db_table = 'abp_tuan_desc'

class AbpType(models.Model):
    typeid = models.IntegerField(primary_key=True)
    typename = models.CharField(max_length=50)
    isdel = models.IntegerField()
    tbcid = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_type'

class AbpTypeBrand(models.Model):
    typeid = models.IntegerField()
    brandid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_type_brand'

class AbpTypeProperty(models.Model):
    propertyid = models.IntegerField(primary_key=True)
    typeid = models.IntegerField()
    propertyname = models.CharField(max_length=255)
    dptype = models.IntegerField()
    isdp = models.IntegerField()
    selval = models.CharField(max_length=255)
    order = models.IntegerField()
    tbpid = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_type_property'

class AbpTypePropertyvalue(models.Model):
    valueid = models.IntegerField(primary_key=True)
    propertyid = models.IntegerField()
    propertyvalue = models.CharField(max_length=50)
    order = models.IntegerField()
    typeid = models.IntegerField()
    tbvid = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'abp_type_propertyvalue'

class AbpTypeSpec(models.Model):
    typeid = models.IntegerField()
    specid = models.IntegerField()
    specdptype = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_type_spec'

class AbpUnit(models.Model):
    unitid = models.IntegerField(primary_key=True)
    unitname = models.CharField(max_length=50, blank=True)
    unitval = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    isdel = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'abp_unit'

class AbpUser(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=100, blank=True)
    pass_field = models.CharField(db_column='pass', max_length=50, blank=True) # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=30, blank=True)
    sex = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    regip = models.CharField(max_length=15, blank=True)
    regtime = models.IntegerField(blank=True, null=True)
    lasttime = models.IntegerField(blank=True, null=True)
    lastpost = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True)
    salt = models.CharField(max_length=4, blank=True)
    source = models.CharField(max_length=10, blank=True)
    source_identity = models.CharField(max_length=50, blank=True)
    mailkey = models.CharField(max_length=8, blank=True)
    mailtime = models.IntegerField(blank=True, null=True)
    isdel = models.IntegerField(blank=True, null=True)
    unread = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_user'

class AbpUserAddress(models.Model):
    addressid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    receiver = models.CharField(max_length=50)
    province = models.CharField(max_length=6)
    city = models.CharField(max_length=6)
    district = models.CharField(max_length=6)
    address = models.CharField(max_length=255)
    link = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    class Meta:
        managed = False
        db_table = 'abp_user_address'

class AbpUserComment(models.Model):
    commentid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    itemid = models.IntegerField()
    addtime = models.IntegerField()
    replytime = models.IntegerField()
    ip = models.CharField(max_length=15)
    score = models.IntegerField()
    content = models.CharField(max_length=255)
    replycontent = models.CharField(max_length=255)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_comment'

class AbpUserComprice(models.Model):
    compriceid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    itemid = models.IntegerField()
    productid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    itemimg = models.CharField(max_length=255)
    price = models.IntegerField()
    comprice = models.CharField(max_length=50)
    comweburl = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    addtime = models.IntegerField()
    replytime = models.IntegerField()
    replycontent = models.CharField(max_length=255)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_comprice'

class AbpUserCoupon(models.Model):
    couponid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    isused = models.IntegerField()
    tradeid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_coupon'

class AbpUserFavor(models.Model):
    itemid = models.IntegerField()
    uid = models.IntegerField()
    addtime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_favor'

class AbpUserGroup(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(max_length=255, blank=True)
    pointlower = models.IntegerField(blank=True, null=True)
    pointupper = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True)
    isspecial = models.TextField(blank=True) # This field type is a guess.
    isdel = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abp_user_group'

class AbpUserLevel(models.Model):
    levelid = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=100)
    leveltype = models.CharField(max_length=6)
    grade = models.IntegerField()
    discount = models.IntegerField()
    nofreight = models.IntegerField()
    speitem = models.IntegerField()
    needtotal = models.IntegerField()
    needone = models.IntegerField()
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_level'

class AbpUserNotify(models.Model):
    notifyid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    uname = models.CharField(max_length=50)
    itemid = models.IntegerField()
    productid = models.IntegerField()
    itemname = models.CharField(max_length=255)
    itemimg = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    addtime = models.IntegerField()
    notifytime = models.IntegerField()
    isdeal = models.IntegerField()
    type = models.CharField(max_length=10)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_notify'

class AbpUserQa(models.Model):
    qaid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    itemid = models.IntegerField()
    addtime = models.IntegerField()
    replytime = models.IntegerField()
    content = models.CharField(max_length=255)
    replycontent = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    isdel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'abp_user_qa'

