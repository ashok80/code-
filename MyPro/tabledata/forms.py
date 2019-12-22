from django.forms import ModelForm
from tabledata.models import BH_GM_DOCK


class BHGMDOCKForm(ModelForm):
    class Meta:
        model = BH_GM_DOCK
        fields = '__all__'
