<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Appointment extends Model
{
    protected $table = 'appointment';
    protected $fillable = ['id', 'date', 'time', 'height', 'status'];
    public $timestamps = false;

    public function person()
    {
        return $this->belongsTo('App\Person');
    }
}
