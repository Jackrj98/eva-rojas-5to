<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Pets extends Model
{
    protected $table = 'pets';
    protected $fillable = ['id', 'name', 'raza', 'type', 'height', 'status'];
    public $timestamps = false;

    public function person()
    {
        return $this->belongsTo('App\Person');
    }
}
