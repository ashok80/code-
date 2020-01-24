from django.forms import ModelForm
from tabledata.models import BH_GM_DOCK, Codemap
from django.forms import TextInput


class BHGMDOCKForm(ModelForm):
    class Meta:
        model = BH_GM_DOCK
        fields = '__all__'


class CodeMapFinal(ModelForm):
    class Meta:
        model = Codemap
        fields = ('id', 'input_value', 'output_value')
