import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
/*CAN-ACTIVE*/
import { AuthGuard } from './helpers/auth.guard';

import { LoginComponent } from './components/login/login.component';
import {ClientComponent} from './components/client/client.component';
import {PetsComponent} from './components/pets/pets.component';

const routes: Routes = [
  { path: 'register-client', component: ClientComponent },
  { path: '', component: PetsComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
