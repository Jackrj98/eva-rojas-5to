<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Person extends Model
{
    protected $table = 'person';
    protected $fillable = ['id', 'cedula', 'lastname', 'name', 'nro_phone', 'createdAt','updatedAt'];
    public $timestamps = false;

    public function account()
    {
        return $this->hasOne('App\Account');
    }

    public function pets()
    {
        return $this->hasMany('App\Pets');
    }

    public function appointment()
    {
        return $this->hasMany('App\Appointment');
    }

    public function role()
    {
        return $this->belongsTo('App\Role');
    }
}   
