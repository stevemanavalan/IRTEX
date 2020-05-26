import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UploadserviceService {
  constructor(private http: HttpClient) {
    
  }
  uploadImage(formData){
    return this.http.post<any>('fileupload', formData)
  }
  getImages(){
    return this.http.get('lists',{});
  }
  runscript(formData){
    return this.http.post<any>('runscript',formData,{observe:"response", responseType: 'json'});

  }
  persistQueryObj(repoImg,qid){
    var queryRepoList = []
    queryRepoList.push(qid)
    queryRepoList.push(repoImg)
    return this.http.post<any>('persistQueryObj', queryRepoList)
  }
}
