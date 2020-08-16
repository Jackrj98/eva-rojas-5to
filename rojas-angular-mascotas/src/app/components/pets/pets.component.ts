import {Component, OnInit} from '@angular/core';
import {MatDialog, MatDialogConfig} from '@angular/material/dialog';
import {DialogPetComponent} from './dialog-pet/dialog-pet.component';
import {DialogAppointComponent} from './dialog-appoint/dialog-appoint.component';
import {Router} from '@angular/router';
import {ClientService} from 'src/app/services/client.service';

import {Pet} from 'src/app/models/pet';
import {Appointment} from 'src/app/models/appointment';
import {Person} from 'src/app/models/person';


@Component({
  selector: 'app-pets',
  templateUrl: './pets.component.html',
  styleUrls: ['./pets.component.scss']
})
export class PetsComponent implements OnInit {

  title = 'List Pets';
  pets: Pet[];
  pet: Pet;
  appointment: Appointment;
  client: Person;

  constructor(
    private clientService: ClientService,
    private router: Router,
    private dialog: MatDialog
  ) {
  }

  ngOnInit(): void {
    this.list();
  }

  list() {
    this.clientService.get_pets(2).subscribe(data => {
      if (data) {
        this.pets = data;
        console.log(data);
      }
    }, error => {
      console.log(error);
    });
  }

  create() {
    this.pet = new Pet();
    this.openDialog('Pets Register');
  }

  openDialog(title) {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.data = {
      title: title,
      pet: this.pet,
    };
    const dialogRef = this.dialog.open(DialogPetComponent, {
      data: dialogConfig.data,
    });
    dialogRef.afterClosed().subscribe(
      (res) => {
        this.list();
      },
      (error) => {
        console.log(error + '  Problem');
      }
    );
  }

  add_appoint() {
    this.appointment = new Appointment();
    this.openDialogAppo('Appointment Register');
  }

  openDialogAppo(title) {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.data = {
      title: title,
      appointment: this.appointment,
    };
    const dialogRef = this.dialog.open(DialogAppointComponent, {
      data: dialogConfig.data,
    });
    dialogRef.afterClosed().subscribe(
      (res) => {
        this.list();
      },
      (error) => {
        console.log(error + '  Problem');
      }
    );
  }

}
