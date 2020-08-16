import {Component, OnInit, Inject} from '@angular/core';
import {FormGroup} from '@angular/forms';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
/*SERVICE*/
import {ClientService} from 'src/app/services/client.service';
/*MODELS*/
import {Pet} from 'src/app/models/pet';

@Component({
  selector: 'app-dialog-pet',
  templateUrl: './dialog-pet.component.html',
  styleUrls: ['./dialog-pet.component.scss']
})
export class DialogPetComponent implements OnInit {
  title: string;
  pet: Pet;
  formPet: FormGroup;

  constructor(
    @Inject(MAT_DIALOG_DATA) data,
    private clientService: ClientService,
    private dialog: MatDialogRef<DialogPetComponent>
  ) {
    this.title = data.title;
    this.pet = data.pet;
  }

  ngOnInit(): void {
    this.formPet = Pet.getForm(this.pet);
  }

  cancel() {
    this.dialog.close(null);
  }

  accept() {
    console.log(this.formPet.value);
    this.formPet.get('person').setValue('2')
    this.clientService.add_pets(this.formPet.value).subscribe(data => {
      if (data) {
        this.dialog.close(data);
      }
    }, error => {
      console.log(error);
      this.dialog.close(null);
    });
  }
}
