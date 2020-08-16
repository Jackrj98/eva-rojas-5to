import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Person } from './person';


export class Pet {
  id: number;
  name: string;
  raza: string;
  type: string;
  height: number;
  person: Person | any;


  static getForm(pet?: Pet) {
    return new FormGroup({
      id: new FormControl(pet.id),
      name: new FormControl(pet.name, {validators: Validators.required}),
      raza: new FormControl(pet.raza, {validators: Validators.required}),
      type: new FormControl(pet.type, {validators: Validators.required}),
      height: new FormControl(pet.height, [Validators.required, Validators.required]),
      person: new FormControl(pet.person, {validators: Validators.required}),
    });
  }
}
