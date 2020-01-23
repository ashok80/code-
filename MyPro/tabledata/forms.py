from django.forms import ModelForm
from tabledata.models import BH_GM_DOCK, Codemap


class BHGMDOCKForm(ModelForm):
    class Meta:
        model = BH_GM_DOCK
        fields = '__all__'


class CodeMapForm(ModelForm):
    class Meta:
        model = Codemap
        fields = '__all__'


class CodeMapEditForm(ModelForm):
    class Meta:
        model = Codemap
        fields = ('input_value', 'output_value', )


class CodeMapFinal(ModelForm):
    class Meta:
        model = Codemap
        fields = ('input_value', 'output_value',)

