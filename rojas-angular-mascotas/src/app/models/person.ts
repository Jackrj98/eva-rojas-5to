import {FormGroup, FormControl, Validators} from '@angular/forms';
import {Role} from './role';


export class Person {
  /*INIT PERSON*/
  id: number;
  lastname: string;
  name: string;
  nro_phone: string;
  cedula: string;
  role: Role | any;
  /*END PERSON*/
  /*INIT ACCOUNT*/
  email: string;
  password: string;
  /*END ACCOUNT*/

  static getForm(person?: Person) {
    return new FormGroup({
      id: new FormControl(person.id),
      name: new FormControl(person.name, {validators: Validators.required}),
      lastname: new FormControl(person.lastname, {validators: Validators.required}),
      nro_phone: new FormControl(person.nro_phone, [Validators.required, Validators.minLength(2), Validators.maxLength(10)]),
      cedula: new FormControl(person.cedula, {validators: Validators.required}),
      email: new FormControl(person.email, {validators: Validators.required}),
      password: new FormControl(person.password, [Validators.required, Validators.minLength(5), Validators.maxLength(25)]),
      role: new FormControl(person.role, {validators: Validators.required}),
    });
  }
}
