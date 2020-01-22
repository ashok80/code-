import csv
from django.utils import timezone
from django.views import View
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.http import HttpResponse
from tabledata.models import BH_GM_DOCK, Location, DQ_FAILURE, BH_GM_Constraint_Dock, Codemap
from tabledata.forms import BHGMDOCKForm, CodeMapForm
from django.core import serializers
from tabledata.resources import DQ_FAILUREResource


class Home(View):
    template_name = 'tabledata/home.html'

    def get(self, request):
        data = BH_GM_DOCK.objects.all().order_by('-bh_gm_dock_id')

        row_list = list()
        rows = dict()

        for i in data:
            rows['bh_gm_dock_id'] = i.bh_gm_dock_id
            rows['location_id'] = i.location
            rows['billing_cisco'] = i.billing_cisco
            rows['location_code'] = i.location_code
            rows['duns'] = i.duns
            rows['facility_name'] = i.facility_name
            rows['zip_code'] = i.zip_code
            rows['dock_code'] = i.dock_code
            rows['simplified_dock'] = i.simplified_dock
            rows['no_of_shifts'] = i.no_of_shifts
            rows['drop_deck_allowed_yn'] = i.drop_deck_allowed_yn
            rows['dock_bump_yn'] = i.dock_bump_yn
            rows['max_dock_bumps_allowed'] = i.max_dock_bumps_allowed
            rows['date_entered'] = i.date_entered
            rows['notes'] = i.notes
            rows['co_locate'] = i.co_locate
            rows['source'] = i.source

            if i.location:
                query = Location.objects.get(location_id=i.location.location_id)
                rows['city'] = query.city
                rows['state'] = query.state
            else:
                rows['city'] = 'None'
                rows['state'] = 'None'

            row_list.append(rows)
            rows = dict()
        return render(request, template_name=self.template_name, context={'rows': row_list})


class DownloadDQFaliure(View):

    def get(self, request):
        resource_object = DQ_FAILUREResource()
        export = resource_object.export()
        response = HttpResponse(export.csv, content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=DQ_FAILURE.csv'
        return response


class EditBHGMDock(View):
    template_name = 'tabledata/edit.html'

    def get(self, request, id):
        if not id:
            return render(request, 'tabledata/404.html')
        else:
            data = BH_GM_DOCK.objects.get(bh_gm_dock_id=id)
            form = BHGMDOCKForm(instance=data)

            dock_with_same_location = None
            if data.location:
                try:
                    dock_with_same_location = BH_GM_DOCK.objects.filter(location=data.location).exclude(bh_gm_dock_id=id)
                except BH_GM_DOCK.DoesNotExist:
                    pass
            try:
                return render(request, 'tabledata/edit.html', context={"rows": data, 'form': form, 'similar_docks': dock_with_same_location})
            except IndexError:
                return render(request, 'tabledata/404.html')

    def post(self, request, id):
        form = BHGMDOCKForm(request.POST)
        if form.is_valid():
            if request.POST.get('drop_deck_allowed_yn') == 'false':
                drop_deck_allowed_yn = False
            elif request.POST.get('drop_deck_allowed_yn') == 'true':
                drop_deck_allowed_yn = True
            else:
                drop_deck_allowed_yn = None

            if request.POST.get('dock_bump_yn') == 'false':
                dock_bump_yn = False
            elif request.POST.get('dock_bump_yn') == 'true':
                dock_bump_yn = True
            else:
                dock_bump_yn = None

            location_id = request.POST.get("location-id")
            location_model_instance = None
            try:
                if location_id:
                    location_model_instance = Location.objects.get(locationid=location_id)
            except Location.DoesNotExist:
                print("Location does not exists with the {} locationid".format(location_id))

            model_instance = BH_GM_DOCK.objects.get(bh_gm_dock_id=id)
            model_instance.location = location_model_instance

            model_instance.billing_cisco=request.POST.get('billing_cisco')
            model_instance.location_code=request.POST.get('location_code')
            model_instance.duns=request.POST.get('duns')
            model_instance.facility_name=request.POST.get('facility_name')
            model_instance.city=request.POST.get('facility_name')
            model_instance.state=request.POST.get('state')
            model_instance.city=request.POST.get('city')
            model_instance.dock_code=request.POST.get('dock_code')
            model_instance.no_of_shifts=request.POST.get('no_of_shifts')
            model_instance.drop_deck_allowed_yn=drop_deck_allowed_yn
            model_instance.dock_bump_yn=dock_bump_yn
            model_instance.max_dock_bumps_allowed=request.POST.get('max_dock_bumps_allowed')
            model_instance.notes=request.POST.get('notes')
            model_instance.co_locate=request.POST.get('co_locate')
            model_instance.save()

            compatibles = list(request.POST.getlist('dock-constraint'))
            print(compatibles)

            model_instance = BH_GM_DOCK.objects.get(bh_gm_dock_id=id)

            for compatible in compatibles:
                BH_GM_Constraint_Dock.objects.create(bh_origin_id=model_instance, bh_compatible_dock_id=compatible)

            return redirect("/tabledata")
        else:
            return render_to_response(self.template_name, {'form': form})


class AddBHGMDock(View):
    template_name = 'tabledata/add.html'

    def get(self, request):
        form = BHGMDOCKForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BHGMDOCKForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/tabledata")
        else:
            return render_to_response(self.template_name, {'form': form})



class ViewBHGMDock(View):
    template_name = 'tabledata/view.html'

    def get(self, request, id):
        if not id:
            return render(request, 'tabledata/404.html')
        else:

            try:
                data = BH_GM_DOCK.objects.all().order_by('-bh_gm_dock_id')

                row_list = list()
                rows = dict()

                for i in data:
                    rows['bh_gm_dock_id'] = i.bh_gm_dock_id
                    rows['location_id'] = i.location
                    rows['billing_cisco'] = i.billing_cisco
                    rows['location_code'] = i.location_code
                    rows['duns'] = i.duns
                    rows['facility_name'] = i.facility_name
                    rows['zip_code'] = i.zip_code
                    rows['dock_code'] = i.dock_code
                    rows['simplified_dock'] = i.simplified_dock
                    rows['no_of_shifts'] = i.no_of_shifts
                    rows['drop_deck_allowed_yn'] = i.drop_deck_allowed_yn
                    rows['dock_bump_yn'] = i.dock_bump_yn
                    rows['max_dock_bumps_allowed'] = i.max_dock_bumps_allowed
                    rows['date_entered'] = i.date_entered
                    rows['notes'] = i.notes
                    rows['co_locate'] = i.co_locate
                    rows['source'] = i.source

                    if i.location:
                        query = Location.objects.get(location_id=i.location.location_id)
                        rows['city'] = query.city
                        rows['state'] = query.state
                    else:
                        rows['city'] = 'None'
                        rows['state'] = 'None'

                    row_list.append(rows)
                    rows = dict()

                    return render(request, self.template_name, context={"rows": row_list})
            except IndexError:
                return render(request, 'tabledata/404.html')


class SearchLocation(View):
    def get(self, request):
        object = Location.objects.all()
        data = serializers.serialize('json', object)
        return HttpResponse(data, content_type='application/json')


class CodeMapView(View):
    template_name = 'tabledata/code-map.html'

    def get(self, request):
        codemap = Codemap.objects.all()
        return render(request, self.template_name, context={'rows': codemap})


class EditCodeMap(View):
    template_name = 'tabledata/code-map-edit.html'

    def get(self, request, id):
        cmap = Codemap.objects.get(code_map_id=id)
        form = CodeMapForm(instance=cmap)
        return render(request, self.template_name, context={'form': form})

    def post(self, request, id):
        form = CodeMapForm(request.POST)
        if form.is_valid():
            codemap_instance = Codemap.objects.get(code_map_id=id)
            codemap_instance.input_value = request.POST.get('input_value')
            codemap_instance.output_value = request.POST.get('output_value')
            codemap_instance.display_label = request.POST.get('display_label')
            codemap_instance.type = request.POST.get('type')
            try:
                codemap_instance.save()
                return redirect('code-map-view')
            except Exception as e:
                print(e)

class AddCodeMap(View):
    template_name = 'tabledata/add-codemap.html'

    def get(self, request):
        form = CodeMapForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = CodeMapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('code-map-view')
