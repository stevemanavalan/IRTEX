import { Component, OnInit } from '@angular/core';
import { UploadserviceService } from './uploadservice.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import * as HighCharts from 'highcharts';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Image Search';
  file = {};
  imgNameList = [];
  jsonImageObj = [];
  uploadForm: FormGroup;
  imageForm;
  queryId = '';
  resultsCount : number;
  uploadedImages : Array<string> = [];
  addinputValue: string = "";
  description: string = "";
  constructor(private uploadservice:UploadserviceService,private formBuilder: FormBuilder, private httpClient: HttpClient){}
  runscript(){
    this.resultsCount = 0;
    this.imgNameList = []
    const formData = new FormData();
    formData.append('file', this.uploadForm.get('file').value);
    this.imageForm = this.uploadForm.get('file').value;
    this.uploadservice.runscript(formData).subscribe(res =>{
      this.jsonImageObj = [];
      var matchedImages = res.body;
      console.log(res.headers.get('qId'));
      this.queryId = res.headers.get('qId');
      this.jsonImageObj = JSON.parse(matchedImages.toString());
      for (var i = 0; i < this.jsonImageObj.length; i++) {
        this.imgNameList.push(this.jsonImageObj[i].name);
      }
      
      this.resultsCount = this.imgNameList.length;
    })
  }
  ngOnInit() {
    this.uploadForm = this.formBuilder.group({
      file: ['']
    });
  }
  fileChange(event) {
    this.uploadedImages = []
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      //addinputValue: string = ""
      this.uploadForm.get('file').setValue(file);
      this.uploadedImages.push(file.name);
     }
  }
  upload(){
    const formRepoImage = new FormData();
    formRepoImage.append('file', this.uploadForm.get('file').value);
    this.uploadservice.uploadImage(formRepoImage).subscribe(
      (res) => console.log(res),
      (err) => console.log(err)
    );   
  }
  persistId(item){
    const queryImage = new FormData();  
    queryImage.append('file', this.uploadForm.get('file').value);
    //console.log(this.imageForm);
    console.log(this.queryId);
    var qId = this.queryId;
    this.uploadservice.persistQueryObj(item,qId).subscribe(res =>{
    var matchedImages = res;      
    })
  }
  displayChart(item) {
    this.description= `The selected image matches ${item.color} percentage with color, shape and texture of the query image.`
    console.log(item)
    HighCharts.chart('pieChart', {
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
      },
      title: {
        text: 'Feature 1 Contribution'
      },
      tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
            enabled: true,
            format: '<b>{point.name}</b>: {point.percentage:.1f} %'
          }
        }
      },
      series: [{
        name: 'Color, Shape and Texture',
        colorByPoint: true,
        type: undefined,
        data: [{
          name: 'Similarity',
          y: parseFloat(item.color),
          sliced: true,
          selected: true
        }, {
          name: 'Dissimiarity',
          y: parseFloat(item.fg)
        }]
      }]
    });
  }
}

