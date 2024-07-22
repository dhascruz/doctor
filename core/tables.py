# example/app/tables.py
from crud.models import *
from doctor.models import *
from table import Table
from table.columns import Column

class TransTable(Table):
    id=Column(field='id')
    name=Column(field='idname')
    add_street=Column(field='nameadd_street')
    add_location=Column(field='add_streetadd_location')
    add_district=Column(field='add_locationadd_district')
    add_state=Column(field='add_districtadd_state')
    add_pincode=Column(field='add_stateadd_pincode')
    status=Column(field='add_pincodestatus')
    phone=Column(field='statusphone')
    sales_id=Column(field='phonesales_id')
    created_time=Column(field='sales_idcreated_time')
    update_time=Column(field='created_timeupdate_time')
    class Meta:
    
        model = Transactions