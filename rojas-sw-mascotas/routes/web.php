<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

/**$router->get('/', function () use ($router) {
    return $router->app->version();
});**/


function resource($uri, $controller, $router)
{
    //$verbs = ['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE'];
    $router->get($uri, $controller.'@index');
    $router->post($uri, $controller.'@create');
    $router->post($uri.'/add_pets', $controller.'@addPet');
    $router->get($uri.'/pets/{id}', $controller.'@getPets');
    $router->post($uri.'/add_Appointment', $controller.'@addAppointment');
    $router->put($uri.'/{id}', $controller.'@edit');
    $router->post($uri.'/sign_in', $controller.'@login');
}
resource('sw/client', 'ClientController', $router);