import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './table.component.html',
  styleUrl: './table.component.css'
})
export class TableComponent implements OnInit{
  item_list: any = [];
  description: string = "This table is our inventory";

  constructor(private apiService: ApiService){

  }

  ngOnInit(): void {
    this.apiService.getInventoryTable().subscribe({
      next: (response) => {
        this.item_list = response;
      },
      error: (error) => {
        console.error('Error fetching data:', error);
      }
    });
  }

}
