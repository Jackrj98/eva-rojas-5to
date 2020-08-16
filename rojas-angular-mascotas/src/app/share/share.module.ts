import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { UtilModule } from '../util/util.module';

import { NavComponent } from './nav/nav.component';
import {UtilPetsComponent} from './util-pets/util-pets.component';

@NgModule({
  declarations: [
    NavComponent,
    UtilPetsComponent,
  ],
  imports: [
    CommonModule,
    UtilModule,
    RouterModule
  ],
  exports: [
    NavComponent,
    UtilPetsComponent,
  ],
})
export class ShareModule { }
