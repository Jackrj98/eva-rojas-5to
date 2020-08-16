import {Component, OnInit, Inject} from '@angular/core';
import {FormGroup} from '@angular/forms';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
/*SERVICE*/
import {ClientService} from 'src/app/services/client.service';
/*MODELS*/
import {Appointment} from 'src/app/models/appointment';


@Component({
  selector: 'app-dialog-appoint',
  templateUrl: './dialog-appoint.component.html',
  styleUrls: ['./dialog-appoint.component.scss']
})
export class DialogAppointComponent implements OnInit {

  title: string;
  appointment: Appointment;
  formAppointment: FormGroup;

  constructor(
    @Inject(MAT_DIALOG_DATA) data,
    private clientService: ClientService,
    private dialog: MatDialogRef<DialogAppointComponent>
  ) {
    this.title = data.title;
    this.appointment = data.appointment;
  }

  ngOnInit(): void {
    this.formAppointment = Appointment.getForm(this.appointment);
  }

  cancel() {
    this.dialog.close(null);
  }

  accept() {
    console.log(this.formAppointment.value);
    this.formAppointment.get('person').setValue('2');
    this.clientService.add_appointment(this.formAppointment.value).subscribe(data => {
      if (data) {
        this.dialog.close(data);
      }
    }, error => {
      console.log(error);
      this.dialog.close(null);
    });
  }

}
