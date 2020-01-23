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
        widgets = {
            'code_map_id': TextInput(attrs={'readonly': 'readonly'}),
        }
        fields = ('input_value', 'output_value', 'code_map_id')

