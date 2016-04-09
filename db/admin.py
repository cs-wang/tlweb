from django.contrib import admin
 
# Register your models here.
from db.models import MemberStatus,Advice,CommissionDetail,CommissionOrder,Member,Message,OrderForm,Product,Service,ServiceAccount,ShortMessage
 
class MemberStatuss(admin.ModelAdmin):
    list_display=('status_id','status_desc')
    search_fields=('status_id','status_desc')
class Advices(admin.ModelAdmin):
    list_display=('advice_id','user_id','advice_title','advice_content','advice_created','reply_time','service','advice_status','reply_content')
    search_fields=('advice_id','user_id','advice_title','advice_content','advice_created','reply_time','service','advice_status','reply_content')
class CommissionDetails(admin.ModelAdmin):
    list_display=('commission_type','commission_desc')
    search_fields=('commission_type','commission_desc')
class CommissionOrders(admin.ModelAdmin):
    list_display=('commission_id','user_id','commission_price','commission_type','commission_memo','commission_created',\
                  'commission_sent','commission_status')
    search_fields=('commission_id','user_id','commission_price','commission_type','commission_memo','commission_created',\
                   'commission_sent','commission_status')
class Members(admin.ModelAdmin):
    list_display=('user_name','password','nickname','status','service_id','reference_id','user_id','delegation_phone',\
                  'delegation_info','bind_phone','weixin_id','bank','account','card_holder','receiver',\
                  'receiver_phone','receiver_addr','register_time','confirm_time')
    search_fields=('user_name','password','nickname','status','service_id','reference_id','user_id','delegation_phone',\
                   'delegation_info','bind_phone','weixin_id','bank','account','card_holder','receiver',\
                   'receiver_phone','receiver_addr','register_time','confirm_time')
class Messages(admin.ModelAdmin):
    list_display=('message_id','message_title','message_content','sent_time','message_status','user_id','service_id')
    search_fields=('message_id','message_title','message_content','sent_time','message_status','user_id','service_id')
class OrderForms(admin.ModelAdmin):
    list_display=('order_id','service_id','order_valid_time','user_id','order_price','order_type','order_created','order_finished',\
                  'order_memo','order_status','express_name','express_number')
    search_fields=('order_id','service_id','order_valid_time','user_id','order_price','order_type','order_created','order_finished',\
                  'order_memo','order_status','express_name','express_number')
class Products(admin.ModelAdmin):
    list_display=('product_id','product_name','product_price')
    search_fields=('product_id','product_name','product_price')
class Services(admin.ModelAdmin):
    list_display=('service_id','service_name','service_pwd','service_area','role','service_response','service_memo','service_ref')
    search_fields=('service_id','service_name','service_pwd','service_area','role','service_response','service_memo','service_ref')
class ServiceAccounts(admin.ModelAdmin):
    list_display=('service','bank','bank_account','card_holder','phone')
    search_fields=('service','bank','bank_account','card_holder','phone')
class ShortMessages(admin.ModelAdmin):
    list_display=('message_id','message_content')
    search_fields=('message_id','message_content')
 
admin.site.register(MemberStatus,MemberStatuss)
admin.site.register(Advice,Advices)
admin.site.register(CommissionDetail,CommissionDetails)
admin.site.register(CommissionOrder,CommissionOrders)
admin.site.register(Member,Members)
admin.site.register(Message,Messages)
admin.site.register(OrderForm,OrderForms)
admin.site.register(Product,Products)
admin.site.register(Service,Services)
admin.site.register(ServiceAccount,ServiceAccounts)
admin.site.register(ShortMessage,ShortMessages)


