import {Component, OnInit, Inject} from '@angular/core';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import {Router} from '@angular/router';

import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
/*SERVICES*/
import {ClientService} from 'src/app/services/client.service';

/*MODELS*/
import {Person} from 'src/app/models/person';
import {Role} from 'src/app/models/role';
import {Account} from 'src/app/models/account';

@Component({
  selector: 'app-client',
  templateUrl: './client.component.html',
  styleUrls: ['./client.component.scss']
})
export class ClientComponent implements OnInit {

  title = 'Clients Pets';
  clients: Person[];
  client: Person;
  role: Role;
  account: Account;
  data: any[];
  formClient: FormGroup;
  formAccount: FormGroup;

  constructor(
    private clientService: ClientService,
    private router: Router
  ) {
    this.client = new Person();
    this.account = new Account();
  }

  ngOnInit(): void {
    this.formClient = Person.getForm(this.client);
    this.formAccount = Account.getForm(this.account);
  }

  cancel() {
    this.router.navigate(['']);
  }

  accept() {

    this.account = this.formAccount.value;

    this.formClient.get('email').setValue(this.account.email);
    this.formClient.get('password').setValue(this.account.password);
    console.log(this.formClient.value);
    this.clientService.createOrUpdate(this.formClient.value).subscribe((client) => {
      if (client) {
        return this.router.navigate(['']);
      }
    }, error => {
      console.log(error);
    });
  }


}
