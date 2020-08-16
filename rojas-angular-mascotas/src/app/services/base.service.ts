import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export abstract class BaseService {
  abstract apiURL: string;

  constructor(protected http: HttpClient) {}

  public retrieve(id: string): Observable<any> {
    return this.http.get<any>(this.apiURL + id + '/');
  }

  public create(object: any): Observable<any> {
    return this.http.post<any>(this.apiURL, object);
  }

  public update(object: any): Observable<any> {
    return this.http.put<any>(this.apiURL + object.id + '/', object);
  }

  public list(): Observable<any[]> {
    return this.http.get<any>(this.apiURL);
  }

  public createOrUpdate(object: any): Observable<any> {
    if (object.id == null) {
      return this.create(object);
    } else {
      return this.update(object);
    }
  }
}
