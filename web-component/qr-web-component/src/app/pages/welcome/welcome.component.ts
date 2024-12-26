import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-welcome',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.css'
})
export class WelcomeComponent implements OnInit {
  welcome_message: string = "";
  description: string = "";

  constructor(private apiService: ApiService){

  }

  ngOnInit(): void {
    this.apiService.getTestMessage().subscribe({
      next: (response) => {
        this.welcome_message = response.message;
        this.description = response.description;
      },
      error: (error) => {
        console.error('Error fetching data:', error);
      }
    });
  }

}