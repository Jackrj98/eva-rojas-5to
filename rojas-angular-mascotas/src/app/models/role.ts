import {FormGroup, FormControl, Validators} from '@angular/forms';

export class Role {
  id: number;
  name: string;

  static getForm(role?: Role) {
    return new FormGroup({
      id: new FormControl(role.id),
      name: new FormControl(role.name, {validators: Validators.required})
    });
  }
}
