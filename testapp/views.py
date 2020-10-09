from django.shortcuts import render
from django.views.generic import View
from testapp.models import Student
import json
from django.http import HttpResponse
# from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import StudentForm
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except Student.DoesNotExist:
            stud=None
        return stud

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            stud=self.get_object_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'The requested resource not available with matched id'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.serialize([stud,])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        studdata=json.loads(data)

        form=StudentForm(studdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mandatory..Please provide id'})
            return render_to_http_response(json_data,status=400)
        stud=self.get_object_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'No resource with matched id can not update'})
            return self.render_to_http_response(json_data,status=400)
        provided_data=json.loads(data)
        original_data={
        'name':stud.name,
        'email':stud.email,
        'dob':stud.dob,
        'profile_pic':stud.profile_pic,
        'fees':stud.fees
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            stud=self.get_object_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'The requested resource is not available with matched id'})
                return self.render_to_http_response(json_data,status=400)
            status,deleted_item=stud.delete()
            if status==1:
                json_data=json.dumps({'msg':'Resource deleted successfully'})
                return self.render_to_http_response(json_data)
            json_data=json.dumps({'msg':'Unable to delete....Please try again.'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'To perform deletion id is mandatory....Please provide id'})
        return self.render_to_http_response(json_data,status=400)
