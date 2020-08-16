import {Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
/*MODEL*/
import {Pet} from 'src/app/models/pet';

@Component({
  selector: 'app-util-pets',
  templateUrl: './util-pets.component.html',
  styleUrls: ['./util-pets.component.scss']
})
export class UtilPetsComponent implements OnInit {
  @Input() pets: Pet[];
  @Output() emitEdit = new EventEmitter();
  @Output() emitEditAccount = new EventEmitter();
  @Output() emitDown = new EventEmitter();
  @Output() emitTop = new EventEmitter();
  @Output() emitRead = new EventEmitter();

  constructor() {
  }

  ngOnInit(): void {
  }

  actionEdit(params) {
    this.emitEdit.emit(params);
  }

  actionEditAccount(params) {
    this.emitEditAccount.emit(params);
  }

  actionDown(params) {
    this.emitDown.emit(params);
  }

  actionTop(params) {
    this.emitTop.emit(params);
  }

  actionRead(params) {
    this.emitRead.emit(params);
  }

}
