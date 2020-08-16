import {FormGroup, FormControl, Validators} from '@angular/forms';
import {Person} from './person';

export class Account {

  id: number;
  email: string;
  password: string;
  is_active: boolean;
  is_staff: boolean;
  api_token: string;
  person: Person | any;




  static getForm(account?: Account) {
    return new FormGroup({
      id: new FormControl(account.id),
      email: new FormControl(account.email, {validators: Validators.required}),
      password: new FormControl(account.password, {validators: Validators.required}),
      is_staff: new FormControl(account.is_staff, {validators: Validators.required}),
      person: new FormControl(account.person, {validators: Validators.required}),
    });
  }
}
