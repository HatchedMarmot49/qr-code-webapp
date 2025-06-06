import { Component } from '@angular/core';
import { TableComponent } from '../../components/table/table.component';

@Component({
  selector: 'app-welcome',
  imports: [TableComponent],
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.css'
})
export class WelcomeComponent {

}
