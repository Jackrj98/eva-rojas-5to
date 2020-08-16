import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {ClientComponent} from './components/client/client.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';

import {UtilModule} from './util/util.module';
import {ShareModule} from './share/share.module';
import { PetsComponent } from './components/pets/pets.component';
import { DialogPetComponent } from './components/pets/dialog-pet/dialog-pet.component';
import { DialogAppointComponent } from './components/pets/dialog-appoint/dialog-appoint.component';
import { LoginComponent } from './components/login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    ClientComponent,
    PetsComponent,
    DialogPetComponent,
    DialogAppointComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    UtilModule,
    ShareModule,
    HttpClientModule,
  ],
  exports: [
    ClientComponent
  ],
  entryComponents: [
    ClientComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
