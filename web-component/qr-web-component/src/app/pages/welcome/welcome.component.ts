import { Component, OnInit } from '@angular/core';
import { TableComponent } from '../../components/table/table.component';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { NavComponent } from '../../components/nav/nav.component';


@Component({
  selector: 'app-welcome',
  standalone: true,
  imports: [TableComponent, CommonModule, NavComponent],
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.css'
})

export class WelcomeComponent /*implements OnInit*/ {
  // welcome_message: string = "";
  // description: string = "";

  // constructor(private apiService: ApiService){

  // }

  // ngOnInit(): void {
  //   this.apiService.getTestMessage().subscribe({
  //     next: (response) => {
  //       this.welcome_message = response.message;
  //       this.description = response.description;
  //     },
  //     error: (error) => {
  //       console.error('Error fetching data:', error);
  //     }
  //   });
  // }

}