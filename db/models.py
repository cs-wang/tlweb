from __future__ import unicode_literals

from django.db import models


class Advice(models.Model):
    advice_id = models.BigIntegerField(primary_key=True)
    user_name = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_name', blank=True, null=True)
    advice_content = models.CharField(max_length=255, blank=True, null=True)
    advice_created = models.DateTimeField(blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'advice'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CommissionDetail(models.Model):
    commission_type = models.CharField(primary_key=True, max_length=1)
    commission_desc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_detail'


class CommissionOrder(models.Model):
    commission_id = models.BigIntegerField(primary_key=True)
    user_name = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_name')
    commission_price = models.FloatField(blank=True, null=True)
    commission_type = models.ForeignKey(CommissionDetail, models.DO_NOTHING, db_column='commission_type')
    commission_memo = models.CharField(max_length=255, blank=True, null=True)
    commission_created = models.DateTimeField(blank=True, null=True)
    commission_sent = models.DateTimeField(blank=True, null=True)
    commission_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_order'
        unique_together = (('commission_id', 'user_name'),)


class DbMemberStatus(models.Model):
    status_id = models.CharField(max_length=1)
    status_desc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'db_member_status'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Member(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=500)
    nickname = models.CharField(max_length=10)
    status = models.ForeignKey('MemberStatus', models.DO_NOTHING)
    service_id = models.BigIntegerField(blank=True, null=True)
    reference_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    delegation_phone = models.CharField(max_length=20, blank=True, null=True)
    delegation_info = models.CharField(max_length=500, blank=True, null=True)
    bind_phone = models.CharField(max_length=20)
    weixin_id = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=255)
    account = models.CharField(max_length=50)
    card_holder = models.CharField(max_length=20, blank=True, null=True)
    receiver = models.CharField(max_length=20, blank=True, null=True)
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    receiver_addr = models.CharField(max_length=255, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'
def login(user,pwd,role):
    if role == 1:
        userEntity = Member.objects.filter(user_name = user)
        if userEntity.password == pwd:
            return True
        else
            return False
    else if role = 2:
        serviceEntity = Service.objects,filter(service_name = user)
        if serviceEntity.service_pwd == pwd:
            return True
        else
            return False

class MemberStatus(models.Model):
    status_id = models.CharField(primary_key=True, max_length=1)
    status_desc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_status'


class Message(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    message_title = models.CharField(max_length=255, blank=True, null=True)
    message_content = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    message_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class OrderForm(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    order_rank = models.BigIntegerField(blank=True, null=True)
    user_name = models.ForeignKey(Member, models.DO_NOTHING, db_column='user_name', blank=True, null=True)
    order_price = models.FloatField(blank=True, null=True)
    order_type = models.CharField(max_length=1, blank=True, null=True)
    order_created = models.DateTimeField(blank=True, null=True)
    order_finished = models.DateTimeField(blank=True, null=True)
    order_memo = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_form'


class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Service(models.Model):
    service_id = models.BigIntegerField(primary_key=True)
    service_name = models.CharField(max_length=20)
    service_pwd = models.CharField(max_length=500, blank=True, null=True)
    service_area = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceAccount(models.Model):
    service = models.ForeignKey(Service, models.DO_NOTHING)
    bank = models.CharField(primary_key=True, max_length=255)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    card_holder = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_account'


class ShortMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'short_message'

