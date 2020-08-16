import {Component, OnInit, Input} from '@angular/core';
import {AuthenticationService} from 'src/app/services/authentication.service';
import {AppComponent} from 'src/app/app.component';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  currentUser = this.authenticationService.currentUserValue;
  loading = false;


  constructor(
    private authenticationService: AuthenticationService,
    protected appComponent: AppComponent,

  ) {
  }

  ngOnInit(): void {

  }


}
