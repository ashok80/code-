from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class BH_GM_DOCK(models.Model):
    bh_gm_dock_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('location', on_delete=models.CASCADE, null=True, blank=True)
    billing_cisco = models.CharField(max_length=255, null=True, blank=True)
    location_code = models.CharField(max_length=255, null=True, blank=True)
    duns = models.CharField(max_length=255, null=True, blank=True)
    facility_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    dock_code = models.CharField(max_length=255)
    simplified_dock = models.CharField(max_length=255, null=True, blank=True)
    no_of_shifts = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(3)])
    drop_deck_allowed_yn = models.BooleanField(null=True, blank=True)
    dock_bump_yn = models.BooleanField(null=True, blank=True)
    max_dock_bumps_allowed = models.IntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    co_locate = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.dock_code)

    class Meta:
        verbose_name = "BH_GM_DOCK"
        verbose_name_plural = "BH_GM_DOCKS"


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    locationid = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    state_prov_code = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    time_zone_gid = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_type = models.CharField(max_length=255)
    locode = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    duns = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    pickup_time_start = models.CharField(max_length=255)
    pickup_time_end = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    active = models.CharField(max_length=255)
    zip_city = models.CharField(max_length=255)
    location_office_type = models.CharField(max_length=255)
    alternate_duns = models.CharField(max_length=255)
    cisco_code = models.CharField(max_length=255)
    plant_code_2_letter = models.CharField(max_length=255)
    alternate_pk = models.IntegerField()
    batchid = models.CharField(max_length=255)
    record_status = models.CharField(max_length=255)
    message_tx = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    drc_supplier_load = models.IntegerField()
    source = models.CharField(max_length=255)
    schedule_date = models.DateTimeField()
    pickup_volume = models.FloatField()
    loading_time_per_ton_in_mins = models.FloatField()
    filter_status = models.CharField(max_length=255)
    alt_location_name = models.CharField(max_length=255)
    logistics_type = models.CharField(max_length=255)
    billing_cisco = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.location_name)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class DQ_FAILURE(models.Model):
    dq_failure_id = models.AutoField(primary_key=True)
    batchid = models.CharField(max_length=255)
    entity_id = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    business_rule = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now=True)
    dq_dimension = models.CharField(max_length=255)
    column_value = models.CharField(max_length=255)
    fixed_yn = models.CharField(max_length=255)
    fixed_date = models.DateTimeField()
    source = models.CharField(max_length=255)
    column_name = models.CharField(max_length=255)
    error_code = models.CharField(max_length=255)
    table_name = models.CharField(max_length=255)
    frequency = models.IntegerField()
    master_load_id = models.IntegerField()
    transaction_date = models.DateTimeField()
    alt_error_code = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.batchid)


class BH_GM_Constraint_Dock(models.Model):
    bh_origin_id = models.ForeignKey(BH_GM_DOCK, on_delete=models.CASCADE)
    bh_compatible_dock_id = models.IntegerField()

    def __str__(self):
        return "Origin - {} | compatible {}".format(self.bh_origin_id, self.bh_compatible_dock_id)

class Codemap(models.Model):
    code_map_id = models.IntegerField(db_column='CODE_MAP_ID')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    input_value = models.CharField(db_column='INPUT_VALUE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    output_value = models.CharField(db_column='OUTPUT_VALUE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    display_label = models.CharField(db_column='DISPLAY_LABEL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CODEMAP'
