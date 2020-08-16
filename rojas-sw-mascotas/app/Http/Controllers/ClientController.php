<?php

namespace App\Http\Controllers;

use App\Role;
use App\Person;
use App\Account;
use App\Pets;
use App\Appointment;

use Illuminate\Support\Facades\Hash;
use Illuminate\Hashing\BcrypHasher;
use Illuminate\Support\Str;
use App\Http\Helper\ResponseBuilder;
use Illuminate\Http\Request;

class ClientController extends Controller
{
    
    public function __construct(\App\Person $client)
    {
        $this->client = $client;
        
    }   

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(\App\Person $client)
    {
        return $client->paginate(10);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create(Request $request)
    {
        $client = new Person();
        $account = new Account();
        $role = Role::where('name', 'Client')->first();
        $client->lastname = $request->lastname;
        $client->name = $request->name;
        $client->cedula = $request->cedula;
        $client->nro_phone = $request->nro_phone;
        $client->role_id = $role->id;
        if($client->save()){
            $account->email=$request->email;
            $account->external_id = 222;
            $account->password= $request->password;
            $account->is_active = true;
            $account->is_staff = false;
            $account->is_superuser = false;
            if($account->save()){
                return response() -> json($client, 201);
            }
        }        
    }

     /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit(Request $request, $id)
    {
        $client = Person::where('id', $id)->first();
        $client->account;
        if (!empty($client)) {
            $client->lastname = $request->lastname;
            $client->name = $request->name;
            $client->nro_phone = $request->nro_phone;
            //$client->save();
            $client->account->password = $request->password;
            $client->account->is_active = $request->is_active;
            $client->account->save();
        }        
        return response() -> json($client, 200);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function addPet(Request $request)
    {   
        $pet = new Pets();        
        $pet->name = $request->name;
        $pet->raza = $request->raza;
        $pet->type = $request->type;
        $pet->height = $request->height;
        $pet->status = true;
        $pet->person_id = $request->person;
        if($pet->save()){
            return response() -> json($pet, 201);
        }        
        
    }

    public function getPets(Request $request)
    {   
        $client = Person::where('id', $request->id)->first();
        $pets = Pets::where('person_id', $client->id)->get();
        if($pets){
            return response() -> json($pets, 200);
        }

    }

    
    public function addAppointment(Request $request)
    {
       // $client = Person::where('id', $request->id)->first();
        $appointment = new Appointment();
        $appointment->external_id = 2323;
        $appointment->date=$request->date;
        $appointment->time=$request->time;
        $appointment->status=true;
        $appointment->person_id=$request->person;
        if($appointment->save()){
            return response() -> json($appointment, 201);
        }
    }  

    public function login(Request $request){
        $email = $request->email;
        $password = $request->password;
        $user = Account::where('email', $email)->first();
        error_log($this->django_password_verify($password, $user->password));
        error_log($user->password);
        if (!empty($user)) {
            if ($this->django_password_verify($password, $user->password)) {
                $user->api_token= Str::random(150);
                $user->save();
                $status = true;
            } else {
                $status = false;
                $info = "el usuaio parece sospechoso,intente de nuevo ";
            }
        } else {
            $status = false;
            $info = "el usuaio parece sospechoso, intente de nuevo ";
        }
        return response() -> json($user->api_token, 201);
    }

    public function django_password_verify(string $password, string $djangoHash): bool
    {
        $pieces = explode('$', $djangoHash);
        if (count($pieces) !== 4) {
            throw new Exception("Illegal hash format");
        }
        list($header, $iter, $salt, $hash) = $pieces;
        // Get the hash algorithm used:
        if (preg_match('#^pbkdf2_([a-z0-9A-Z]+)$#', $header, $m)) {
            $algo = $m[1];
        } else {
            throw new Exception(sprintf("Bad header (%s)", $header));
        }
        if (!in_array($algo, hash_algos())) {
            throw new Exception(sprintf("Illegal hash algorithm (%s)", $algo));
        }
        //formato PBKDF2
        $calc = hash_pbkdf2(
            //ALGO =MD5,SHA256, haval1604
            //salt = generar valores aletorios
            $algo,
            $password,
            $salt,
            (int) $iter,
            32,
            true
        );
        return hash_equals($calc, base64_decode($hash));
    }
}
