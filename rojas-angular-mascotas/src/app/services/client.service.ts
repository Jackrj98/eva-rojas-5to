import {Injectable} from '@angular/core';
import {BaseService} from './base.service';
import {environment} from '../../environments/environment';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClientService extends BaseService {

  protected http: HttpClient;
  apiURL = environment.apiURL;
  api: string;

  add_pets(object: any): Observable<any> {
    //this.api = this.apiURL + 'add_pets/2/';
    return this.http.post<any>(this.apiURL + 'add_pets/', object);
  }

  add_appointment(object: any): Observable<any> {
    return this.http.post<any>(this.apiURL + 'add_Appointment/', object);
  }

  get_pets(params) {
    return this.http.get<any>(this.apiURL + 'pets/' + params + '/');
  }

}
