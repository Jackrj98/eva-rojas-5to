import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Person } from './person';


export class Appointment {
  id: number;
  date: string;
  time: string;
  status: boolean;
  person: Person | any;


  static getForm(appointment?: Appointment) {
    return new FormGroup({
      id: new FormControl(appointment.id),
      date: new FormControl(appointment.date, {validators: Validators.required}),
      time: new FormControl(appointment.time, {validators: Validators.required}),
      person: new FormControl(appointment.person, {validators: Validators.required}),
    });
  }
}
