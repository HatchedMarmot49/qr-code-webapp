import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private api_test = "/api/test"
  private api_items = "/api/items"

  constructor(private http: HttpClient ) {

  }


  getTestMessage(): Observable<any>{
    return this.http.get<any>(this.api_test);
  }

  getInventoryTable(): Observable<any>{
    return this.http.get<any>(this.api_items);
  }
}

/*
//interface example

interface TestResponse {
  message: string;
  description: string;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private api_url = "/api/test";

  constructor(private http: HttpClient) {}

  getTestMessage(): Observable<TestResponse> {
    return this.http.get<TestResponse>(this.api_url);
  }
}

*/